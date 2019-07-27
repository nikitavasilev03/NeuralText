from PIL import Image

images_code_file = open("mnist_100.csv", "r")
images_code = images_code_file.readlines()
images_code_file.close()

i = 0
for record in images_code:
    im = Image.new("RGB", (28, 28))
    px = im.load()
    image_code = record.split(',')
    image_code = image_code[1:]
    for x in range(28):
        for y in range(28):
            px[y, x] = (255 - int(image_code[x * 28 + y]), 255 - int(image_code[x * 28 + y]), 255 - int(image_code[x * 28 + y]))
            pass
        pass
    i += 1
    im.save("Conveted images\\" + str(i)+ "-" + str(record[0]) + ".png", "PNG")