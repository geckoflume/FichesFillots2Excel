import os
from shutil import rmtree
from pdf2image import convert_from_path

form_dir = 'formulaires/'
temp_dir = 'temp/'
dpi = 250

def create_temp(name):
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    rmtree(temp_dir + name)
    os.mkdir(temp_dir + name)

for file in os.listdir(form_dir):
    filename, file_extension = os.path.splitext(file)
    actual = filename.replace(' ', '-')
    print('Current form: ' + file + '...')
    create_temp(actual)
    pages = convert_from_path(form_dir + file, dpi, fmt='jpeg', output_folder=temp_dir + actual)
    print('Done!')


#for page in pages:
#    page.save('out.jpg', 'JPEG')
