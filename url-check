import pandas as pd
import requests
import datetime

# Hard-coded list of URLs to check
urls = [
    "https://www.manzill.com",
    "https://www.example.com",
   ]

# Generate a descriptive output path using the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
output_path = fr"C:\Users\manzill.surolia\Desktop\linkcheck\hardcoded_links_with_Status_{current_date}.xlsx"

print("Starting URL status check script...")

# Data structure to store URLs and their statuses
url_data = {"URL": [], "Status": []}

# Check the status of each URL
for url in urls:
    print(f"Checking URL: {url}")
    try:
        # Attempt a HEAD request first
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code == 404:
            # Retry with GET if HEAD returns 404
            print(f"HEAD request returned 404 for {url}, retrying with GET...")
            response = requests.get(url, allow_redirects=True, timeout=5)

        # Store the URL and its status
        url_data["URL"].append(url)
        url_data["Status"].append(response.status_code)
        print(f"Status for {url}: {response.status_code}")
    except requests.RequestException as e:
        # Handle any exceptions (e.g., timeout, connection errors)
        url_data["URL"].append(url)
        url_data["Status"].append(f"Error: {e}")
        print(f"Error for {url}: {e}")

# Convert the data to a DataFrame and save it to an Excel file
url_df = pd.DataFrame(url_data)
try:
    url_df.to_excel(output_path, index=False)
    print(f"URL statuses saved to: {output_path}")
except Exception as e:
    print(f"Error saving file: {e}")

print("Script completed.")
