from PIL import Image
import os
# using venv
source_folder = 'output'
destination_folder = 'new/'
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    
directory = os.listdir(source_folder)
    
for item in directory:
    img = Image.open(source_folder + '/' + item)
    imgResize = img.resize((1600, 900), Image.LANCZOS)
    imgResize.save(destination_folder + item[:-4] +'.png', quality = 90)