import base64
import os

# Path of the CSV file
csv_path = 'discount_ebook_template.csv'

# Read the CSV file in binary mode
with open(csv_path, 'rb') as csv_file:
    csv_content = csv_file.read()

# Encode the CSV content to base64
csv_base64 = base64.b64encode(csv_content)

# Convert to string and prepend with the necessary prefix
csv_data_uri = 'data:text/csv;base64,' + csv_base64.decode('utf-8')

print(csv_data_uri)

# running >> python3 convert_to_base64.py