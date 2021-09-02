import os

imagePath = "./jigsaw"

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
        # print(tmp)
        tmp[layer] = os.path.join(imagePath, categories[layer], picture)
        if layer < len(arr) - 1:
            arrange(arr, layer + 1)
        else:
            print(tmp)
            result.append(tmp)
            count += 1


scan_folders()
produce_files()
initialize_tmp()
arrange(files, 0)

print(tmp)
print(count)

# print(files)
