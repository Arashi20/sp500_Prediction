# S&P 500 Market Prediction Project

## Overview

This project aimed to explore historical S&P 500 data and build machine learning models (An LSTM model and a LightGBM model) to identify patterns related to bull markets, bear markets, and crashes, with the goal of investigating potential predictability in market movements.

**Disclaimer:** *Predicting the stock market is inherently complex and high-risk. This project is intended for educational and research purposes only and does not constitute financial advice. Any models developed should not be used for actual trading without thorough validation and understanding of the associated risks.*


## Goals

*   Perform Exploratory Data Analysis (EDA) on historical S&P 500 data (1970-Present).
*   Identify and analyze characteristics of major bull markets, bear markets, and crashes.
*   Investigate relationships between price action, volume, and volatility.
*   Engineer relevant features for time series prediction.
*   Build and evaluate Machine Learning / Deep Learning models (e.g., LSTM, Transformer) for predicting future market behavior.

## Data

The primary dataset is `sp500.csv`, containing daily Open, High, Low, Close, and Volume data for the S&P 500 index (^GSPC), sourced historically (Yahoo Finance).

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```
2.  **Create and activate a virtual environment:** (Recommended)
    ```bash
    # Using venv (built-in)
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

*   **Data Exploration:** Run the `notebooks/Data_Exploration.ipynb` notebook.
*   **Model Training:** Run the `notebooks/Model_Training.ipynb` notebook.

## Future Steps

*   Potentially investigate different models.
*   Try out another feature set
