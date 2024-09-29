import pandas as pd

df = pd.read_excel('employee.xlsx')
print("Initial DataFrame:")
print(df.head())

specified_year = int(input("Enter specific year for which you want to find employees : ")) 
employees_of_year = df[df['Year'] == specified_year]

print(f"\nEmployees of the year {specified_year}:")
print(employees_of_year)
