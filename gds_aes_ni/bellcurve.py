import random
from matplotlib import pyplot as plt

#Provides one value for the distribution
def distribution():
    ranVal = random.randint(0,1)
    if ranVal == 0:
        return random.normalvariate(25,3)
    else:
        return random.normalvariate(45,3)

#provides all random values would need the student to graph and distinguish
def distributionAll():
    lst = []
    for i in range(10000):
        ranVal = random.randint(0,1)
        if ranVal == 0:
            lst.append(distribution())
        else:
            lst.append(distribution())
    return lst

    

if __name__ == "__main__":
    vals = distributionAll()
    val= open('vals.csv', 'w')
    count = 0
    for point in vals:
        count += 1
        val.write(str(point))
        val.write(',')
