# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')

df = pd.read_csv("C:/Users/yogaa/OneDrive/Dokumen/SMT 4/Kecerdasan-Buatan/Praktikum/L9/car.csv")
print('\n\nprint(df.head())')
print(df.head())
print('\n\nprint(df.shape)')
print(df.shape)
print('\n\ndf.info()')
df.info()
print('\n\nprint(df.describe())')
print(df.describe())
print('\n\nprint(df.describe())')
print(df.columns.tolist())
print('\n\ndf.isnull().sum()')
print(df.isnull().sum())
print('\n\ndf.nunique()')
print(df.nunique())




# Assuming 'df' is your DataFrame
class_counts = df['buying'].value_counts()

# Using Matplotlib to create a count plot
plt.figure(figsize=(8, 6))
plt.bar(class_counts.index, class_counts, color='red')
plt.title('Count Plot of Class/ Label Dataset')
plt.xlabel('Class/ Label')
plt.ylabel('Count')
plt.show()



# Set Seaborn style
sns.set_style("darkgrid") 

# Identify numerical columns
numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

# Plot distribution of each numerical feature
plt.figure(figsize=(14, len(numerical_columns) * 3))
for idx, feature in enumerate(numerical_columns, 1):
	plt.subplot(len(numerical_columns), 2, idx)
	sns.histplot(df[feature], kde=True)
	plt.title(f"{feature} | Skewness: {round(df[feature].skew(), 2)}")

# Adjust layout and show plots
plt.tight_layout()
plt.show()


# Assuming 'df' is your DataFrame
plt.figure(figsize=(10, 8))

# Using Seaborn to create a swarm plot
sns.swarmplot(x="buying", y="persons", data=df, palette='viridis')

plt.title('Swarm Plot for Species and Sepal Length')
plt.xlabel('buying')
plt.ylabel('persons')
plt.show()


# Set the color palette
sns.set_palette("Pastel1")

# Assuming 'df' is your DataFrame
plt.figure(figsize=(10, 6))

# Using Seaborn to create a pair plot with the specified color palette
sns.pairplot(df)

plt.suptitle('Pair Plot for DataFrame')
plt.show()
