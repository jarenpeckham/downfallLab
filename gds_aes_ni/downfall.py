import getQwords2
import bellcurve
from subprocess import call

#provides all random values would need the student to graph and distinguish
def distributionAll():
    lst = []
    for i in range(10000):
        lst.append(bellcurve.distribution())
        
    return lst

if __name__ == "__main__":
    vals = distributionAll()
    val= open('vals.csv', 'w')
    count = 0
    for point in vals:
        count += 1
        val.write(str(point))
        val.write(',')


    print("1st Qword ")
    print
    qwor1 = getQwords2.getQword1()
    for q in qwor1:
        print(q)
    print
    print("2nd Qword ")
    print
    qwor2 = getQwords2.getQword2()
    for q2 in qwor2:
        print(q2)
    
    finalLst = []
    bool = False
    print
    print("Combining Qwords and searching for a match")
    print
    for i in qwor1:
        for j in qwor2:
            z = str(i+j)
            finalLst.append(i+j)
            encrypt = call(['openssl', 'aes-128-cbc', '-salt', '-e', '-in', '/tmp/downfall.txt', '-out', '/tmp/downfall.txt.encrypted2', '-K', z,'-iv', '11111111111111111111111111111111'])
            val = open("/tmp/downfall.txt.encrypted2","r",encoding='latin-1').read()
            val2 = open("/tmp/downfall.txt.encrypted","r",encoding='latin-1').read()
            print(z)
            if val == val2:
                bool = True
                print("Encryption Matches!")
                print("Stolen Key: " + z)
                break
        if bool:
            break
            
    

    
