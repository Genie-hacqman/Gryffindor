from time import sleep

def traffic_light():
    for i in range(3):
        print("***************************")
        print("Red")
        print("***************************")
        sleep(5)
        print("***************************")
        print("Yellow")
        print("***************************")
        sleep(1)
        print("***************************")
        print("Green")
        print("***************************")
        print("Go!")
        print("***************************")





if __name__ == "__main__":
    traffic_light()