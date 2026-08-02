# 📊 Sales Business Metrics Analysis

## Project Problem Statement

Businesses generate large volumes of sales data daily, making it difficult to identify trends, monitor profitability, and evaluate overall business performance. Raw data alone provides little value unless it is transformed into meaningful insights. This project analyses historical sales data to uncover business trends, calculate key performance indicators (KPIs), and develop an interactive dashboard that supports informed business decision-making.

---

## 🎯 Aim of the Project

The aim of this project was to analyse sales business data using Python and Google Looker Studio to identify sales patterns, evaluate business performance, calculate important business metrics, and present the findings through an interactive dashboard.

---

## 📌 Objectives and Steps Taken

### Objectives
- Import and understand the sales dataset.
- Clean and prepare the data.
- Perform Exploratory Data Analysis (EDA).
- Calculate business KPIs.
- Identify sales trends and patterns.
- Build an interactive dashboard.
- Present business insights and recommendations.

### Steps Taken

### 1. Data Understanding
- Imported the dataset into Databricks.
- Reviewed the dataset structure.
- Checked for missing values and duplicates.
- Verified data types.
- Converted the Date column into datetime format.

### 2. Data Preparation
- Converted Sales and Cost of Sales from Decimal to Float.
- Created new date fields:
  - Year
  - Month
  - Month Number
  - Day of Week
- Calculated:
  - Gross Profit
  - Gross Profit Percentage
  - Gross Profit per Unit
  - Sales Price per Unit

### 3. Exploratory Data Analysis (EDA)
Analysed:
- Monthly Sales
- Yearly Sales
- Sales by Day of Week
- Quantity Sold
- Gross Profit
- Cost of Sales
- Overall Business Performance

### 4. Business KPIs
Calculated:
- Total Sales
- Total Cost of Sales
- Total Gross Profit
- Total Quantity Sold
- Average Sales Price per Unit
- Average Gross Profit Percentage
- Highest Sales Day
- Lowest Sales Day
- Total Transactions

### 5. Dashboard Development
Developed an interactive dashboard in Google Looker Studio containing:
- Summary Page
- Detailed Analysis Page
- Glossary Page

Dashboard features include:
- KPI Scorecards
- Sales Trend Over Time
- Sales by Month
- Sales by Day of Week
- Sales vs Cost of Sales
- Gross Profit Trend
- Quantity Sold by Month
- Interactive Filters

---

## 📈 Summary of Results

The analysis revealed the following key findings:

- Total Sales amounted to approximately **R186.9 million**.
- Total Cost of Sales amounted to approximately **R194.0 million**.
- The business recorded an overall **negative Gross Profit** of approximately **R7.1 million**, indicating that costs exceeded revenue.
- Sales performance varied across different months, showing seasonal fluctuations.
- Customer purchasing behaviour differed across the days of the week.
- Quantity sold also varied by month, indicating changes in product demand.
- Sales trends changed over time, highlighting periods of stronger and weaker business performance.
- The dashboard provides an interactive way to monitor KPIs and explore business performance.

---

## 🛠️ Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Databricks
- Google Looker Studio
- GitHub

---

## ✅ Conclusion

This project successfully transformed raw sales data into meaningful business insights through data cleaning, exploratory data analysis, KPI development, and dashboard creation. The findings revealed that although the business generated strong sales revenue, the Cost of Sales exceeded Total Sales, resulting in an overall negative Gross Profit. This indicates the need for improved cost management to enhance profitability.

The interactive dashboard allows users to monitor key business metrics, analyse sales trends, and make data-driven decisions. Overall, the project demonstrates practical skills in data preparation, business analysis, Python programming, dashboard development, and data visualisation.

---

## 💡 Recommendations

- Review and reduce the Cost of Sales to improve profitability.
- Investigate the factors contributing to high-performing months and apply similar strategies during lower-performing periods.
- Focus marketing efforts on the best-performing days of the week.
- Monitor Gross Profit alongside Total Sales to improve financial performance.
- Continue using dashboards to support business monitoring and decision-making.
- Conduct further analysis at product and customer level to identify additional opportunities for growth.

---
