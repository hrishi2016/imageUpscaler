# Install dependencies
!pip install pillow google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client OpenEXR numpy

# Authenticate and mount Google Drive
from google.colab import auth
from google.colab import drive

auth.authenticate_user()
drive.mount('/content/drive')

# Import necessary libraries
import OpenEXR
import numpy as np
from PIL import Image
import os

# Define the path to the input directory and output directory
input_dir = '/content/drive/MyDrive/input_exr/'
output_dir = '/content/drive/MyDrive/output_exr/'

# Define the scale factor for the image upscale
scale_factor = 2

# Define the output resolution in pixels
output_width = 3840
output_height = 2160

# Loop through all the image files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.exr'):
        
        # Load the input EXR image
        input_image_path = os.path.join(input_dir, filename)
        input_file = OpenEXR.InputFile(input_image_path)
        input_header = input_file.header()
        input_size = (input_header['dataWindow'].max.x + 1, input_header['dataWindow'].max.y + 1)
        input_channels = input_header['channels'].keys()
        input_data = {}

        for channel in input_channels:
            input_data[channel] = np.frombuffer(input_file.channel(channel), dtype=np.float32).reshape(input_size[::-1])
        
        # Calculate the output size based on the output resolution and scale factor
        output_size = (output_width // scale_factor, output_height // scale_factor)

        # Use NumPy to resize the input image data to the output size
        output_data = {}
        for channel in input_channels:
            output_data[channel] = np.zeros(output_size, dtype=np.float32)
            output_data[channel] = np.asarray(Image.fromarray(input_data[channel]).resize(output_size, resample=Image.BICUBIC))

        # Use OpenEXR to save the output data to the output directory
        output_image_path = os.path.join(output_dir, filename)
        output_file = OpenEXR.OutputFile(output_image_path, input_header)
        for channel in input_channels:
            output_file.writePixels({channel: output_data[channel].tostring()})

        print(f'{filename} upscaled and saved to {output_image_path}.')
