#creating a parity function to determine if a number is even or odd

def parity(num):
    if num% 2 == 0:
        return "even"
    else:
        return "odd"
    
num = int(input("Enter a number: "))
print(parity(num))    


#Using try and except function to pass an error.

def parity(num):

    if num% 2 == 0:
        return "even"
    else:
        return "odd"
while True:    
    try:
        user_input = int(input("Enter num: "))
        print(parity(user_input))
        break
    
    except(ValueError,TypeError):
        print("Invalid input") 
     


#Take a short video and divide it into its various picture frames

import cv2

video_path="C:\\Users\\user\\Desktop\\Gryffindor\\Sandra\\Vid.mp4"
output_folder="C:\\Users\\user\\Desktop\\Gryffindor\\Sandra\\Frames/"
cap=cv2.VideoCapture(video_path)
count=0

while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imwrite(f"{output_folder}frame_{count}.jpeg",frame)
    count+=1 

cap.release()


#Create a gif from a normal picture using pillow

from PIL import Image 
Img=Image.open("C:\\Users\\user\\Desktop\\Gryffindor\\Sandra\\GIFF.jpeg")

frames=[]

for i in range(5):
    size=(Img.width-i*10,Img.height-i*10)
    frame=Img.resize(size)
    frames.append(frame)

frames[0].save(
    "outpüt.gif",
    save_all=True,
    append_images=frames[1:],
    duration=500,
    loop=0
)

