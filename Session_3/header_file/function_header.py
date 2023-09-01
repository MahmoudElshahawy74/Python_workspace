import re
from openpyxl import Workbook

# Define a regular expression pattern to match C function prototypes
function_pattern = re.compile(r'\w+\s+\w+\([^)]*\);')

# Specify the header file you want to parse
header_file = 'header.h'  # Replace with your header file

# Open the header file and read its contents
with open(header_file, 'r') as file:
    header_content = file.read()

# Find all function prototypes in the header content
function_prototypes = function_pattern.findall(header_content)

# Create a new Excel workbook
wb = Workbook()

# Select the active sheet (first sheet)
sheet = wb.active

# Insert function prototypes into the Excel sheet with unique IDs
unique_id = 0
for prototype in function_prototypes:
    unique_id += 1
    sheet[f'A{unique_id}'] = f'IDX{unique_id}'  # Unique ID
    sheet[f'B{unique_id}'] = prototype  # Function prototype

# Save the Excel workbook
excel_file = 'function_prototypes.xlsx'
wb.save(excel_file)

print(f'Function prototypes saved to {excel_file}')
