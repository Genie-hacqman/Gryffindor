from PIL import Image

# open images
img1 = Image.open("./img.jpeg")
img2 = Image.open("./img2.jpeg")

# save as Gif
img1.save(
    "animation.gif",
    save_all=True,
    append_images=[img2],
    duration=500,
    loop=0,

)
print("Gif created successfully!")