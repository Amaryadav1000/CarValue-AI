import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st


# --------------------------------------------------
# Project paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "Models")
DATA_PATH = os.path.join(BASE_DIR, "Data", "car_data.csv")


# --------------------------------------------------
# Load project files
# --------------------------------------------------

model = joblib.load(
    os.path.join(MODEL_DIR, "car_price_model.pkl")
)

encoder = joblib.load(
    os.path.join(MODEL_DIR, "encoder.pkl")
)

variant_freq = joblib.load(
    os.path.join(MODEL_DIR, "variant_freq.pkl")
)

df = pd.read_csv(DATA_PATH)


categorical_cols = [
    "city",
    "make",
    "model",
    "fuel_type",
    "color",
    "body_type",
    "transmission"
]

numerical_cols = [
    "mileage",
    "make_year",
    "no_of_owners",
    "registration_year",
    "car_age",
    "variant"
]


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="CarValue AI",
    page_icon="🚗",
    layout="wide"
)


# --------------------------------------------------
# Custom styling
# --------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at top right,
                rgba(37, 99, 235, 0.12),
                transparent 35%
            ),
            #0b1120;
    }

    .main-title {
        font-size: 46px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 4px;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .price-card {
        padding: 28px;
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            rgba(30, 41, 59, 0.95),
            rgba(15, 23, 42, 0.95)
        );
        border: 1px solid rgba(148, 163, 184, 0.18);
        text-align: center;
        margin-top: 20px;
    }

    .price-label {
        color: #94a3b8;
        font-size: 15px;
        margin-bottom: 8px;
    }

    .price-value {
        font-size: 42px;
        font-weight: 800;
        color: #38bdf8;
    }

    .metric-card {
        padding: 18px;
        border-radius: 14px;
        background: rgba(30, 41, 59, 0.65);
        border: 1px solid rgba(148, 163, 184, 0.12);
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 48px;
        font-weight: 700;
        font-size: 16px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🚗 CarValue AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Used-car price estimation based on vehicle specifications and market patterns.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("Model Information")

    st.write(
        "CarValue AI estimates the expected price of a used car "
        "using a Random Forest regression model."
    )

    st.divider()

    st.metric(
        "Test R² Score",
        "95.82%"
    )

    st.metric(
        "Mean Absolute Error",
        "₹44,527"
    )

    st.divider()

    st.caption(
        "The displayed metrics are from the project's held-out test set."
    )


# --------------------------------------------------
# Input sections
# --------------------------------------------------

st.subheader("Vehicle Details")

col1, col2, col3 = st.columns(3)


with col1:

    city = st.selectbox(
        "City",
        sorted(df["city"].dropna().unique())
    )

    make = st.selectbox(
        "Manufacturer",
        sorted(df["make"].dropna().unique())
    )

    model_name = st.selectbox(
        "Model",
        sorted(df["model"].dropna().unique())
    )

    variant = st.selectbox(
        "Variant",
        sorted(df["variant"].dropna().unique())
    )


with col2:

    fuel_type = st.selectbox(
        "Fuel Type",
        sorted(df["fuel_type"].dropna().unique())
    )

    transmission = st.selectbox(
        "Transmission",
        sorted(df["transmission"].dropna().unique())
    )

    body_type = st.selectbox(
        "Body Type",
        sorted(df["body_type"].dropna().unique())
    )

    color = st.selectbox(
        "Color",
        sorted(df["color"].dropna().unique())
    )


with col3:

    mileage = st.number_input(
        "Mileage (km)",
        min_value=1,
        max_value=500000,
        value=40000,
        step=1000
    )

    make_year = st.number_input(
        "Manufacturing Year",
        min_value=int(df["make_year"].min()),
        max_value=int(df["make_year"].max()),
        value=2020,
        step=1
    )

    registration_year = st.number_input(
        "Registration Year",
        min_value=int(df["registration_year"].min()),
        max_value=int(df["registration_year"].max()),
        value=2020,
        step=1
    )

    no_of_owners = st.number_input(
        "Number of Owners",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )


car_age = st.number_input(
    "Car Age (years)",
    min_value=0,
    max_value=50,
    value=5,
    step=1
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.divider()

predict_button = st.button(
    "Estimate Car Price"
)


if predict_button:

    car = pd.DataFrame([{
        "city": city,
        "make": make,
        "model": model_name,
        "variant": variant,
        "mileage": mileage,
        "make_year": make_year,
        "no_of_owners": no_of_owners,
        "color": color,
        "body_type": body_type,
        "transmission": transmission,
        "registration_year": registration_year,
        "car_age": car_age,
        "fuel_type": fuel_type
    }])

    car["variant"] = (
        car["variant"]
        .map(variant_freq)
        .fillna(0)
    )

    numeric_data = car[numerical_cols].to_numpy()

    categorical_data = encoder.transform(
        car[categorical_cols]
    )

    final_features = np.hstack([
        numeric_data,
        categorical_data
    ])

    predicted_price = model.predict(
        final_features
    )[0]

    st.markdown(
        f"""
        <div class="price-card">
            <div class="price-label">
                Estimated Market Price
            </div>
            <div class="price-value">
                ₹{predicted_price:,.0f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(
        "Estimate generated successfully."
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "CarValue AI • Machine Learning Portfolio Project"
)