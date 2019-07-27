#from PIL import Image
import os

images_path = []
files = os.listdir("Conveted images")
print(files)
for f in files:
        if f.endswith('.png'):
                print(f)
                images_path.append(f)

