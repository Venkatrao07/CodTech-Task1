# CodTech-Task1
# Simple Linear Regression on Housing Data

This project applies Simple Linear Regression to predict housing prices using a dataset. It includes exploratory data analysis (EDA), model training, evaluation, and visualization of results.

## Project Overview

This project involves:

- Loading and preprocessing the housing dataset.

- Performing exploratory data analysis (EDA).

- Splitting the data into training and testing sets.

- Training a Linear Regression model.

- Evaluating the model's performance using Root Mean Squared Error (RMSE).

- Visualizing the regression results.

## Requirements

- Python 3.x
- Pandas
- Seaborn
- Matplotlib
- Scikit-learn

You can install the required Python packages using pip:
 
pip install pandas seaborn matplotlib scikit-learn

Dataset
The dataset used in this project is housingData.csv, which should be located in the project directory. The dataset should contain various features related to housing and a target variable MEDV representing housing prices.

Code Description

Import Libraries: Necessary libraries for data manipulation, visualization, and modeling are imported.

Load Dataset: The dataset is loaded and missing values are imputed with the mean.

Exploratory Data Analysis (EDA): A heatmap of correlations between features is generated to understand the relationships in the dataset.

Split Data: The data is split into training and testing sets.

Train Model: A Linear Regression model is trained on the training data.

Evaluate Model: The model is evaluated using RMSE on the test data.

Visualize Results: A scatter plot of actual vs. predicted values is displayed along with a line representing the ideal prediction.
