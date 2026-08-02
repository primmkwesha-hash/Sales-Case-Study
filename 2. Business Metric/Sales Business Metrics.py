# Databricks notebook source
# MAGIC %md
# MAGIC ###Import Libraries

# COMMAND ----------

import pandas as pd
import numpy as np

# COMMAND ----------

# MAGIC %md
# MAGIC ###Data Ingestion

# COMMAND ----------

df = spark.table('workspace.default.sales ')

# COMMAND ----------

df = spark.table('workspace.default.sales ').toPandas()
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Data Exploratory

# COMMAND ----------

df.info()

# COMMAND ----------

type(df["Sales"].iloc[0])

# COMMAND ----------

df["Sales"] = df["Sales"].astype(float)
df["Cost Of Sales"] = df["Cost Of Sales"].astype(float)

# COMMAND ----------

df["Date"] = pd.to_datetime(df["Date"])

# COMMAND ----------

df.info()

# COMMAND ----------

df

# COMMAND ----------

# MAGIC %md
# MAGIC The dataset consists of 1,053 rows and 4 columns: Date, Sales, Cost of Sales, and Quantity Sold. df.info() confirmed that the dataset contains no missing (null) values and no duplicate records. This indicates that the dataset is complete, consistent, and suitable for further analysis.

# COMMAND ----------

# MAGIC %md
# MAGIC Converted Date to a datetime format to enable time-series analysis. The Sales and Cost of Sales columns were converted to numeric (float) data types to ensure accurate calculations. Additional date features (Year, Month, Month Number, Day, and Day of Week) were extracted to support monthly and daily trend analysis.

# COMMAND ----------

# Check date range 

print("Start Date:", df["Date"].min())
print("End Date:", df["Date"].max())

# COMMAND ----------

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()
df["Day of Week"] = df["Date"].dt.day_name()
df["Month Number"] = df["Date"].dt.month



# COMMAND ----------

# Explore the new columns

df[["Year", "Month", "Day of Week"]].head()

# COMMAND ----------

# View monthly sales

monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()

monthly_sales

# COMMAND ----------

# Sort by descending order

monthly_sales.sort_values(by="Sales", ascending=False)

# COMMAND ----------

# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC May recorded the highest total sales, followed by April and June. On the other hand, November recorded the lowest total sales, followed by July and December. This shows that sales performance varied across the different months of the year.

# COMMAND ----------

# View yearly sales
df["Year"].value_counts()

# COMMAND ----------

# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC The dataset contains only two trading days for 2013, while 2014 and 2015 contain complete yearly records. The 2016 data is incomplete, containing 321 trading days. Therefore, comparisons involving 2013 and 2016 should be interpreted with caution, as they do not represent full calendar years.

# COMMAND ----------

# Calculate Gross Profit

df["Gross Profit"] = df["Sales"] - df["Cost Of Sales"]

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##Business Metrics

# COMMAND ----------

# MAGIC %md
# MAGIC Question 1
# MAGIC
# MAGIC What is the daily sales price per unit?

# COMMAND ----------

df['Sales Price per Unit'] = df['Sales'] / df['Quantity Sold']
df.head(5)

# COMMAND ----------

# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC The selling price changes from one day to another.

# COMMAND ----------

# MAGIC %md
# MAGIC Insight
# MAGIC
# MAGIC This suggests that the product price is not fixed and may have been affected by promotions, discounts, or pricing strategies.

# COMMAND ----------

# MAGIC %md
# MAGIC Recommendation
# MAGIC
# MAGIC The business should monitor changes in selling price and compare them with sales volume to determine whether lower prices increase customer demand and overall profitability.

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question 2
# MAGIC
# MAGIC What is the average unit sales price of this product?

# COMMAND ----------

average_price = df["Sales Price per Unit"].mean()

print("Average Unit Sales Price: R", round(average_price, 2))

# COMMAND ----------

# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC The average selling price of the product over the entire period was R37.07 per unit.

# COMMAND ----------

# MAGIC %md
# MAGIC Business Insight
# MAGIC
# MAGIC Although the daily selling price changed from day to day, the overall average price remained R37.07. This indicates that the product was generally sold around this price throughout the period.

# COMMAND ----------

# MAGIC %md
# MAGIC Recommendation
# MAGIC
# MAGIC Management can use R37.07 as a benchmark when evaluating pricing strategies. Daily prices that are significantly below this average may indicate promotional periods, while higher prices may reflect premium pricing. Comparing these price changes with sales volume can help determine the most profitable pricing strategy.

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question 3
# MAGIC
# MAGIC What is the daily % gross profit?

# COMMAND ----------

df["Gross Profit %"] = (
    (df["Sales"] - df["Cost Of Sales"]) / df["Sales"]
) * 100

df.head(5)

# COMMAND ----------

# How many days made profit
(df["Sales"] > df["Cost Of Sales"]).sum()

# COMMAND ----------

# How many days made a loss
(df["Sales"] < df["Cost Of Sales"]).sum()

# COMMAND ----------

# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC Observation
# MAGIC
# MAGIC Out of 1,053 trading days, 446 days (42.36%) recorded a positive gross profit, while 607 days (57.64%) recorded a gross loss. This indicates that the product incurred gross losses on more days than it generated gross profit.

# COMMAND ----------

# MAGIC %md
# MAGIC  Insight
# MAGIC
# MAGIC The product was sold at a loss on more than half of the trading days. This suggests that the selling price was frequently lower than the cost of sales. Possible reasons include promotional discounts, high procurement costs, or changes in pricing strategy.

# COMMAND ----------

# MAGIC %md
# MAGIC Recommendation
# MAGIC
# MAGIC The business should review its pricing strategy and cost structure to improve profitability. If the losses were due to promotional campaigns, management should assess whether the increase in sales volume was sufficient to justify the lower profit margins.

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question 4
# MAGIC
# MAGIC What is the daily % gross profit per unit?

# COMMAND ----------

df["Gross Profit per Unit"] = (
    df["Sales"] - df["Cost Of Sales"]
) / df["Quantity Sold"]

# COMMAND ----------

df["Gross Profit % per Unit"] = (
    df["Gross Profit per Unit"] /
    df["Sales Price per Unit"]
) * 100
df.head(5)

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question 5
# MAGIC
# MAGIC Pick any 3 periods during which this product was on promotion/special
# MAGIC a. What was the Price Elasticity of Demand during each of these periods?
# MAGIC b. In your opinion, does this product perform better or worse when sold at a
# MAGIC promotional price?

# COMMAND ----------

# View the top 30 products with the lowest sales price

df.sort_values(by="Sales Price per Unit").head(30)

# COMMAND ----------

# Display the promotion table

import pandas as pd

promotion_table = pd.DataFrame({
    "Promotion Period": ["Promotion 1", "Promotion 2", "Promotion 3"],
    "Start Date": ["2014-08-28", "2014-02-22", "2014-06-05"],
    "End Date": ["2014-09-08", "2014-03-08", "2014-06-19"],
    "Sales Price Range": [
        "R30.70 - R30.76",
        "R31.64 - R31.99",
        "R31.70 - R31.90"
    ]
})

display(promotion_table)

# COMMAND ----------

# MAGIC %md
# MAGIC Identified promotional periods based on days where the sales price per unit was consistently below the average selling price of R37.07. These periods were considered promotional periods because the product was sold at a significantly lower price than normal.

# COMMAND ----------

# Promotion 1
promo1 = df[(df["Date"] >= "2014-08-28") & (df["Date"] <= "2014-09-08")]

# Promotion 2
promo2 = df[(df["Date"] >= "2014-02-22") & (df["Date"] <= "2014-03-08")]

# Promotion 3
promo3 = df[(df["Date"] >= "2014-06-05") & (df["Date"] <= "2014-06-19")]

print("Promotion 1")
print(promo1[["Sales Price per Unit", "Quantity Sold"]].mean())

print("\nPromotion 2")
print(promo2[["Sales Price per Unit", "Quantity Sold"]].mean())

print("\nPromotion 3")
print(promo3[["Sales Price per Unit", "Quantity Sold"]].mean())

# COMMAND ----------

promotion_summary = pd.DataFrame({
    "Promotion": ["Promotion 1", "Promotion 2", "Promotion 3"],
    "Promotion Period": [
        "28 Aug 2014 - 8 Sep 2014",
        "22 Feb 2014 - 8 Mar 2014",
        "5 Jun 2014 - 19 Jun 2014"
    ],
    "Average Sales Price per Unit": [
        round(promo1["Sales Price per Unit"].mean(), 2),
        round(promo2["Sales Price per Unit"].mean(), 2),
        round(promo3["Sales Price per Unit"].mean(), 2)
    ],
    "Average Quantity Sold": [
        round(promo1["Quantity Sold"].mean()),
        round(promo2["Quantity Sold"].mean()),
        round(promo3["Quantity Sold"].mean())
    ]
})

display(promotion_summary)

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC
# MAGIC Promotion 1 had the lowest selling price and also had the highest quantity sold. As the selling price increased in Promotion 2 and Promotion 3, the quantity sold decreased.

# COMMAND ----------

# MAGIC %md
# MAGIC Insight
# MAGIC
# MAGIC This suggests that customers bought more units when the selling price was lower. However, because Promotion 2 and Promotion 3 had almost the same selling price but different quantities sold, price alone does not explain sales performance. Other factors, such as the time of year, customer demand, marketing efforts, or competition may also have influenced sales.

# COMMAND ----------

# MAGIC %md
# MAGIC Recommendation
# MAGIC
# MAGIC The product performs better during promotional periods because reducing the selling price increases customer demand. The first promotion achieved the highest average quantity sold, indicating that customers responded positively to the lower price. However, management should ensure that discounts are not too large, as excessive price reductions can reduce profit margins. A moderate promotional discount appears to be the best strategy for increasing sales while maintaining profitability.

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Question 6
# MAGIC
# MAGIC  Please derive any other interesting insight you can from the dataset provided. This
# MAGIC can include:
# MAGIC a. Interesting visuals
# MAGIC b. Reports
# MAGIC c. Dashboards
# MAGIC d. KPIs or metrics.
# MAGIC

# COMMAND ----------

df["Sales Price per Unit"] = df["Sales Price per Unit"].astype(float)
if 'Gross Profit' in df.columns: df["Gross Profit"] = df["Gross Profit"].astype(float)
df["Gross Profit %"] = df["Gross Profit %"].astype(float)
df["Gross Profit per Unit"] = df["Gross Profit per Unit"].astype(float)
df["Gross Profit % per Unit"] = df["Gross Profit % per Unit"].astype(float)

# COMMAND ----------

# Save the final dataset

df.to_csv("final_sales_business_metrics.csv", index=False)

# COMMAND ----------

import os
os.getcwd()

# COMMAND ----------

# MAGIC %md
# MAGIC ###Data Visualisation

# COMMAND ----------

df.columns

# COMMAND ----------

df["Month"] = df["Month"].astype(str)

# COMMAND ----------

monthly_sales = (
    df.groupby(["Month Number", "Month"])["Sales"]
      .sum()
      .reset_index()
      .sort_values("Month Number")
)

# COMMAND ----------

# View Sales by Month

import pandas as pd
import matplotlib.pyplot as plt

# Define the correct month order
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Convert Month to an ordered categorical variable
df["Month"] = pd.Categorical(
    df["Month"],
    categories=month_order,
    ordered=True
)

# Group sales by month
sales_by_month = (
    df.groupby("Month")["Sales"]
      .sum()
      .reindex(month_order)
)

# Plot
plt.figure(figsize=(10,5))
plt.bar(sales_by_month.index, sales_by_month.values)

plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Insight
# MAGIC
# MAGIC The high sales recorded in May suggest that customer demand was strongest during this month. This may have been influenced by effective promotional campaigns, seasonal buying patterns, or increased customer activity. In contrast, the low sales recorded in November indicate a period of weaker demand that may require additional marketing or promotional efforts.
# MAGIC
# MAGIC Recommendation
# MAGIC
# MAGIC Management should analyse the factors that contributed to May's strong sales performance and consider applying similar pricing, marketing, or promotional strategies during lower-performing months such as November, July, and December. This could help improve sales throughout the year.

# COMMAND ----------

# View Quantity Sold by Month

import matplotlib.pyplot as plt

monthly_quantity = (
    df.groupby(["Month Number", "Month"], observed=True)["Quantity Sold"]
      .sum()
      .reset_index()
      .sort_values("Month Number")
      .reset_index(drop=True)
)

plt.figure(figsize=(10,5))
plt.bar(monthly_quantity["Month"], monthly_quantity["Quantity Sold"])
plt.title("Monthly Quantity Sold")
plt.xlabel("Month")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC The chart shows that the quantity sold generally increasing from January to May, reaching its highest level in May. Although there was a slight decline in June, sales remained relatively strong before dropping noticeably in July. Quantity sold increased again in August but gradually declined from September to November, with November recording the lowest quantity sold. There was a small recovery in December, although sales remained lower than the peak months.

# COMMAND ----------

# View Average Sales Price per Unit by Month

import matplotlib.pyplot as plt

# Group by Month Number and Month
monthly_avg_price = (
    df.groupby(["Month Number", "Month"], observed=True)["Sales Price per Unit"]
      .mean()
      .reset_index()
      .sort_values("Month Number")
      .reset_index(drop=True)
)

# Plot
plt.figure(figsize=(10,5))
plt.bar(monthly_avg_price["Month"], monthly_avg_price["Sales Price per Unit"])

plt.title("Monthly Average Sales Price per Unit")
plt.xlabel("Month")
plt.ylabel("Average Sales Price per Unit (R)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC The monthly average sales price fluctuated throughout the year, indicating that the selling price was not constant. The lowest average selling price was recorded in August at approximately R35.6 per unit, while the highest average selling price was recorded in November at approximately R38.5 per unit. After reaching its peak in November, the average selling price declined slightly in December.

# COMMAND ----------

# View Average Gross Profit % per Unit by Month

import matplotlib.pyplot as plt

monthly_gp = (
    df.groupby(["Month Number", "Month"], observed=True)["Gross Profit % per Unit"]
      .mean()
      .reset_index()
      .sort_values("Month Number")
)

plt.figure(figsize=(10,5))
plt.plot(
    monthly_gp["Month"],
    monthly_gp["Gross Profit % per Unit"],
    marker="o",
    linewidth=2
)

plt.title("Monthly Gross Profit Percentage")
plt.xlabel("Month")
plt.ylabel("Gross Profit %")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC
# MAGIC Gross profit percentage was negative in most months which means the cost of sales was often higher than sales. July and October recorded the highest positive gross profit percentages showing the strongest profitability. December recorded the lowest gross profit percentage meaning the business made the biggest loss in that month.

# COMMAND ----------

# View the top 10 highest sales days

top10 = df.nlargest(10,"Sales")

plt.figure(figsize=(10,5))
plt.bar(top10["Date"].dt.strftime("%Y-%m-%d"), top10["Sales"])

plt.title("Top 10 Highest Sales Days")
plt.xlabel("Date")
plt.ylabel("Sales (R)")
plt.xticks(rotation=45)

plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC
# MAGIC The highest sales day was 1 March 2014 with sales exceeding R850,000. Most of the top 10 sales days occurred during 2014, indicating that this year contained many of the business's strongest trading days. The remaining top sales days generated between approximately R600,000 and R720,000, showing consistently high sales performance.

# COMMAND ----------

# View the bottom 10 lowest sales days

bottom10 = df.nsmallest(10,"Sales")

plt.figure(figsize=(10,5))
plt.bar(bottom10["Date"].dt.strftime("%Y-%m-%d"), bottom10["Sales"])

plt.title("Top 10 Lowest Sales Days")
plt.xlabel("Date")
plt.ylabel("Sales (R)")
plt.xticks(rotation=45)

plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC
# MAGIC The lowest sales day was 14 September 2016 with sales of about R20,000. The other low-sales days are mostly between R22,000 and R30,000, showing that these days performed much worse than the top sales days. Several of the lowest sales days occurred in 2015 and 2016, which may suggest weaker trading periods in those years.

# COMMAND ----------

# View the average sales by day of week

day_sales = df.groupby("Day of Week")["Sales"].mean().reindex([
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
])

plt.figure(figsize=(9,5))
plt.bar(day_sales.index, day_sales.values)

plt.title("Average Sales by Day of Week")
plt.xlabel("Day")
plt.ylabel("Average Sales (R)")

plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC Observation
# MAGIC
# MAGIC
# MAGIC Saturday recorded the highest average sales, making it the strongest sales day of the week. Friday also performed exceptionally well, with average sales only slightly lower than Saturday. Monday showed moderate sales, performing better than Tuesday, Wednesday and Thursday. Tuesday, Wednesday and Thursday recorded relatively similar sales, indicating stable but average customer activity during the middle of the week.
# MAGIC Sunday had the lowest average sales, suggesting that customer demand is weakest on this day.

# COMMAND ----------

# Check the correlation between the sales metrics
import seaborn as sns

plt.figure(figsize=(6,5))

sns.heatmap(
    df[["Sales","Cost Of Sales","Quantity Sold","Sales Price per Unit"]].corr(),
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Heatmap")

plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Observations
# MAGIC
# MAGIC
# MAGIC Sales and Cost of Sales have a nearly perfect positive correlation (1.00). This means that as sales increase, the cost of sales also increases proportionally. Sales and Quantity Sold have a very strong positive correlation (0.99). Higher sales are mainly driven by selling more units.Cost of Sales and Quantity Sold also have a very strong positive correlation (0.99). Selling more products naturally increases production or purchasing costs. Sales Price per Unit has a moderate negative correlation with Sales (-0.57). Higher selling prices tend to be associated with lower overall sales. Sales Price per Unit has a moderate negative correlation with Quantity Sold (-0.62). As the selling price increases, fewer units are sold. Sales Price per Unit also has a moderate negative correlation with Cost of Sales (-0.58). When fewer units are sold because of higher prices, the cost of supplying those products also decreases.

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# Business KPIs

total_sales = df["Sales"].sum()
total_cost = df["Cost Of Sales"].sum()
total_profit = df["Gross Profit"].sum()
total_quantity = df["Quantity Sold"].sum()

average_sale = df["Sales"].mean()
average_price = df["Sales Price per Unit"].mean()
average_profit_percent = df["Gross Profit %"].mean()

highest_sale = df["Sales"].max()
lowest_sale = df["Sales"].min()

transactions = len(df)

print("===== SALES BUSINESS KPIs =====")

print(f"Total Sales: R{total_sales:,.2f}")
print(f"Total Cost of Sales: R{total_cost:,.2f}")
print(f"Total Gross Profit: R{total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")

print(f"\nAverage Sale per Transaction: R{average_sale:,.2f}")
print(f"Average Sales Price per Unit: R{average_price:.2f}")
print(f"Average Gross Profit %: {average_profit_percent:.2f}%")

print(f"\nHighest Sales Day: R{highest_sale:,.2f}")
print(f"Lowest Sales Day: R{lowest_sale:,.2f}")

print(f"\nTotal Transactions: {transactions}")

# COMMAND ----------

import pandas as pd

kpi_table = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Cost of Sales",
        "Total Gross Profit",
        "Total Quantity Sold",
        "Average Sale per Transaction",
        "Average Sales Price per Unit",
        "Average Gross Profit %",
        "Highest Sales Day",
        "Lowest Sales Day",
        "Total Transactions"
    ],
    "Value": [
        f"R{total_sales:,.2f}",
        f"R{total_cost:,.2f}",
        f"R{total_profit:,.2f}",
        f"{total_quantity:,}",
        f"R{average_sale:,.2f}",
        f"R{average_price:.2f}",
        f"{average_profit_percent:.2f}%",
        f"R{highest_sale:,.2f}",
        f"R{lowest_sale:,.2f}",
        transactions
    ]
})

kpi_table

# COMMAND ----------

# MAGIC %md
# MAGIC Observation:
# MAGIC
# MAGIC The business generated strong sales revenue and a high transaction volume, but costs exceeded revenue, resulting in an overall loss.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Insight:
# MAGIC
# MAGIC Although sales performance is healthy, profitability remains a major concern due to high costs.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Recommendation:
# MAGIC
# MAGIC Focus on reducing costs, reviewing pricing strategies, and leveraging high-performing months and days to improve overall profitability.