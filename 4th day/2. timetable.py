import pandas as pd 
import matplotlib .pyplot as plt

df=pd.read_csv("marks_sum_.csv")

print(df)

plt.bar(df["name"], df ["total"])
plt.xlabel("name")
plt.ylabel("total")
plt.title("student mark graph")

plt.show()

plt.bar(df["name"], df ["average"])
plt.xlabel("name")
plt.ylabel("average")
plt.title("student mark graph")

plt.show()

labels=["a","b","c","d","e","f","g","h","i","j"]
sizes=[376,307,349,274,272,267,301,341,388,309]
plt.pie(sizes, labels=labels)

plt.show()

plt.scatter(df["name"], df ["total"])
plt.xlabel("students")
plt.ylabel("marks total")
plt.title("student mark graph")

plt.show()

