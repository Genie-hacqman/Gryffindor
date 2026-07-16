
# hd = open('./mock.csv')
# for line in hd.readlines()[:5]:
#     print(line)
# hd.close()





# for i in range(1, 51):
#     line = hd.readline()
#     print(line)
# hd.close()  




from PIL import Image,ImageChops

img1 = Image.open('./hack.jpeg')
img2 = Image.open('./hack2.jpeg')

diff = ImageChops.difference(img1, img2)
diff.show()





























