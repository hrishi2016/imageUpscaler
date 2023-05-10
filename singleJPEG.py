# Install dependencies
!pip install pillow google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Authenticate and mount Google Drive
from google.colab import auth
from google.colab import drive

auth.authenticate_user()
drive.mount('/content/drive')

# Import necessary libraries
from PIL import Image

# Define the path to the input and output images
input_image_path = '/content/drive/MyDrive/input_image.jpg'
output_image_path = '/content/drive/MyDrive/output_image.jpg'

# Define the scale factor for the image upscale
scale_factor = 2

# Load the input image
input_image = Image.open(input_image_path)

# Get the original dimensions of the input image
input_width, input_height = input_image.size

# Calculate the output dimensions based on the scale factor
output_width = input_width * scale_factor
output_height = input_height * scale_factor

# Use the Pillow library to resize the input image to the output dimensions
output_image = input_image.resize((output_width, output_height), resample=Image.BICUBIC)

# Save the output image to Google Drive
output_image.save(output_image_path)
