import pandas as pd 
import matplotlib .pyplot as plt

df=pd.read_csv("marks.csv")
print(df)

plt.bar(df["name"], df ["marks"])
plt.xlabel("students")
plt.ylabel("marks")
plt.title("student mark graph")

plt.show()

labels=["alice","bob","charlie"]
sizes=[50,45,48]
plt.pie(sizes, labels=labels)

plt.show()


plt.scatter(df["name"], df ["marks"])
plt.xlabel("students")
plt.ylabel("marks")
plt.title("student mark graph")

plt.show()