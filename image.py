import os, sys
from PIL import Image

size = 2560, 1440

input_file_path = './input'
output_file_path = './output/'

for file in os.listdir(input_file_path):
    print(file)
    im = Image.open(os.path.join(input_file_path, file))
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(output_file_path + file, "JPEG")
    