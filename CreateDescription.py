import os

def create_description():
    for img in os.listdir("NegativeImgs"):
        line="NegativeImgs/"+img+"\n"
        with open("bg.txt", "a") as f:
            f.write(line)
create_description()
