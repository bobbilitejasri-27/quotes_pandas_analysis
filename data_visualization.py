import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("quotes_dataset.csv")

author_counts = data["Author"].value_counts()

plt.figure(figsize=(8,5))
author_counts.plot(kind="bar")

plt.title("Number of Quotes by Author")
plt.xlabel("Author")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("author_chart.png")

print("Chart saved as author_chart.png")
