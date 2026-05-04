import pandas as pd
# dataSeties = pd.Series([1, 3, 5, 7, 9])
# dataFrame = {
#     'Name': ['John', 'Anna', 'Peter', 'Linda'],
#     'Age': [28, 34, 29, 32],
#     'City': ['New York', 'Paris', 'Berlin', 'London']
# }
# df = pd.DataFrame(dataFrame)

df = pd.read_csv('/Users/evgeniakolesnikova/Library/Mobile Documents/com~apple~CloudDocs/ai_data_analysis_lab/Lessons/Data_Analysis.py')
df.head()  # Displays the first 5 rows by default