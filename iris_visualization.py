import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/Iris.csv")

# Display first 5 rows
print(df.head())

# ---------------- BAR CHART ----------------
species_count = df['Species'].value_counts()

plt.figure(figsize=(6,5))
species_count.plot(kind='bar')

plt.title("Count of Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")

plt.savefig("images/bar_chart.png")
plt.close()

# ---------------- HISTOGRAM ----------------
plt.figure(figsize=(6,5))

plt.hist(df['SepalLengthCm'], bins=10)

plt.title("Sepal Length Distribution")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")

plt.savefig("images/histogram.png")
plt.close()

# ---------------- SCATTER PLOT ----------------
plt.figure(figsize=(6,5))

sns.scatterplot(
    x='SepalLengthCm',
    y='PetalLengthCm',
    hue='Species',
    data=df
)

plt.title("Sepal Length vs Petal Length")

plt.savefig("images/scatter_plot.png")
plt.close()

print("Visualizations created successfully!")