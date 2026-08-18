# CarValue AI

CarValue AI is a used car price prediction project built with Python and machine learning.

The idea is simple: enter some details about a used car and the model gives an estimated resale price.

I built the project starting from the dataset, then cleaned and explored the data, prepared the features, trained the model and connected it to a Streamlit application.

## What the project does

- Predicts the estimated price of a used car
- Takes car details such as make, model, variant, mileage and year
- Handles categorical car information
- Uses variant frequency encoding
- Uses a Random Forest regression model
- Provides a simple web interface using Streamlit

## Dataset

The dataset contains 8,095 used car records.

The original dataset has 15 columns:

- city
- make
- model
- variant
- mileage
- make_year
- price
- fuel_type
- no_of_owners
- color
- body_type
- transmission
- registration_year
- car_age
- make_model

There were no missing values or duplicate rows in the dataset.

I removed `make_model` during preprocessing because it was already derived from `make` and `model`.

## Model

I used Random Forest Regression for the price prediction.

The data was split into:

- Training data: 6,476 rows
- Test data: 1,619 rows

For categorical features, I used one-hot encoding.

The `variant` column had 1,293 different values, so I used frequency encoding instead of creating hundreds of one-hot columns.

The frequency values were calculated from the training data only.

## Results

The model was tested on the test dataset.

```text
MAE  : ₹44,527
RMSE : ₹88,271
R²   : 0.9582