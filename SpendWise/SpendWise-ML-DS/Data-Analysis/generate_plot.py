import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load your data from the JSON file (modify the file path as necessary)
df = pd.read_json("dataset.json")

# Ensure 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set Seaborn style to 'whitegrid' for a clean and minimalist background
sns.set(style="whitegrid", palette="muted")

# Set color palette to a smooth blue
sns.set_palette(["#4A90E2"])

# Font setup for UI sans-serif bold font
plt.rcParams.update({'font.family': 'Arial', 'font.weight': 'bold'})  # Use Arial font with bold weight

# 1. Spending Trends Over Time (Line Plot)
monthly_spending = df.resample('M', on='Date')['Amount'].sum()
plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_spending.index, y=monthly_spending.values, color="#4A90E2")
plt.title("Total Spending Over Time", fontsize=16, color='black', weight='bold')
plt.xlabel("Date", fontsize=12, color='black', weight='bold')
plt.ylabel("Total Amount Spent", fontsize=12, color='black', weight='bold')
plt.xticks(color='black', weight='bold')
plt.yticks(color='black', weight='bold')
plt.gca().set_facecolor('white')  # White background for the plot
plt.grid(True, axis='y', linestyle='--', color='lightgray')  # Subtle grid lines
plt.savefig('static/expense_graph.png')
plt.close()

# 2. Spending by Category (Bar Plot)
category_spending = df.groupby('Category')['Amount'].sum()
plt.figure(figsize=(10, 6))
sns.barplot(x=category_spending.index, y=category_spending.values, color="#4A90E2")
plt.title("Spending by Category", fontsize=16, color='black', weight='bold')
plt.xlabel("Category", fontsize=12, color='black', weight='bold')
plt.ylabel("Total Amount", fontsize=12, color='black', weight='bold')
plt.xticks(rotation=45, color='black', weight='bold')
plt.yticks(color='black', weight='bold')
plt.gca().set_facecolor('white')
plt.grid(True, axis='y', linestyle='--', color='lightgray')
plt.savefig('static/category_graph.png')
plt.close()

# 4. Payment Mode Breakdown (Pie Chart)
payment_mode_count = df['Payment_Mode'].value_counts()
plt.figure(figsize=(6, 6))
payment_mode_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#4A90E2', '#8AB8E2', '#A1C6E5'])
plt.title("Payment Mode Distribution", fontsize=16, color='black', weight='bold')
plt.ylabel("", fontsize=12, color='black', weight='bold')  # Hide the y-label
plt.gca().set_facecolor('white')
plt.savefig('static/payment_mode_graph.png')
plt.close()

# 9. Impulse vs. Need Purchases by Category (Stacked Bar Plot)
impulse_need_by_category = df.pivot_table(values='Amount', index='Category', columns='is_Need', aggfunc='sum')
plt.figure(figsize=(10, 6))
impulse_need_by_category.plot(kind='bar', stacked=True, color=['#4A90E2', '#8AB8E2'])
plt.title("Impulse vs Need Purchases by Category", fontsize=16, color='black', weight='bold')
plt.xlabel("Category", fontsize=12, color='black', weight='bold')
plt.ylabel("Amount Spent", fontsize=12, color='black', weight='bold')
plt.xticks(color='black', weight='bold')
plt.yticks(color='black', weight='bold')
plt.gca().set_facecolor('white')
plt.grid(True, axis='y', linestyle='--', color='lightgray')
plt.savefig('static/impulse_need_graph.png')
plt.close()
