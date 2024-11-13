import pandas as pd
import requests
import datetime  # Import for date handling

# Define input parameters
path = r"C:\Desktop\your-excel-file.xlsx"  # Path to the Excel file
sheet_name = 'Sheet 1'  # Sheet name containing URLs

# Generate a descriptive output path using the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Formats the date as YYYY-MM-DD
output_path = fr"C:\Desktop\your-excel-file_with_Status_{current_date}.xlsx"  # Descriptive output file name

print("Starting script...")  # Debug print

# Load the Excel file and the specified sheet
try:
    excel_data = pd.read_excel(path, sheet_name=sheet_name)
    print(f"Excel file '{path}' loaded successfully from sheet '{sheet_name}'.")  # Debug print
except Exception as e:
    print(f"Error loading Excel file: {e}")
    exit()

# Detect columns with URLs that start with 'http' or 'https'
url_columns = [col for col in excel_data.columns if excel_data[col].astype(str).str.startswith(('http://', 'https://')).any()]

if not url_columns:
    print("No URL columns detected in the sheet.")
    exit()

print(f"Detected URL columns: {url_columns}")  # Debug print

# Check the status of URLs in each detected column
for column in url_columns:
    statuses = []
    for index, url in excel_data[column].items():
        if pd.notnull(url) and isinstance(url, str) and url.startswith(('http://', 'https://')):
            print(f"Checking URL: {url}")  # Debug print
            try:
                # Attempt a HEAD request first
                response = requests.head(url, allow_redirects=True, timeout=5)
                if response.status_code == 404:
                    # If HEAD returns 404, retry with GET to follow redirects
                    print(f"HEAD request returned 404 for {url}, retrying with GET...")
                    response = requests.get(url, allow_redirects=True, timeout=5)
                
                status = response.status_code
                print(f"Status for {url}: {status}")  # Debug print
            except requests.RequestException as e:
                status = f"Error: {e}"
                print(f"Error for {url}: {e}")  # Debug print
        else:
            status = None  # None for empty or non-URL cells
        
        # Update the status directly in the DataFrame for immediate saving
        excel_data.at[index, f'{column}_Status'] = status

        # Save progress after each URL check
        try:
            excel_data.to_excel(output_path, index=False)
            print(f"Progress saved after checking URL '{url}' to: {output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")

print("Script completed.")  # Final debug print
