# Import Pandas
import pandas as pd

# Import excel file
xlsx = pd.ExcelFile('hash-analytic-project-2.xlsx')

# Extract all 10 sheets into DataFrames
df1 = pd.read_excel(xlsx, 'Sheet1')
df2 = pd.read_excel(xlsx, 'Sheet2')
df3 = pd.read_excel(xlsx, 'Sheet3')
df4 = pd.read_excel(xlsx, 'Sheet4')
df5 = pd.read_excel(xlsx, 'Sheet5')
df6 = pd.read_excel(xlsx, 'Sheet6')
df7 = pd.read_excel(xlsx, 'Sheet7')
df8 = pd.read_excel(xlsx, 'Sheet8')
df9 = pd.read_excel(xlsx, 'Sheet9')
df10 = pd.read_excel(xlsx, 'Sheet10')

# Export DataFrames to csv files
df1.to_csv('df1.csv', encoding='utf-8')
df2.to_csv('df2.csv', encoding='utf-8')
df3.to_csv('df3.csv', encoding='utf-8')
df4.to_csv('df4.csv', encoding='utf-8')
df5.to_csv('df5.csv', encoding='utf-8')
df6.to_csv('df6.csv', encoding='utf-8')
df7.to_csv('df7.csv', encoding='utf-8')
df8.to_csv('df8.csv', encoding='utf-8')
df9.to_csv('df9.csv', encoding='utf-8')
df10.to_csv('df10.csv', encoding='utf-8')
