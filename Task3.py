import pandas as pd
# ── Load Data ──────────────────────────────────────────
df = pd.read_csv("students.csv")
print("Dataset loaded successfully.")
print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns\n")
# ── Inspect Data ────────────────────────────────────────
print("=== First 5 Rows ===")
print(df.head())
print("\n=== Data Info ===")
print(df.info())
# ── Clean Data ──────────────────────────────────────────
before = len(df)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print(f"\nRows removed during cleaning: {before - len(df)}")
# ── Analysis ────────────────────────────────────────────
# 1. Top scorer overall
top = df.loc[df['marks'].idxmax()]
print(f"\nTop Scorer: {top['name']} — {top['marks']} marks ({top['subject']})")
# 2. Average marks per subject
avg_by_subject = df.groupby("subject")["marks"].mean().round(2)
print("\nAverage Marks by Subject:")
print(avg_by_subject)
# 3. Students with marks above average
overall_avg = df['marks'].mean()
above_avg = df[df['marks'] > overall_avg]
print(f"\nOverall Average: {overall_avg:.2f}")
print(f"Students above average: {len(above_avg)}")
print(above_avg[['name', 'subject', 'marks']])
# 4. Grade distribution
grade_count = df["grade"].value_counts()
print("\nGrade Distribution:")
print(grade_count)
# 5. Export summary
above_avg.to_csv("top_performers.csv", index=False)
print("\n[OK] Summary exported to top_performers.csv")
