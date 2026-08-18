# CarValue AI

CarValue AI is a machine learning project that estimates the resale price of used cars based on vehicle specifications and historical used-car listing data.

The project covers the complete workflow from data preparation and exploratory analysis to feature engineering, model training, evaluation, and a Streamlit-based prediction interface.

## Project Overview

The application takes details about a used car and predicts its estimated resale price.

The project includes:

- Used car price prediction
- Make and model based prediction
- Mileage and vehicle-age analysis
- Fuel type and transmission information
- Body type and color features
- Variant frequency encoding
- Random Forest regression
- Model evaluation using MAE, RMSE and R²
- Streamlit prediction interface

## Dataset

The dataset contains **8,095 used-car records** with **15 original columns**.

The original features are:

- `city`
- `make`
- `model`
- `variant`
- `mileage`
- `make_year`
- `price`
- `fuel_type`
- `no_of_owners`
- `color`
- `body_type`
- `transmission`
- `registration_year`
- `car_age`
- `make_model`

The dataset contained **no missing values and no duplicate rows**.

The derived `make_model` feature was removed during preprocessing because it was already based on the `make` and `model` columns.

## Data Preparation

The dataset was checked for:

- Missing values
- Duplicate records
- Invalid mileage values
- Invalid manufacturing years
- Invalid registration years
- Invalid car ages
- Invalid prices

The data passed these quality checks without requiring removal of invalid records.

## Feature Engineering

Categorical and numerical features were prepared before model training.

Most categorical features were handled using **one-hot encoding**.

The `variant` column contained **1,293 unique variants**. Since one-hot encoding such a high-cardinality feature would create a very large number of columns, frequency encoding was used instead.

The variant frequencies were calculated using the training data to avoid information leakage.

## Model Training

The target variable is:

```text
price