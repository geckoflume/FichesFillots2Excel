import os
from shutil import rmtree
import pdf2image

form_dir = 'formulaires/'
temp_dir = 'temp/'
dpi = 250

rmtree(temp_dir)

def create_temp(name, count):
    os.makedirs(temp_dir + name + '/' + str(count), mode=0o777, exist_ok=True)

for file in os.listdir(form_dir):
    filename, file_extension = os.path.splitext(file)
    actual = filename.replace(' ', '-')
    nbForms = pdf2image._page_count(form_dir + file)
    print('Current file: ' + file + ' ('+ str(int(nbForms / 2)) + ' forms)...')
    count = 0
    for page in range(1, nbForms, 2) :
        create_temp(actual, count)
        pdf2image.convert_from_path(form_dir + file, dpi, first_page=page, last_page = min(page + 2 - 1, nbForms), fmt='jpeg', output_folder=temp_dir + actual+ '/' + str(count))
        count += 1
    print('Done!')



#for page in pages:
#    page.save('out.jpg', 'JPEG')
