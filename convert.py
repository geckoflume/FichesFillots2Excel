import os
from shutil import rmtree
import pdf2image

form_dir = 'formulaires/'
temp_dir = 'temp/'
dpi = 250

if os.path.exists(temp_dir):
    rmtree(temp_dir, ign)

def create_temp(name):
    os.makedirs(temp_dir + name, mode=0o777, exist_ok=True)

def extract_images():
    for file in os.listdir(form_dir):
        filename, file_extension = os.path.splitext(file)
        actual = filename.replace(' ', '-')
        create_temp(actual)
        print('Current file: ' + file + '...')
        pdf2image.convert_from_path(form_dir + file, dpi, fmt='jpeg', output_folder=temp_dir + actual)
        print('Done!')

def separate_forms():
    for file in os.listdir(form_dir):
        filename, file_extension = os.path.splitext(file)
        actual = filename.replace(' ', '-')
        count = 0
        pics = os.listdir(temp_dir + actual)
        for pic in range(0, len(pics), 2):
            actual_form = actual + '/' + str(count)
            create_temp(actual_form)
            os.rename(temp_dir + actual + '/' + pics[pic], temp_dir + actual_form + '/' + pics[pic])
            os.rename(temp_dir + actual + '/' + pics[pic + 1], temp_dir + actual_form + '/' + pics[pic + 1])
            count += 1

extract_images()
separate_forms()


#for page in pages:
#    page.save('out.jpg', 'JPEG')
