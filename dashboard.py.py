import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# DATA
# -----------------------------
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sales = [50000, 90000, 60000, 92000, 61000, 103000,
         101000, 88000, 129000, 94000, 105000, 82000]

profit = [12000, 18000, 15000, 20000, 16000, 22000,
          21000, 19000, 25000, 20000, 23000, 17000]

categories = ['Technology', 'Furniture', 'Office Supplies', 'Electronics', 'Others']
category_sales = [28, 25, 22, 15, 10]

products = ['Laptop', 'Office Chair', 'Smartphone', 'Desk', 'Headphones']
product_sales = [85000, 75000, 73000, 62000, 45000]

payment_methods = ['Credit Card', 'Debit Card', 'UPI', 'Cash']
payment_percent = [43.2, 28.4, 17.6, 10.8]

regions = ['North', 'South', 'East', 'West', 'Central']
region_sales = [350000, 300000, 240000, 200000, 150000]

customer_segments = ['High Value', 'Medium Value', 'Low Value']
segment_values = [28, 44, 28]

acquisition = [12, 25, 53, 56, 73, 55, 56, 69, 48, 40, 67, 52]

customer_tenure = ['<3 Months', '3-6 Months', '6-12 Months',
                    '12-24 Months', '>24 Months']
tenure_values = [18, 24, 27, 20, 10]

# -----------------------------
# FIGURE
# -----------------------------
fig = plt.figure(figsize=(18, 10), facecolor='white')

# MAIN TITLE
fig.suptitle('BUSINESS SALES PERFORMANCE DASHBOARD',
             fontsize=28,
             fontweight='bold',
             color='black',
             y=0.99)

# -----------------------------
# TOP SUMMARY BOXES
# -----------------------------
summary_boxes = [
    ('TOTAL SALES\n$1,071,000', '#7FDBFF'),
    ('TOTAL PROFIT\n$218,000', '#90EE90'),
    ('TOTAL ORDERS\n500', '#FFA500'),
    ('TOTAL CUSTOMERS\n500', '#DDA0DD'),
    ('AVG ORDER VALUE\n$2,142', '#40E0D0'),
    ('PROFIT MARGIN\n20.35%', '#CD7F6F')
]

x_positions = [0.08, 0.24, 0.40, 0.56, 0.72, 0.88]

for i, (text, color) in enumerate(summary_boxes):
    fig.text(x_positions[i], 0.84, text,
             fontsize=15,
             ha='center',
             va='center',
             bbox=dict(boxstyle='round,pad=0.8',
                       facecolor=color,
                       edgecolor='black'))

# -----------------------------
# CHART 1 - SALES OVER TIME
# -----------------------------
ax1 = plt.subplot(3, 3, 1)
ax1.plot(months, sales, marker='o', linewidth=3)
ax1.set_title('Sales Over Time', fontsize=14)
ax1.grid(True)
ax1.set_ylabel('Sales')

# -----------------------------
# CHART 2 - SALES BY CATEGORY
# -----------------------------
ax2 = plt.subplot(3, 3, 2)
ax2.pie(category_sales,
        labels=categories,
        autopct='%1.1f%%',
        startangle=90)
ax2.set_title('Sales By Category', fontsize=14)

# -----------------------------
# CHART 3 - TOP PRODUCTS
# -----------------------------
ax3 = plt.subplot(3, 3, 3)
ax3.barh(products, product_sales)
ax3.set_title('Top Products By Sales', fontsize=14)
ax3.set_xlabel('Sales')

# -----------------------------
# CHART 4 - SALES & PROFIT
# -----------------------------
ax4 = plt.subplot(3, 3, 4)
ax4.bar(months, sales, label='Sales')
ax4.plot(months, profit, marker='o', linewidth=3, label='Profit')
ax4.set_title('Sales & Profit By Month', fontsize=14)
ax4.legend()

# -----------------------------
# CHART 5 - PAYMENT METHOD
# -----------------------------
ax5 = plt.subplot(3, 3, 5)
ax5.pie(payment_percent,
        labels=payment_methods,
        autopct='%1.1f%%',
        startangle=90)
ax5.set_title('Sales By Payment Method', fontsize=14)

# -----------------------------
# CHART 6 - REGION SALES
# -----------------------------
ax6 = plt.subplot(3, 3, 6)
ax6.bar(regions, region_sales)
ax6.set_title('Sales By Region', fontsize=14)
ax6.set_ylabel('Revenue')

# -----------------------------
# CHART 7 - CUSTOMER SEGMENTATION
# -----------------------------
ax7 = plt.subplot(3, 3, 7)
ax7.pie(segment_values,
        labels=customer_segments,
        autopct='%1.1f%%',
        startangle=90)
ax7.set_title('Customer Segmentation', fontsize=14)

# -----------------------------
# CHART 8 - CUSTOMER ACQUISITION
# -----------------------------
ax8 = plt.subplot(3, 3, 8)
ax8.plot(months, acquisition, marker='o', linewidth=3)
ax8.set_title('Customer Acquisition', fontsize=14)
ax8.grid(True)

# -----------------------------
# CHART 9 - CUSTOMER TENURE
# -----------------------------
ax9 = plt.subplot(3, 3, 9)
ax9.bar(customer_tenure, tenure_values)
ax9.set_title('Sales By Customer Tenure', fontsize=14)

# ----------------------------
# LAYOUT FIX
# -----------------------------
plt.tight_layout(rect=[0, 0, 1, 0.76])

plt.savefig("output.png")
plt.show()