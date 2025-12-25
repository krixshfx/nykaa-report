import pandas as pd
import matplotlib.pyplot as plt
import os

# Create visualizations directory if it doesn't exist
if not os.path.exists('nykaa_market_report/visualizations'):
    os.makedirs('nykaa_market_report/visualizations')

# Read data from CSV
df = pd.read_csv('nykaa_market_report/data/report_data.csv')

# --- 1. Market Growth ---
market_size_2024 = df[df['Metric'] == 'Indian BPC Market 2024 (USD)']['Value'].values[0]
market_forecast_2033 = df[df['Metric'] == 'Indian BPC Market 2033 (USD)']['Value'].values[0]
market_size_2024 = float(market_size_2024.replace('B', ''))
market_forecast_2033 = float(market_forecast_2033.replace('B', ''))

plt.figure(figsize=(8, 6))
plt.bar(['2024', '2033'], [market_size_2024, market_forecast_2033], color=['#FF69B4', '#FFC0CB'])
plt.title('Indian BPC Market Growth (in Billion USD)')
plt.ylabel('Market Size (Billion USD)')
plt.savefig('nykaa_market_report/visualizations/market_growth.png')
plt.close()

# --- 2. Nykaa's Financial Performance ---
revenue_fy24 = df[df['Metric'] == 'Revenue FY24 (INR)']['Value'].values[0]
net_profit_fy24 = df[df['Metric'] == 'Net Profit FY24 (INR)']['Value'].values[0]
revenue_fy24 = float(revenue_fy24.replace('cr', ''))
net_profit_fy24 = float(net_profit_fy24.replace('cr', ''))

plt.figure(figsize=(8, 6))
plt.bar(['Revenue', 'Net Profit'], [revenue_fy24, net_profit_fy24], color=['#FF69B4', '#FFC0CB'])
plt.title('Nykaa Financial Performance FY24 (in Crore INR)')
plt.ylabel('Amount (Crore INR)')
plt.savefig('nykaa_market_report/visualizations/financial_performance.png')
plt.close()

# --- 3. Online BPC Market Share ---
nykaa_share = df[df['Metric'] == 'Online BPC Market Share 2023']['Value'].values[0]
myntra_share = df[df['Metric'] == 'Myntra Online BPC Market Share 2023']['Value'].values[0]
amazon_share = df[df['Metric'] == 'Amazon Online BPC Market Share 2023']['Value'].values[0]
nykaa_share = float(nykaa_share.replace('%', ''))
myntra_share = float(myntra_share.replace('%', ''))
amazon_share = float(amazon_share.replace('%', ''))
other_share = 100 - nykaa_share - myntra_share - amazon_share

labels = ['Nykaa', 'Myntra', 'Amazon', 'Others']
sizes = [nykaa_share, myntra_share, amazon_share, other_share]
colors = ['#FF69B4', '#FFC0CB', '#FFE4E1', '#FFF0F5']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Online BPC Market Share 2023')
plt.axis('equal')
plt.savefig('nykaa_market_report/visualizations/market_share.png')
plt.close()

# --- 4. Nykaa's Revenue Mix ---
bpc_share = df[df['Metric'] == 'BPC Segment of Revenue (Q4 FY25)']['Value'].values[0]
fashion_share = df[df['Metric'] == 'Fashion Segment of Revenue (Q4 FY25)']['Value'].values[0]
bpc_share = float(bpc_share.replace('%', ''))
fashion_share = float(fashion_share.replace('%', ''))

labels = ['Beauty & Personal Care', 'Fashion']
sizes = [bpc_share, fashion_share]
colors = ['#FF69B4', '#FFC0CB']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Nykaa Revenue Mix (Q4 FY25)')
plt.axis('equal')
plt.savefig('nykaa_market_report/visualizations/revenue_mix.png')
plt.close()

# --- 5. SWOT Materiality Scorecard ---
swot_data = {
    'Threat: Intense Competition': [5, 5, 25],
    'Weakness: BPC Dependency': [4, 5, 20],
    'Opportunity: Tier II/III Expansion': [4, 4, 16],
    'Strength: Brand Equity': [5, 3, 15]
}
swot_df = pd.DataFrame(swot_data, index=['Impact', 'Likelihood', 'Materiality']).T

plt.figure(figsize=(8, 6))
plt.imshow(swot_df, cmap='hot', interpolation='nearest')
plt.colorbar(label='Materiality')
plt.xticks(range(len(swot_df.columns)), swot_df.columns)
plt.yticks(range(len(swot_df.index)), swot_df.index)
plt.title('SWOT Materiality Scorecard')
plt.savefig('nykaa_market_report/visualizations/swot_materiality.png')
plt.close()

print("Visualizations created successfully!")
