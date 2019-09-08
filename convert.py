import os
from shutil import rmtree
import pdf2image
from PIL import Image

form_dir = 'formulaires/'
temp_dir = 'temp/'
dpi = 250

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

# 1 and 2
def extract_name(file):
    extract_part(file, 0.55, 0, 0.35, 0.07, "name")

# 1
def extract_gender(file):
    extract_part(file, 0.55, 0.4, 0.2, 0.04, "gender")

# 1
def extract_bdate(file):
    extract_part(file, 0.79, 0.4, 0.17, 0.04, "bdate")

# 1
def extract_drink(file):
    extract_part(file, 0.55, 0.6, 0.37, 0.13, "drink")

# 1
def extract_godfather(file):
    extract_part(file, 0.55, 0.73, 0.45, 0.09, "godfather")

# 1
def extract_from(file):
    extract_part(file, 0.55, 0.82, 0.45, 0.056, "from")

# 1
def extract_fivewords(file):
    extract_part(file, 0.55, 0.87, 0.45, 0.13, "fivewords")

#1
def extract_qi(file):
    extract_part(file, 0.06, 0.065, 0.45, 0.045, "qi")

# 1
def extract_hiddentalent(file):
    extract_part(file, 0.06, 0.105, 0.45, 0.034, "hiddentalent")

# 1
def extract_boobakaaris(file):
    extract_part(file, 0.06, 0.138, 0.45, 0.029, "boobakaaris")

# 1
def extract_dance(file):
    extract_part(file, 0.06, 0.16, 0.34, 0.17, "dance")

#1
def extract_drawing(file):
    extract_part(file, 0.054, 0.433, 0.409, 0.317, "drawing")

# 2
def extract_joke(file):
    extract_part(file, 0.55, 0.1, 0.45, 0.12, "joke")

# 2
def extract_gods(file):
    extract_part(file, 0.55, 0.21, 0.45, 0.104, "gods")

# 2
def extract_marchetti(file):
    extract_part(file, 0.55, 0.31, 0.38, 0.16, "marchetti")

# 2
def extract_kesako(file):
    extract_part(file, 0.55, 0.49, 0.45, 0.078, "kesako")

# 2
def extract_e(file):
    extract_part(file, 0.55, 0.56, 0.33, 0.17, "e")

# 2
def extract_closedbar(file):
    extract_part(file, 0.55, 0.73, 0.45, 0.03, "closedbar")

# 2
def extract_220(file):
    extract_part(file, 0.55, 0.76, 0.45, 0.058, "220")

# 2
def extract_soviet(file):
    extract_part(file, 0.55, 0.81, 0.45, 0.058, "soviet")

# 2
def extract_important(file):
    extract_part(file, 0.672, 0.87, 0.328, 0.13, "important")

# 2
def extract_sport(file):
    extract_part(file, 0.05, 0.11, 0.48, 0.056, "sport")

# 2
def extract_assos(file):
    extract_part(file, 0.05, 0.16, 0.48, 0.085, "assos")

#2
def extract_bde(file):
    extract_part(file, 0.05, 0.24, 0.48, 0.075, "bde")

#2
def extract_wei(file):
    extract_part(file, 0.05, 0.31, 0.32, 0.024, "wei")

#2
def extract_presentation(file):
    extract_part(file, 0.05, 0.39, 0.357, 0.062, "presentation")

#2
def extract_limousin(file):
    extract_part(file, 0.05, 0.45, 0.32, 0.057, "limousin")

#2
def extract_bar(file):
    extract_part(file, 0.05, 0.5, 0.48, 0.062, "bar")

#2
def extract_quote(file):
    extract_part(file, 0.05, 0.56, 0.48, 0.057, "quote")

#2
def extract_ball(file):
    extract_part(file, 0.05, 0.61, 0.48, 0.076, "ball")

#2
def extract_h5(file):
    extract_part(file, 0.05, 0.7, 0.48, 0.075, "h5")

#2
def extract_panda(file):
    extract_part(file, 0.05, 0.77, 0.48, 0.032, "panda")

#2
def extract_acronyms(file):
    extract_part(file, 0.05, 0.8, 0.48, 0.082, "acronyms")

#2
def extract_prince(file):
    extract_part(file, 0.05, 0.88, 0.4, 0.08, "prince")

def crop_all():
    for file in os.listdir(form_dir):
        filename, file_extension = os.path.splitext(file)
        actual = filename.replace(' ', '-')
        pics = os.listdir(temp_dir + actual)
        for folder in os.listdir(temp_dir + actual):
            extract_name(temp_dir + actual + '/' + folder + '/' + os.listdir(temp_dir + actual + '/' + folder)[0])

extract_images()
separate_forms()
crop_all()


#for page in pages:
#    page.save('out.jpg', 'JPEG')
