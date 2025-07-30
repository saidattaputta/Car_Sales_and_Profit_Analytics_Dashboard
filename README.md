# Car Sales & Service Analytics Dashboard

## Overview

This project analyzes car sales and after-sales service (recalls and sentiment) across multiple models and dealers (2018-2019), based on `CarSalesByModelStart-copy.xlsx`. It delivers key insights and business outcomes via Python (data wrangling) and interactive dashboards (Power BI/Tableau), helping stakeholders make data-driven decisions.

---

##  Data Description

- **File:** `CarSalesByModelStart-copy.xlsx`
- **Key Sheets:**
  - **CarSales:** Raw sales transactions (Date, Model, Dealer, Quantity, Profit)
  - **Sheet1:** Sum of quantity sold by dealer
  - **Sheet2:** Monthly profit by model
  - **Sheet3:** Annual profit by dealer
  - **Sheet4:** Model-dealer-wise profit

---

## Process & Tech Stack

### 1. Data Loading & Cleaning
```
import pandas as pd
data = pd.read_excel('CarSalesByModelStart-copy.xlsx', sheet_name='CarSales')
data.dropna(inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
```


### 2. Feature Engineering

```
data['YearMonth'] = data['Date'].dt.to_period('M')
```

### 3. Aggregations

Sales by model
```
sales_by_model = data.groupby('Model')['Quantity Sold'].sum()
```

Profit by dealer
```
profit_by_dealer = data.groupby('Dealer ID')['Profit'].sum()
```


### 4. Visualization

- Plots in **matplotlib/Power BI/Tableau**:
  - Monthly Profit & Units Sold
  - Recalls by Model/System
  - Profit by Dealer
  - Sentiment Breakdown

---

## 📊 Dashboards

**Sales Dashboard:**
<img width="694" height="385" alt="Screenshot 2025-07-30 at 1 46 50 PM" src="https://github.com/user-attachments/assets/09c58e81-7c39-486c-99af-ecdae23467ce" />


**Service Dashboard:**
<img width="653" height="390" alt="Screenshot 2025-07-30 at 1 47 01 PM" src="https://github.com/user-attachments/assets/56c8f85f-7802-4a0b-a5cd-83e66141b5af" />


---

## 📌 Insights & Outcomes

- **Total Profit:** $29,968,866
- **Total Quantity Sold:** 58,118 units
- **Top Models:** Labrador and Salish lead in both profit and sales.
- **Best Dealers:** Dealer 1288 has the highest profit consistency.
- **Seasonality:** Sales/profit peak around May-June, then drop in winter.
- **Recalls:** Labrador faces the highest recalls; major systems affected include Steering, Brakes, Engine.
- **Sentiment:** Predominantly Positive with periodic Negative spikes correlating to recall surges.
- **Underperformers:** Hudson, Champlain show lower sales and higher recall/negative sentiment.
- **Dealer Trends:** Profits mirror sales volumes across dealers.


---

## 🏁 Conclusion

This analytics suite delivers actionable insights on car model & dealer performance, customer sentiment, and recall root causes. The process enables strategic interventions for marketing and after-sales improvement.

---

*For more details, refer to the project code, Excel file, and interactive dashboards.*
