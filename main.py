"""
For png:
[r,g,b,alpha*1]

for jpeg:
[r,g,b]

1: Alpha is basicly the opacity of the current pixel

arr[0][0][0] is the r value of one pixel
"""
from PIL import Image
import numpy as np

raw_image = Image.open("sample2.jpg")
img = raw_image.copy()

arr = np.array(img)
print(arr[0])
row_count = arr.shape[0]
col_count = arr.shape[1]

print(f"Image Resulation: {row_count} x {col_count}")

#arr[:][1000] = [255, 0, 0,255]

def makingblurry():
    tmp_nlist = []
    for y,row in enumerate(arr):
        for x,col in enumerate(row):
            neighbors = [(x - 1, y),(x + 1, y),(x, y - 1),(x, y + 1)]
            for nx,ny in neighbors:
                if 0 <= nx < col_count and 0 <= ny < row_count:
                    tmp_nlist.append(arr[ny][nx])
            result = [sum(values) for values in zip(*tmp_nlist)]
            result = [i//4 for i in result]
            arr[y][x] = result
            tmp_nlist = []
    new_img = Image.fromarray(arr)
    new_img.save(f"new_foo.jpg")

makingblurry()


def scaling():
    pass


"""

sample.jpg:
[[ 98  26   2]
 [ 98  26   2]
 [ 99  27   3]
 ...
 [235 111  15]
 [235 111  15]
 [234 110  14]]


 sample2.jpg:

 [35 35  9  9  9  9  1  1  1  1  1  1  1  1  1  1  0  1  1  0  0  0  1  0
  0  0  0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  1  1  1  1  1  1  1  1
  1  1  1  1  1  1  1  1  0  1  1  1  1  1  1  1]



"""