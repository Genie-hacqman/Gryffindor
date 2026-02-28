# with open("files/MOCK_DATA.csv", "r", encoding="utf-8") as file:
#    content = file.readlines()

# for txt in content[:51]:
#    pass
   


from PIL import Image, ImageChops

img1 = Image.open("./files/a.JPG")
climg2 = Image.open("./files/b.JPG")

difference = ImageChops.difference(img1,climg2)

difference.show()

