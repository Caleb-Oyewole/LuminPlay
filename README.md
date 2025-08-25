Nigerian Learning Styles Data Engineering Project 🇳🇬
​This repository documents the end-to-end data engineering process applied to the raw nigerian_learning_styles_app_dataset.csv file. The goal of this project was to clean, transform, and structure the data into a usable format, resulting in the processed file, nigerian_learning_styles_app_dataset_processed.csv.
​Repository Contents
​nigerian_learning_styles_app_dataset.csv: The original, raw dataset.
​nigerian_learning_styles_app_dataset_processed.csv: The cleaned and transformed dataset, ready for analysis and machine learning.
​data_engineering_script.py: The Python script used to perform the data processing.
​Data Engineering Process ⚙️
​The following steps were performed to prepare the data:
​Data Ingestion: The raw CSV file was loaded into a data processing environment (e.g., a Pandas DataFrame in Python).
​Data Cleaning:
​Handling Missing Values: We checked for and addressed any missing data points.
​Removing Duplicates: Duplicate records were identified and removed to ensure data integrity.
​Data Type Conversion: Columns were converted to their correct data types (e.g., age from float to integer, if necessary).
​Data Transformation:
​Feature Engineering: New features were derived from existing columns. For example, a new column for user_id was created to uniquely identify each user based on their demographic information (age, grade_level, sex).
​Normalization: The data was normalized into a relational structure by creating separate tables (simulated in the processed CSV) for users and interactions to reduce redundancy.
​Categorical Encoding: Categorical variables like learning_style and preferred_instruction_type were handled appropriately for potential use in machine learning models.
​How to Use This Repository
​If you wish to replicate this process, you can use the data_engineering_script.py file to perform the same transformations on the raw dataset. The processed CSV can be directly used for data analysis, visualization, or training machine learning models.
​License
​This project is open-source and available under the MIT License.
