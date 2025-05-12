**Oraimo Sales Forecasting Project**

![ORAIMO 2](https://github.com/user-attachments/assets/ef6f566b-4fe8-45ef-8126-ec87202d70c0)



## Project Overview

**Forecasting Monthly Sales for October 2024 Based on Historical Sales Data**

This repository contains the code, data, and documentation for building time series models to forecast sales revenue for Oraimo—Africa’s leading smart accessories brand—for the month of October 2024. The project aims to improve demand planning, minimize stockouts and overstocking, and support strategic decision-making in inventory and marketing.


## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/oraimo-sales-forecasting.git
   cd oraimo-sales-forecasting
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   The key libraries include:

   * pandas, numpy, matplotlib, seaborn
   * statsmodels, prophet, scikit-learn
   * xgboost, lightgbm, tensorflow, keras
   * streamlit (for optional dashboard)

## Data Description

The dataset contains historical sales records from January to September 2024, with the goal to forecast October 2024.

| Column         | Description                                               |
| -------------- | --------------------------------------------------------- |
| `date`         | Sale date (YYYY-MM-DD)                                    |
| `city`         | City or region of sale                                    |
| `shop_name`    | Retail outlet where sale occurred                         |
| `model`        | Product model identifier                                  |
| `product_type` | Category of product (e.g., CABLE, CHARGER KIT, EARPHONES) |
| `quantity`     | Units sold                                                |
| `sales_price`  | Price per unit (KSH)                                      |
| `amount`       | Total revenue = `quantity` × `sales_price`                |
| `source`       | Sales channel                                             |

## Preprocessing & Cleaning

1. **Missing & Duplicate Removal**: Dropped rows with nulls (\~32 rows) and duplicates (\~299 rows).
2. **Standardization**: Converted `month` and `product_type` to uppercase.
3. **Column Selection**: Removed irrelevant fields (`city_2`, `year`, `source`, `shop_name`, `model`, etc.).
4. **Outlier Handling**: Retained true bulk-purchase outliers to preserve real purchasing behavior.
5. **City & Product Cleanup**: Merged variations and fixed misspellings via mapping dictionaries.
6. **Datetime Indexing**: Parsed `date` to datetime and set as index for time series operations.

## Exploratory Data Analysis (EDA)

* **Univariate Analysis**: Distributions of `quantity`, `sales_price`, and `amount`.
* **Trend Plots**: Monthly and weekly averages; daily totals with 7-day rolling mean.
* **Seasonality & Cyclicality**: Heatmaps by month vs. day of week; no strong annual seasonality due to short span.
* **Top Products & Categories**: Bar charts of best/worst-selling items; pie chart of category breakdown.
* **Holiday Effects**: Annotated known holidays to detect spikes or dips.

## Feature Engineering

* **Time-Based**: Day, month, weekday, ISO week, weekend flag.
* **Lag Features**: 1-day, 7-day, and 14-day lags of daily sales.
* **Rolling Statistics**: 7-day moving average and standard deviation.
* **Holiday Flag**: Marked key dates (e.g., public holidays, Black Friday).

## Modeling

1. **Baseline**: Simple moving average; naive persistence.
2. **Classical TS**: ARIMA, SARIMA, Holt–Winters.
3. **Machine Learning**: Random Forest, XGBoost, LightGBM using engineered features.
4. **Advanced**: Prophet for trend/seasonality decomposition.
5. **Deep Learning (Optional)**: LSTM networks for sequential modeling.

Each model is trained with backtesting: train on Jan–Aug, validate on Sep, and forecast Oct.
![image](https://github.com/user-attachments/assets/7a2c7018-6e1f-428a-a172-ab04e7975a25)

## Forecasting
![image](https://github.com/user-attachments/assets/62df8bdf-0e36-4496-9fe4-0a057c72bc35)


## Evaluation

Key metrics used:

* **MAE** (Mean Absolute Error)
* **RMSE** (Root Mean Squared Error)


![image](https://github.com/user-attachments/assets/3c158a1c-55c2-42ce-aa31-d1dfee72b2b9)


## Results & Insights

* **Stationarity**: Daily sales series is stationary (ADF p-value ≈ 0), allowing direct ARIMA modeling.
* **Best Model**: \[XGboost Model].
* **Business Findings**:

  * Spikes in Feb & May; decline toward October.
  * Higher sales on weekends, especially Saturdays.
  * Nairobi dominates regionally; coastal region shows moderate performance.


## Contributors

* Calvince Kaunda
* Gloryann Otieno
* Peter Nyakundi
* Samuel Marimbi
* Sanayet Sankaine

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.


