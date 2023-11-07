import random
#Ascii = Downfall
st = "0100010001101111011101110110111001100110011000010110110001101100"

for char in st:
    if char == '0':
        print(random.normalvariate(25,3))
    elif char == '1':
        print(random.normalvariate(45,3))

print("DownFall!")