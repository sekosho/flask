import sys
import os

file = r"C:\Users\ssksh\Desktop\sekosho\hanyamizu\amazon\shipping_main.py"
file_name = "text.txt"
print(__file__)
print(os.path.dirname(__file__))
dirpath = os.path.dirname(__file__)
picture_path = os.path.join(dirpath, "static/user_image/{}".format(file_name))
# picture_path = "flaskr\static\user_image\"+file_name
open(picture_path, "wb").write(file)
