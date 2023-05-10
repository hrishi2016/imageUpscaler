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

# Define the output ratio as a decimal
output_ratio = 0.8  # 4:5 ratio = 0.8

# Loop through all the image files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        
        # Load the input image
        input_image_path = os.path.join(input_dir, filename)
        input_image = Image.open(input_image_path)

        # Get the original dimensions of the input image
        input_width, input_height = input_image.size

        # Calculate the output dimensions based on the output ratio
        if input_width / input_height > output_ratio:
            output_width = int(input_height * output_ratio)
            output_height = input_height
        else:
            output_width = input_width
            output_height = int(input_width / output_ratio)

        # Calculate the cropping parameters
        left = (input_width - output_width) / 2
        top = (input_height - output_height) / 2
        right = (input_width + output_width) / 2
        bottom = (input_height + output_height) / 2

        # Use the Pillow library to crop and resize the input image to the output dimensions
        output_image = input_image.crop((left, top, right, bottom)).resize((1080, 1350), resample=Image.BICUBIC)

        # Define the output path for the cropped and resized image
        output_image_path = os.path.join(output_dir, filename)

        # Save the cropped and resized image to the output directory
        output_image.save(output_image_path)

        print(f'{filename} cropped and resized to Instagram ratio and saved to {output_image_path}.')
