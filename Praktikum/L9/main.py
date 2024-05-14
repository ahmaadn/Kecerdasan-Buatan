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
numerical_columns = df.select_dtypes(include=["object"]).columns

# Plot distribution of each numerical feature
plt.figure(figsize=(14, len(numerical_columns) * 3))
for idx, feature in enumerate(numerical_columns, 1):
	plt.subplot(len(numerical_columns), 2, idx)
	sns.histplot(df[feature], kde=True)
	plt.title(f"{feature} | Skewness: {feature}")

# Adjust layout and show plots
plt.tight_layout()
plt.show()

# Assuming 'df' is your DataFrame
plt.figure(figsize=(10, 5))

# Using Seaborn to create a swarm plot
sns.swarmplot(x="buying", y="persons", data=df, palette='viridis')

plt.title('person Plot for buying')
plt.xlabel('buying')
plt.ylabel('persons')
plt.show()


# Set the color palette
sns.set_palette("Pastel1")

# Assuming 'df' is your DataFrame
plt.figure(figsize=(15, 10))

# Using Seaborn to create a pair plot with the specified color palette
sns.pairplot(df, x_vars="buying", y_vars="maint")

plt.suptitle('Pair Plot for DataFrame')
plt.show()


# Assuming 'df' is your DataFrame
plt.figure(figsize=(10, 5))

# Using Seaborn to create a violin plot
sns.violinplot(x="buying", y="persons", data=df, palette={
			'vhigh': 'lightcoral', 'low': 'lightblue', 'med': 'lightgreen','high': 'red', }, alpha=0.7)

plt.title('Violin Plot for Species and Sepal Length')
plt.xlabel('buying')
plt.ylabel('persons')
plt.show()


#plotting box plot between alcohol and quality
sns.boxplot(x='buying', y='persons', data=df)

from sklearn.preprocessing import LabelEncoder

# Membuat instance dari LabelEncoder
df['doors'] = df['doors'].replace('5more', 5)
df['persons'] = df['persons'].replace('5more', 5)
df['doors'] = pd.to_numeric(df['doors'], errors='coerce')
df['persons'] = pd.to_numeric(df['persons'], errors='coerce')

# Mengisi nilai NaN dengan nilai median atau modus sesuai kebutuhan
df['persons'].fillna(df['persons'].median(), inplace=True)

# Membuat instance dari LabelEncoder dan melakukan encoding pada semua kolom kategorikal
label_encoder = LabelEncoder()
df['buying'] = label_encoder.fit_transform(df['buying'])
df['maint'] = label_encoder.fit_transform(df['maint'])
df['lug_boot'] = label_encoder.fit_transform(df['lug_boot'])
df['safety'] = label_encoder.fit_transform(df['safety'])
df['class'] = label_encoder.fit_transform(df['class'])  # Encoding kolom 'class'

print(df)
print(df)

# Membuat heatmap korelasi
plt.figure(figsize=(15, 10))
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm', linewidths=2)
plt.title('Correlation Heatmap')
plt.show()