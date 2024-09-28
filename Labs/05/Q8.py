import re

text = """
Today's date is 28/09/2024. Tomorrow's date will be 30/09/2024.
Yesterday's date was Sep 27, 2024. Another important date is 2024-09-26.
"""

date_pattern = r'(\b\d{2}/\d{2}/\d{4}\b)|(\b\d{4}-\d{2}-\d{2}\b)|(\b[A-Za-z]{3} \d{1,2}, \d{4}\b)'

# (\b\d{2}/\d{2}/\d{4}\b): DD/MM/YYYY.
# (\b\d{4}-\d{2}-\d{2}\b): YYYY-MM-DD.
# (\b[A-Za-z]{3} \d{1,2}, \d{4}\b): Mon DD, YYYY

dates = re.findall(date_pattern, text)
extracted_dates = [date for match in dates for date in match if date]
print(extracted_dates)
