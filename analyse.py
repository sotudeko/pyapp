import pandas as pd
import matplotlib.pyplot as plt

def analyze_sales_data(file_path):
    """
    Reads a CSV file, analyzes sales data by product, and visualizes the results.
    """
    try:
        # Use pandas to read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        print("--- Original Sales Data ---")
        print(df)
        print("\n" + "="*30 + "\n")

        # Group by 'product' and sum the 'sales' column
        product_sales = df.groupby('product')['sales'].sum().reset_index()
        
        print("--- Total Sales by Product ---")
        print(product_sales)
        print("\n" + "="*30 + "\n")

        # Visualize the data using matplotlib
        plt.figure(figsize=(8, 6))
        plt.bar(product_sales['product'], product_sales['sales'], color=['skyblue', 'salmon', 'lightgreen'])
        plt.title('Total Sales by Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    analyze_sales_data('sales_data.csv')

