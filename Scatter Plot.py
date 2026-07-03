import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

plt.figure(figsize=(8,5))

plt.scatter(
    data["Month"],
    data["Sales"]
)

plt.title("Monthly Sales Scatter Plot")

plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
