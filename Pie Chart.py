import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

plt.figure(figsize=(8,8))

plt.pie(
    data["Sales"],
    labels=data["Month"],
    autopct="%1.1f%%"
)

plt.title("Sales Distribution")

plt.show()