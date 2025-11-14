"""
SIMPLE JUPYTER NOTEBOOK VERSION
Copy each section into a separate Jupyter cell
All graphs will display INLINE with plt.show()

Author: Sukesh Singla
Date: November 13, 2025
"""

# ============================================================
# CELL 1: IMPORTS AND SETUP
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configure for Jupyter
%matplotlib inline
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['figure.dpi'] = 100

pd.set_option('display.max_columns', None)
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("✅ Setup complete!")


# ============================================================
# CELL 2: LOAD DATA
# ============================================================
# Update this path to where your CSV file is located
df = pd.read_csv('car_prices_cleaned.csv')

print("First 5 rows:")
df.head()


# ============================================================
# CELL 3: DATA INFO
# ============================================================
print(f"Dataset Shape: {df.shape}")
print(f"Total Records: {len(df):,}")
df.info()


# ============================================================
# CELL 4: MISSING VALUES ANALYSIS
# ============================================================
null_df = pd.DataFrame({
    'Column': df.columns,
    'Null Count': df.isnull().sum().values,
    'Null %': (df.isnull().sum() / len(df) * 100).values
})
null_df[null_df['Null Count'] > 0].sort_values('Null Count', ascending=False)


# ============================================================
# CELL 5: VISUALIZATION 1 - Missing Values Bar Chart
# ============================================================
null_counts = df.isnull().sum().sort_values(ascending=False)
null_counts = null_counts[null_counts > 0]

plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(null_counts)), null_counts.values, 
               color='#E74C3C', alpha=0.8, edgecolor='black')
plt.xticks(range(len(null_counts)), null_counts.index, rotation=45, ha='right')
plt.ylabel('Missing Values', fontsize=12, fontweight='bold')
plt.title('Missing Values by Column', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()  # 👈 THIS SHOWS THE GRAPH!


# ============================================================
# CELL 6: VISUALIZATION 2 - Missing Values Heatmap
# ============================================================
plt.figure(figsize=(12, 8))
sns.heatmap(df.isnull(), cbar=True, yticklabels=False, cmap='viridis')
plt.title('Missing Values Heatmap', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()  # 👈 THIS SHOWS THE GRAPH!


# ============================================================
# CELL 7: QUERY 2.1 - Price Statistics
# ============================================================
print("CAR PRICE STATISTICS")
print(f"Average: ${df['sellingprice'].mean():,.2f}")
print(f"Minimum: ${df['sellingprice'].min():,.2f}")
print(f"Maximum: ${df['sellingprice'].max():,.2f}")


# ============================================================
# CELL 8: QUERY 2.2 - Unique Colors
# ============================================================
print(f"Unique colors: {df['color'].nunique()}")
print(f"Colors: {', '.join(map(str, df['color'].unique()))}")


# ============================================================
# CELL 9: QUERY 2.3 - Brands and Models
# ============================================================
print(f"Unique brands: {df['make'].nunique()}")
print(f"Unique models: {df['model'].nunique()}")


# ============================================================
# CELL 10: QUERY 2.4 - High Price Cars
# ============================================================
high_price = df[df['sellingprice'] > 165000]
print(f"Cars > $165K: {len(high_price)}")
high_price.head()


# ============================================================
# CELL 11: QUERY 2.5 - Top 5 Models
# ============================================================
top_models = df['model'].value_counts().head(5)
print("Top 5 Most Sold Models:")
top_models


# ============================================================
# CELL 12: QUERY 2.6 - Average Price by Brand
# ============================================================
avg_by_brand = df.groupby('make')['sellingprice'].mean().sort_values(ascending=False)
print("Top 10 Brands by Average Price:")
avg_by_brand.head(10)


# ============================================================
# CELL 13: QUERY 2.7 - Min Price by Interior
# ============================================================
df.groupby('interior')['sellingprice'].min().sort_values().head(10)


# ============================================================
# CELL 14: QUERY 2.8 - Max Odometer by Year
# ============================================================
df.groupby('year')['odometer'].max().sort_values(ascending=False).head(15)


# ============================================================
# CELL 15: QUERY 2.9 - Create Car Age
# ============================================================
df['car_age'] = 2025 - df['year']
print("✅ Car age column created")
df[['year', 'car_age']].describe()


# ============================================================
# CELL 16: QUERY 2.10 - Filtered Cars
# ============================================================
filtered = df[(df['condition'] >= 48) & (df['odometer'] > 90000)]
print(f"Cars with condition≥48 and odometer>90K: {len(filtered)}")
filtered.head()


# ============================================================
# CELL 17: QUERY 2.11 - State Analysis
# ============================================================
newer = df[df['year'] > 2013]
state_prices = newer.groupby('state')['sellingprice'].mean().sort_values(ascending=False)
print("Top 10 States for Newer Cars:")
state_prices.head(10)


# ============================================================
# CELL 18: QUERY 2.12 - Value for Money
# ============================================================
threshold = df['condition'].quantile(0.80)
excellent = df[df['condition'] >= threshold]
value = excellent.groupby('make')['sellingprice'].mean().sort_values()
print(f"Excellent threshold: {threshold}")
print("\nTop 10 Value Brands:")
value.head(10)


# ============================================================
# CELL 19: VISUALIZATION 3 - Correlation Matrix
# ============================================================
numerical = df.select_dtypes(include=[np.number])
corr = numerical.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1)
plt.title('Correlation Matrix', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()  # 👈 THIS SHOWS THE GRAPH!


# ============================================================
# CELL 20: VISUALIZATION 4 - Price by Year
# ============================================================
avg_by_year = df.groupby('year')['sellingprice'].mean()

plt.figure(figsize=(14, 6))
plt.plot(avg_by_year.index, avg_by_year.values, 
         marker='o', linewidth=2, markersize=6, color='#2E86AB')
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Average Price ($)', fontsize=12, fontweight='bold')
plt.title('Average Selling Price by Year', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

# Trend line
z = np.polyfit(avg_by_year.index, avg_by_year.values, 1)
p = np.poly1d(z)
plt.plot(avg_by_year.index, p(avg_by_year.index), 
         "--", color='red', alpha=0.8, linewidth=2, label='Trend')
plt.legend()
plt.tight_layout()
plt.show()  # 👈 THIS SHOWS THE GRAPH!


# ============================================================
# CELL 21: VISUALIZATION 5 - Price by Odometer
# ============================================================
df['odo_bin'] = pd.cut(df['odometer'], bins=20)
avg_by_odo = df.groupby('odo_bin')['sellingprice'].mean()
centers = [i.mid for i in avg_by_odo.index]

plt.figure(figsize=(14, 6))
plt.scatter(centers, avg_by_odo.values, alpha=0.6, s=100, color='#A23B72')
plt.plot(centers, avg_by_odo.values, alpha=0.4, linewidth=2, color='#A23B72')
plt.xlabel('Odometer Reading', fontsize=12, fontweight='bold')
plt.ylabel('Average Price ($)', fontsize=12, fontweight='bold')
plt.title('Price by Odometer', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x/1000)}K'))
plt.tight_layout()
plt.show()  # 👈 THIS SHOWS THE GRAPH!

df = df.drop('odo_bin', axis=1)


# ============================================================
# CELL 22: VISUALIZATION 6 - Cars by State
# ============================================================
by_state = df['state'].value_counts()

plt.figure(figsize=(16, 8))
plt.bar(range(len(by_state)), by_state.values, 
        color='#F18F01', alpha=0.8, edgecolor='black')
plt.xlabel('State', fontsize=12, fontweight='bold')
plt.ylabel('Number of Cars', fontsize=12, fontweight='bold')
plt.title('Cars Sold by State', fontsize=14, fontweight='bold')
plt.xticks(range(len(by_state)), by_state.index, rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()  # 👈 THIS SHOWS THE GRAPH!

print("\nTop 3 States:")
for i, (state, count) in enumerate(by_state.head(3).items(), 1):
    print(f"{i}. {state}: {count:,} cars")


# ============================================================
# CELL 23: VISUALIZATION 7 - Price by Condition (Size 5)
# ============================================================
bins5 = range(int(df['condition'].min()), int(df['condition'].max()) + 6, 5)
df['cond5'] = pd.cut(df['condition'], bins=bins5)
avg_cond5 = df.groupby('cond5')['sellingprice'].mean()

plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(avg_cond5)), avg_cond5.values, 
               color='#06A77D', alpha=0.8, edgecolor='black')
plt.xlabel('Condition Range', fontsize=12, fontweight='bold')
plt.ylabel('Average Price ($)', fontsize=12, fontweight='bold')
plt.title('Price by Condition Ranges (Size 5)', fontsize=14, fontweight='bold')
plt.xticks(range(len(avg_cond5)), [str(x) for x in avg_cond5.index], 
           rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')

for bar in bars:
    h = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., h, f'${h:,.0f}', 
             ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()  # 👈 THIS SHOWS THE GRAPH!

df = df.drop('cond5', axis=1)


# ============================================================
# CELL 24: VISUALIZATION 8 - Cars by Condition (Size 10)
# ============================================================
bins10 = range(int(df['condition'].min()), int(df['condition'].max()) + 11, 10)
df['cond10'] = pd.cut(df['condition'], bins=bins10)
count_cond10 = df['cond10'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(count_cond10)), count_cond10.values, 
               color='#C73E1D', alpha=0.8, edgecolor='black')
plt.xlabel('Condition Range', fontsize=12, fontweight='bold')
plt.ylabel('Number of Cars', fontsize=12, fontweight='bold')
plt.title('Cars by Condition Ranges (Size 10)', fontsize=14, fontweight='bold')
plt.xticks(range(len(count_cond10)), [str(x) for x in count_cond10.index], 
           rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')

for bar in bars:
    h = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., h, f'{int(h)}', 
             ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()  # 👈 THIS SHOWS THE GRAPH!

df = df.drop('cond10', axis=1)


# ============================================================
# CELL 25: VISUALIZATION 9 - Price by Color (With Outliers)
# ============================================================
df_color = df[df['color'].notna()].copy()
color_order = df_color.groupby('color')['sellingprice'].median().sort_values(ascending=False).index

plt.figure(figsize=(14, 6))
sns.boxplot(data=df_color, x='color', y='sellingprice', 
            order=color_order, palette='Set2')
plt.xlabel('Color', fontsize=12, fontweight='bold')
plt.ylabel('Price ($)', fontsize=12, fontweight='bold')
plt.title('Price by Color (With Outliers)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()  # 👈 THIS SHOWS THE GRAPH!


# ============================================================
# CELL 26: VISUALIZATION 10 - Price by Color (Without Outliers)
# ============================================================
# Remove outliers
Q1 = df_color['sellingprice'].quantile(0.25)
Q3 = df_color['sellingprice'].quantile(0.75)
IQR = Q3 - Q1
df_clean = df_color[
    (df_color['sellingprice'] >= Q1 - 1.5*IQR) & 
    (df_color['sellingprice'] <= Q3 + 1.5*IQR)
]

print(f"Removed {len(df_color) - len(df_clean):,} outliers")

plt.figure(figsize=(14, 6))
sns.boxplot(data=df_clean, x='color', y='sellingprice', 
            order=color_order, palette='Set2')
plt.xlabel('Color', fontsize=12, fontweight='bold')
plt.ylabel('Price ($)', fontsize=12, fontweight='bold')
plt.title('Price by Color (Without Outliers)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()  # 👈 THIS SHOWS THE GRAPH!


# ============================================================
# CELL 27: SUMMARY
# ============================================================
print("="*80)
print("✅ ANALYSIS COMPLETE!")
print("="*80)
print(f"""
Dataset: {len(df):,} records, {len(df.columns)} features
Average Price: ${df['sellingprice'].mean():,.2f}
Most Popular: {df['model'].value_counts().index[0]}

All 10 visualizations displayed inline! 🎉
""")
print("="*80)
