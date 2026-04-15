import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("movies_dataset.csv")

# Basic checks
print("First 5 rows:")
print(df.head(), "\n")

print("Dataset info:")
print(df.info(), "\n")

print("Summary statistics:")
print(df.describe(numeric_only=True), "\n")

# Top rated movies
top_rated = df.sort_values("rating", ascending=False).head(5)
print("Top rated movies:")
print(top_rated[["title", "genre", "rating", "revenue"]], "\n")

# Average rating by genre
avg_rating_by_genre = (
    df.groupby("genre", as_index=False)["rating"]
    .mean()
    .sort_values("rating", ascending=False)
)
print("Average rating by genre:")
print(avg_rating_by_genre, "\n")

# Total revenue by genre
revenue_by_genre = (
    df.groupby("genre", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)
print("Total revenue by genre:")
print(revenue_by_genre, "\n")

# High-rated but lower-revenue movies
high_rated_low_revenue = df[(df["rating"] > 8.5) & (df["revenue"] < 500000000)]
print("High-rated but lower-revenue movies:")
print(high_rated_low_revenue[["title", "rating", "revenue"]], "\n")

# Chart 1: Average rating by genre
plt.figure(figsize=(8, 5))
plt.bar(avg_rating_by_genre["genre"], avg_rating_by_genre["rating"])
plt.title("Average Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("avg_rating_by_genre.png")
plt.close()

# Chart 2: Total revenue by genre
plt.figure(figsize=(8, 5))
plt.bar(revenue_by_genre["genre"], revenue_by_genre["revenue"])
plt.title("Total Revenue by Genre")
plt.xlabel("Genre")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("revenue_by_genre.png")
plt.close()

# Chart 3: Rating vs Revenue
plt.figure(figsize=(8, 5))
plt.scatter(df["rating"], df["revenue"])
for _, row in df.iterrows():
    plt.annotate(row["title"], (row["rating"], row["revenue"]), fontsize=8)
plt.title("Rating vs Revenue")
plt.xlabel("Rating")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("rating_vs_revenue.png")
plt.close()

print("Analysis complete. Charts saved as PNG files.")
