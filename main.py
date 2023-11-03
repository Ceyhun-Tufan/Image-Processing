from PIL import Image
import numpy as np

raw_image = Image.open("sample.jpg")
img = raw_image.copy()
arr = np.array(img)
print(arr[0])

with open("raw_array_image.txt", "w") as file:
    file.write(str(arr))
    

row_count = arr.shape[0]
col_count = arr.shape[1]
print(f"Image Resulation: {row_count} x {col_count}")

# arr[:][1000] = [255, 0, 0,255]

# actually its just useless

def makingblurry():
    tmp_nlist = []
    for y, row in enumerate(arr):
        for x, col in enumerate(row):
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for nx, ny in neighbors:
                if 0 <= nx < col_count and 0 <= ny < row_count:
                    tmp_nlist.append(arr[ny][nx])
            result = [sum(values) for values in zip(*tmp_nlist)]
            result = [i//4 for i in result]
            arr[y][x] = result
            tmp_nlist = []
    new_img = Image.fromarray(arr)
    new_img.save(f"blurry_final.jpg")

# makingblurry()


def Morphological(cell_size: int = 4):
    print("Process started")
    tmp_nlist = []
    final_array = []
    # dividing 4x4 cells
    for y, row in enumerate(arr):
        if y % 2 == 0:
            continue
        else:
            final_array.append([])
        for x, col in enumerate(row):
            if x % 2 == 0:
                continue
            neighbors = [(x + 1, y), (x, y - 1), (x + 1, y - 1), (x, y)]

            for nx, ny in neighbors:
                if 0 <= nx < col_count and 0 <= ny < row_count:
                    tmp_nlist.append(arr[ny][nx])

            final_array[-1].append([sum(values) for values in zip(*tmp_nlist)])
            final_array[-1][-1] = [i//4 for i in final_array[-1][-1]]
            tmp_nlist = []

    final_array = np.asarray(final_array)
    print(final_array)
    with open("final_array_image.txt", "w") as file:
        file.write(str(final_array))
    new_img = Image.fromarray(final_array.astype(np.uint8))
    new_img.save("morphological.jpg")
    print("Process is done.")


Morphological(cell_size=4)


# little note:  removing item from list -- filter(lambda item: item!='xx',lst) -- returns lasted list
