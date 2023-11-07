import random
import subprocess

KEY = open("/tmp/downfallKey.txt","r").read()
print("Key: " + KEY)


lst = ['0','1','2','3', '4','5','6','7','8','9','a','b','c','d','e','f']
def getQword2():
    rtlist = []
    ind = random.randint(0,10)
    for j in range(10):
        ret = ''
        if ind == j:
            ret = KEY[16:].strip()
        else:
            for i in range(16):
                ret += str(lst[random.randint(0,1000000000)%16])
        rtlist.append(ret)
    return rtlist

def getQword1():
    rtlist = []
    ind = random.randint(0,10)
    for j in range(10):
        ret = ''
        if ind == j:
            ret = KEY[0:16].strip()
        else:
            for i in range(16):
                ret += str(lst[random.randint(0,1000000000)%16])
        rtlist.append(ret)
    return rtlist

if __name__ == "__main__":
    print("1st Qword ")
    for q in getQword1():
        print(q)
    print
    print("2nd Qword ")
    for q2 in getQword2():
        print(q2)
    encrypt = subprocess.Popen(['openssl', 'aes-128-cbc', '-salt', '-e', '-in', '/tmp/downfall.txt', '-out', '/tmp/downfall.txt.encrypted2', '-K', KEY,'-iv', '11111111111111111111111111111111'])
    val = open("/tmp/downfall.txt.encrypted2","r").read()
    val2 = open("/tmp/downfall.txt.encrypted","r").read()
    if val == val2:
        print("work")