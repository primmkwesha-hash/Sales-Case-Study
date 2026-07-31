## Sales Business Metrics Analysis

### Project Overview
This project analyzes retail sales data to uncover business insights that can support decision-making. The analysis focuses on identifying sales trends, customer purchasing patterns, pricing strategies, profitability, and peak sales periods. Python was used in Databricks for data cleaning, exploratory data analysis (EDA), business metrics, and data visualization.


### Dataset Information
The dataset contains 1,053 rows and 14 columns, covering daily sales transactions from 2013 to 2016. It contains no missing values or duplicate records after data cleaning. The dataset includes sales, cost of sales, quantity sold, sales price per unit, gross profit, and date-related variables such as year, month, day, and day of the week.


### Business Questions
This analysis answers the following business questions:

- Which month generated the highest sales?
- Which month sold the highest quantity of products?
- How did the average sales price change throughout the year?
- Which months achieved the highest gross profit percentage?
- Which were the highest and lowest sales days?
- Which day of the week generated the highest average sales?
- What relationships exist between sales, quantity sold, cost of sales, and sales price?


### Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Databricks


### Key Findings

- May generated the highest total sales.
- May also recorded the highest quantity of products sold.
- October and November had the highest average sales prices.
- August recorded one of the lowest average sales prices while maintaining strong sales performance.
- October achieved the highest gross profit percentage, while December recorded the lowest.
- The highest single-day sales exceeded R850,000, while the lowest sales days were below R30,000.
- Saturday generated the highest average sales, followed by Friday, indicating stronger weekend demand.
- Sales, Cost of Sales, and Quantity Sold showed an extremely strong positive correlation.
- Sales Price per Unit showed a moderate negative correlation with Quantity Sold, suggesting that lower prices generally encourage higher sales volumes.


### Business Recommendations

- Increase inventory before high-demand months such as May and June.
- Schedule promotions during slower months like November and December to boost sales.
- Allocate additional staff and stock on Fridays and Saturdays to meet higher customer demand.
- Investigate the causes of the lowest-performing sales days to identify opportunities for improvement.
- Review pricing strategies used during successful months and apply similar approaches where appropriate.
- Continue monitoring pricing to maintain a balance between profitability and customer demand.


### Visualizations

The project includes the following visualizations:

- Monthly Sales Trend
- Monthly Quantity Sold
- Monthly Average Sales Price
- Monthly Gross Profit Percentage
- Top 10 Highest Sales Days
- Top 10 Lowest Sales Days
- Average Sales by Day of the Week
- Correlation Heatmap


### Conclusion

This analysis provided valuable insights into the company's sales performance, customer purchasing behaviour, pricing strategy, and profitability. Sales performance was largely driven by the quantity of products sold rather than higher selling prices. Seasonal demand patterns and promotional activities significantly influenced revenue, while correlation analysis confirmed strong relationships between sales, quantity sold, and costs. These findings can support better pricing decisions, inventory planning, marketing strategies, and future promotional campaigns.
