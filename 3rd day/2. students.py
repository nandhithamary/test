import numpy as np
import matplotlib.pyplot as plt
students=["arun", "alna", "chethan", "divya", "elna"]
marks=[75,85,90,70,95]

plt.plot(students, marks)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("simple line plot")

plt.grid()
plt.show()

