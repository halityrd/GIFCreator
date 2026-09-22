from PIL import Image
import imageio.v3 as iio

img = Image.open("sprite-sheet.jpg")

print(img.size)

cols = 4
rows = 2
cell_width = img.size[0] // cols
cell_height = img.size[1] // rows

print(cell_width, cell_height)

frames = []
for rows in range(rows):
    for column in range(cols):
        left = column * cell_width
        top = rows * cell_height
        crop_img = img.crop((left, top, left + cell_width, top + cell_height))

        frames.append(crop_img)

frames[0].save(
    "new-gif.gif",
    save_all=True,
    append_images=frames[1:],
    duration=500,
    loop=0,
)

# iio.imwrite("new-gif.gif", frames, duration=500, loop=0)
