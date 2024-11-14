# Importing Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Drug_Consumption.csv')

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Summary statistics
print("\nSummary statistics of the dataset:")
print(data.describe())

# Distribution of Age
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Distribution of Personality Scores
plt.figure(figsize=(10, 6))
sns.kdeplot(data['Nscore'], color='blue', label='Nscore', shade=True)
sns.kdeplot(data['Escore'], color='green', label='Escore', shade=True)
sns.kdeplot(data['Impulsive'], color='red', label='Impulsive', shade=True)
plt.title('Distribution of Personality Scores')
plt.xlabel('Score')
plt.ylabel('Density')
plt.legend()
plt.show()

# Count plot for categorical data (Gender)
plt.figure(figsize=(8, 5))
sns.countplot(x='Gender', data=data, palette='viridis')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Box plot for Age by Nicotine addiction status
plt.figure(figsize=(10, 6))
sns.boxplot(x='Nicotine', y='Age', data=data, palette='Set2')
plt.title('Age Distribution by Nicotine Addiction Status')
plt.xlabel('Nicotine Addiction Status')
plt.ylabel('Age')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
correlation = data[['Age', 'Nscore', 'Escore', 'Impulsive']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Attributes')
plt.show()

# Pairplot for numerical features
sns.pairplot(data[['Age', 'Nscore', 'Escore', 'Impulsive', 'Nicotine']], hue='Nicotine', palette='coolwarm')
plt.suptitle('Pairplot of Key Features by Nicotine Addiction Status', y=1.02)
plt.show()

# Outlier detection using boxplots
plt.figure(figsize=(12, 6))
sns.boxplot(data=data[['Nscore', 'Escore', 'Impulsive']], palette='Pastel1')
plt.title('Boxplot of Personality Scores for Outlier Detection')
plt.xlabel('Attributes')
plt.ylabel('Score')
plt.show()