import imageio as iio

img = iio.v2.imread("photo.jpg")

print(type(img))
print(img.dtype)
print(img.shape)

iio.imwrite("photo#.png", img)