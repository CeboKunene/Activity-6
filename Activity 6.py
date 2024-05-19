import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("C:/Users/Sfundesihle/Downloads/New folder/archive.zip")
print(data.head())

Missing_values = data.isnull().sum()
print(Missing_values)

Duplicates = data.duplicated().sum()
print("Number of duplicate entries:", Duplicates)


data['Science'].hist()
plt.show()

data.columns
data.dtypes
data.size
data.shape


plt.figure(figsize=(10, 5))
plt.plot((data['Science'].head(5)),(data['Law'].head(5)), marker='o', linestyle='-', color='red')
plt.title('science vs. law')
plt.xlabel('Science')
plt.ylabel('Law')
plt.grid(True)
plt.show()

plt.scatter((data['Science'].head(5)),(data['law'].head(5)))
plt.title('Science vs. law')
plt.xlabel('Science')
plt.ylabel('Law')
plt.show()


plt.hist((data['Science'].head(7)), bins=20, color='blue', alpha=0.7)
plt.title('Histogram of Science')
plt.xlabel('Science')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(8, 5))
plt.bar((data['Science'].head(7)),(data['Law'].head(7)) , color='blue', alpha=0.7)
plt.title('Science vs. law')
plt.xlabel('Science')
plt.ylabel('Law')
plt.show()

plt.figure(figsize=(7, 7))
plt.pie((data['Science'].head(7)), labels=(data['date'].head(7)), autopct='%1.1f%%', startangle=140)
plt.title('Pie chart of Science')
plt.show()

plt.figure(figsize=(6, 8))
plt.boxplot((data['Science'].head(9)), vert=True, patch_artist=True, meanline=True, showmeans=True)
plt.title('Box plot of Science')
plt.ylabel('Science')
plt.grid(True)
plt.show()