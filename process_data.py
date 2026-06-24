import os
import glob
import pandas as pd

def process_data(data_dir, output_file):
    # Locate all daily sales CSV files
    csv_files = glob.glob(os.path.join(data_dir, "daily_sales_data_*.csv"))
    
    if not csv_files:
        raise FileNotFoundError(f"No daily sales CSV files found in directory: {data_dir}")
        
    dfs = []
    for file_path in csv_files:
        print(f"Reading and processing: {os.path.basename(file_path)}")
        df = pd.read_csv(file_path)
        
        # 1. Filter for "pink morsel" only (case-insensitive)
        df = df[df['product'].str.lower() == 'pink morsel'].copy()
        
        # 2. Clean the price field (strip '$' sign and any non-numeric chars except decimals)
        df['price'] = df['price'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float)
        
        # 3. Clean quantity (convert to integer)
        df['quantity'] = df['quantity'].astype(int)
        
        # 4. Calculate sales (sales = price * quantity)
        df['sales'] = df['price'] * df['quantity']
        
        # 5. Extract only required columns (sales, date, region)
        df = df[['sales', 'date', 'region']]
        
        dfs.append(df)
        
    # Combine all DataFrames into one
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Save the cleaned dataset to formatted_data.csv
    combined_df.to_csv(output_file, index=False)
    print(f"\nSuccess! Formatted data saved to: {output_file}")
    print(f"Total rows processed: {len(combined_df)}")

if __name__ == "__main__":
    # Get paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "data")
    output_file = os.path.join(script_dir, "formatted_data.csv")
    
    process_data(data_dir, output_file)
