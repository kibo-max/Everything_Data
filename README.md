# Oraimo Sales Forecasting

## Project Overview

This project focuses on building a time series forecasting model for Oraimo, a consumer electronics brand. Using sales data from January to October 2024, we aim to predict sales for November 2024. The project will help improve demand planning, minimize stockouts and overstocking, and enable more informed inventory and marketing decisions.

## Business Understanding

Oraimo faces demand fluctuations across different cities and product categories. Without accurate forecasting, the company risks overstocking or understocking its inventory, leading to losses from unsold stock or missed sales opportunities. Analyzing sales data is crucial for assessing business performance and identifying improvement areas. Sales forecasting goes a step further by predicting future demand, which helps optimize inventory management, workforce planning and supply chain decisions.

### Objectives

- To build a recommender system that forecasts sales for Oraimo across different cities and product categories.
- To analyze historical sales data to understand demand patterns and fluctuations.
- To implement a forecasting model that predicts sales for the upcoming month, reducing the risks of overstocking and understocking.
- To optimize inventory management and resource allocation by providing more accurate future demand insights.

### Stakeholders

- Oraimo Management Team – for strategic planning and decision-making
- Sales and Inventory Teams – to improve stock management and meet customer demand
- Supply Chain & Logistics Teams – for efficient distribution and resource allocation
- Retailers & Shop Managers – to ensure timely product availability
- Data & Business Analysts – to monitor performance and model accuracy

## Metrics of Success

- Identify clear and actionable sales trends across cities, shops, and product types.
- Ensure the final forecast aligns with observed historical patterns and seasonal demand shifts.
- Provide insights that inform inventory and resource planning for November 2024.
- Achieve a forecasting model with:

## Data Understanding

The Oraimo Sales dataset is from a Data Science community, DataVerse. The dataset contains historical sales records from January to October 2024 by Oraimo across multiple shops across the country. The dataset contains 19,802 rows and 14 columns.

#### Features:

**year** — Year of the sale (2024)  
**month** — Month name of the sale  
**date** — Raw string of the sale date  
**week** — Week number in the year  
**city** — Name of the city where the sale occurred  
**shop_name** — Name of the specific shop  
**model** — Specific product model sold  
**type** — Product type/category  
**quantity** — Number of units sold  
**sales_price** — Selling price per unit  
**amount** — Total revenue from the sale (quantity × sales_price)  
**source** — Sales channel 
**proper_date** — Cleaned datetime format of the sale  
**city_2** — Additional city labeling 

## Data Cleaning

In this step, we clean the dataset by handling missing values, duplicate values, standardizing data, dropping irrelevant columns and addressing any other issues to ensure that the data is reliable and ready for further analysis.

## Exploratory Data Analysis

In this section, we explore and visualize the data to understand its distribution, relationships and patterns. This will help in identifying trends, outliers and potential issues that could affect model performance. It also guides decisions on feature engineering and model selection.

## Feature Engineering

We prepare the dataset for modelling

## Modeling

We use SARIMA and XGBoost models to forecast sales for November 2024.

## Results

We evaluate the performance of our models using MAE and RMSE.

## Conclusion

We conclude by summarizing our findings and providing recommendations.

## Next Steps

We outline future work that can be done to improve the project.
