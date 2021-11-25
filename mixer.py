import os
import time
from PIL import Image

imagePath = "./jigsaw"
outputPath = "./output"

categories = []
files = []

mix_tmp = []
combines = []


def scan_folders():
    for category in os.listdir(imagePath):
        categories.append(category)

    print(categories)


def count_permutations():
    if len(categories) == 0:
        scan_folders()


def produce_files():
    if len(categories) == 0:
        print("Empty Content")
        return

    for category in categories:
        cat_files = os.listdir(os.path.join(imagePath, category))
        files.append(cat_files)


tmp = []
result = []
count = 0


def initialize_tmp():
    tmp.clear()
    for _tmp in categories:
        tmp.append('')


def arrange(arr: list, layer: int):
    global count

    pictures = arr[layer]
    for picture in pictures:
        tmp[layer] = os.path.join(imagePath, categories[layer], picture)
        if layer < len(arr) - 1:
            arrange(arr, layer + 1)
        else:
            result.append(tmp)
            count += 1

def mix_files(arr: list, *args):
    arr = arr.copy()
    if len(args) > 0:
        if len(arr) > 1:
            new_image = Image.alpha_composite(args[0], Image.open(arr[0]))
            arr.pop(0)
            mix_files(arr, new_image)
            return
        if len(arr) == 1:
            print(arr)
            new_image = Image.alpha_composite(args[0], Image.open(arr[0]))
            new_image.save(os.path.join(outputPath, "mix_" + str(time.time()) + ".png"))
            arr.pop(0)
            # new_image.show()
            return
    new_image = Image.alpha_composite(Image.open(arr[0]), Image.open(arr[1]))
    arr.pop(0)
    arr.pop(0)
    mix_files(arr, new_image)
    return


scan_folders()
produce_files()
initialize_tmp()
arrange(files, 0)

for item in result:
    mix_files(item)

print('done')
