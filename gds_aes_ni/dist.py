import bellcurve
import matplotlib.pyplot as plt

#provides all random values would need the student to graph and distinguish
lst = []
for i in range(10000):
    lst.append(bellcurve.distribution())
    
plt.hist(lst)
plt.show()

