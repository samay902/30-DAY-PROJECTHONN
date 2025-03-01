import numpy as np
from PIL import Image
import matplotlib.pyplot as plt





def image_toarray(path):

    try:
        img = Image.open(path).convert("L")
        img = img.resize((28, 28))
        digit_array = np.array(img)
        if digit_array[0, 0] < 100:
            digit_array = 255 - digit_array
        return digit_array
    except FileNotFoundError:
        print("shit's fucked up")
    except Exception as e:
        print("something's fucked up:", e)

def make_my_image(img_data):
    plt.imshow(img_data, cmap="binary")
    plt.axis("off")  # Removes axes for better visualization
    plt.show(block="True")


paths = r"G:\my_digit.png"
data = image_toarray(paths)
if data is not None:  # Fix incorrect condition check
    make_my_image(data)
