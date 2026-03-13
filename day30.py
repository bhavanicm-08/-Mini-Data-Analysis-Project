import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Akshmith", "Roopesh", "Pranvi", "Karan", "Suraksha"],
    "Python": [90, 82, 89, 76, 91],
    "Machine Learning": [85, 78, 92, 74, 88],
    "Java": [80, 76, 95, 70, 84]
}

df = pd.DataFrame(data)

print("Dataset:\n")
print(df)
print("\nSummary Statistics:\n")
print(df.describe())
df.set_index("Name").plot(kind="bar")

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

avg_marks = df[["Python","Machine Learning","Java"]].mean()
avg_marks.plot(kind="pie", autopct='%1.1f%%')
plt.title("Average Marks Distribution by Subject")
plt.ylabel("")
plt.show()
