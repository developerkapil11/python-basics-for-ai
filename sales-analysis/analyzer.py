from helpers import calculate_total, format_currency;
import pandas as pd;
import json;
import os;

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")

    df = pd.read_csv(data_path)
    
    print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")
    totals = []

    for index, row in df.iterrows():
        total = calculate_total(row['quantity'], row['price'])
        totals.append(total)
    
    df['total'] = totals

    print('Slales Data:')
    for index, row in df.iterrows():
        formatted_total = format_currency(row['total'])
        print(f"{row['product']}: {formatted_total}")

    grand_total = df['total'].sum()

    print(f"grand_total: {format_currency(grand_total)}")

    print(df, 'this is csv with totals')

    os.makedirs('output', exist_ok=True)
    df.to_csv("output/sales_csv_with_total.csv", index=False)

    df.to_excel('output/sales_excel_with_total.xlsx', index =  False)

    df.to_json('output/sales_json_with_total.json', orient='records', indent=2)

    print('All files created Successfully inside output folder')
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

readJson = pd.read_json("output/sales_json_with_total.json")

with open("output/sales_json_with_total.json", 'r') as f:
    readJson = f.read()
    # print(readJson)

readExcel = pd.read_excel("output/sales_excel_with_total.xlsx")
# print(readExcel)