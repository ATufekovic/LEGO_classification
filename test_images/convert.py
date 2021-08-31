from PIL import Image
import os

root_path = "./test_images/G3 camera"

for folder in os.listdir(root_path):
    print(folder)
    for file in os.listdir(root_path + "/" + folder):
        im = Image.open(root_path + "/" + folder + "/" + file)
        im.save(root_path + "/" + folder + "/" + file.split(".")[0] + ".png")
        os.remove(root_path + "/" + folder + "/" + file)