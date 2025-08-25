import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Initial Data Profiling and Loading ---
print("--- Starting Data Processing Pipeline ---")
file_name = 'nigerian_learning_styles_app_dataset.csv'
try:
    df = pd.read_csv(file_name)
    print("DataFrame loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    exit()

print("\n--- Initial DataFrame Info ---")
df.info()

# --- 2. Data Exploration and Visualization ---
print("\n--- Generating Visualizations ---")

# Create a histogram for the 'age' column
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='age', bins=9, kde=True, color='skyblue')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.75)
plt.savefig('age_distribution.png')
plt.close()

# Create a bar chart for the 'learning_style' column
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='learning_style', order=df['learning_style'].value_counts().index, palette='viridis')
plt.title('Frequency of Learning Styles')
plt.xlabel('Learning Style')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.75)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('learning_style_counts.png')
plt.close()

# Create a correlation matrix heatmap for numerical features
numerical_df = df.select_dtypes(include=['int64', 'float64'])
correlation_matrix = numerical_df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Numerical Features')
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.close()

# --- 3. Data Transformation (One-Hot Encoding) ---
print("\n--- Performing Data Transformation ---")

# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Perform one-hot encoding
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

print("\n--- Final Encoded DataFrame ---")
print(df_encoded.head())

# --- 4. Optional: Save the cleaned and prepared data ---
# You can uncomment the line below to save the processed data to a new CSV file
df_encoded.to_csv('nigerian_learning_styles_app_dataset_processed.csv', index=False)

print("\n--- Data Processing Pipeline Complete ---")