import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

plt.figure(figsize=(10,5))

plt.bar(
    data["Month"],
    data["Sales"]
)

plt.title("Monthly Sales")

plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
