import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
data = pd.read_csv("sales_data.csv")

# Display Data
print("\nSales Data\n")
print(data)

# Line Chart
plt.figure(figsize=(10,5))

plt.plot(
    data["Month"],
    data["Sales"],
    marker="o",
    linewidth=3
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()