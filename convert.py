import os
from shutil import rmtree
import pdf2image
from PIL import Image

form_dir = 'formulaires/'
temp_dir = 'temp/'
dpi = 250
cropping_data = [(0, 0.55, 0, 0.35, 0.07, "name"),
(0, 0.55, 0.4, 0.2, 0.04, "gender"),
(0, 0.79, 0.4, 0.17, 0.04, "bdate"),
(0, 0.55, 0.6, 0.37, 0.13, "drink"),
(0, 0.55, 0.73, 0.45, 0.09, "godfather"),
(0, 0.55, 0.82, 0.45, 0.056, "from"),
(0, 0.55, 0.87, 0.45, 0.13, "fivewords"),
(0, 0.06, 0.065, 0.45, 0.045, "qi"),
(0, 0.06, 0.105, 0.45, 0.034, "hiddentalent"),
(0, 0.06, 0.138, 0.45, 0.029, "boobakaaris"),
(0, 0.06, 0.16, 0.34, 0.17, "dance"),
(0, 0.054, 0.433, 0.409, 0.317, "drawing"),
(1, 0.55, 0.1, 0.45, 0.12, "joke"),
(1, 0.55, 0.21, 0.45, 0.104, "gods"),
(1, 0.55, 0.31, 0.38, 0.16, "marchetti"),
(1, 0.55, 0.49, 0.45, 0.078, "kesako"),
(1, 0.55, 0.56, 0.33, 0.17, "e"),
(1, 0.55, 0.73, 0.45, 0.03, "closedbar"),
(1, 0.55, 0.76, 0.45, 0.058, "220"),
(1, 0.55, 0.81, 0.45, 0.058, "soviet"),
(1, 0.672, 0.87, 0.328, 0.13, "important"),
(1, 0.05, 0.11, 0.48, 0.056, "sport"),
(1, 0.05, 0.16, 0.48, 0.085, "assos"),
(1, 0.05, 0.24, 0.48, 0.075, "bde"),
(1, 0.05, 0.31, 0.32, 0.024, "wei"),
(1, 0.05, 0.39, 0.357, 0.062, "presentation"),
(1, 0.05, 0.45, 0.32, 0.057, "limousin"),
(1, 0.05, 0.5, 0.48, 0.062, "bar"),
(1, 0.05, 0.56, 0.48, 0.057, "quote"),
(1, 0.05, 0.61, 0.48, 0.076, "ball"),
(1, 0.05, 0.7, 0.48, 0.075, "h5"),
(1, 0.05, 0.77, 0.48, 0.032, "panda"),
(1, 0.05, 0.8, 0.48, 0.082, "acronyms"),
(1, 0.05, 0.88, 0.4, 0.08, "prince")]

if os.path.exists(temp_dir):
    rmtree(temp_dir)

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

def extract_part(file, lratio, tratio, wratio, hratio, output):
    im = Image.open(file)
    im_size = im.size
    left = im_size[0] * lratio
    top = im_size[1] * tratio
    width = im_size[0] * wratio
    height = im_size[1] * hratio
    box = (left, top, left+width, top+height)
    area = im.crop(box)
    area.save(os.path.dirname(os.path.abspath(file)) + '/' + output + ".jpg", "JPEG")

def crop_all():
    for file in os.listdir(form_dir):
        filename, file_extension = os.path.splitext(file)
        actual = filename.replace(' ', '-')
        pics = os.listdir(temp_dir + actual)
        for folder in os.listdir(temp_dir + actual):
            pages = os.listdir(temp_dir + actual + '/' + folder)
            for crop in cropping_data:
                extract_part(temp_dir + actual + '/' + folder + '/' + pages[crop[0]], crop[1], crop[2], crop[3], crop[4], crop[5])

extract_images()
separate_forms()
crop_all()


#for page in pages:
#    page.save('out.jpg', 'JPEG')
