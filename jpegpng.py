# Install dependencies
!pip install pillow google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Authenticate and mount Google Drive
from google.colab import auth
from google.colab import drive

auth.authenticate_user()
drive.mount('/content/drive')

# Import necessary libraries
from PIL import Image
import os

# Define the path to the input directory and output directory
input_dir = '/content/drive/MyDrive/input_images/'
output_dir = '/content/drive/MyDrive/output_images/'

# Define the scale factor for the image upscale
scale_factor = 2

# Loop through all the image files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        
        # Load the input image
        input_image_path = os.path.join(input_dir, filename)
        input_image = Image.open(input_image_path)

        # Get the original dimensions of the input image
        input_width, input_height = input_image.size

        # Calculate the output dimensions based on the scale factor
        output_width = input_width * scale_factor
        output_height = input_height * scale_factor

        # Use the Pillow library to resize the input image to the output dimensions
        output_image = input_image.resize((output_width, output_height), resample=Image.BICUBIC)

        # Define the output path for the upscaled image
        output_image_path = os.path.join(output_dir, filename)

        # Save the upscaled image to the output directory
        output_image.save(output_image_path)

        print(f'{filename} upscaled and saved to {output_image_path}.')
