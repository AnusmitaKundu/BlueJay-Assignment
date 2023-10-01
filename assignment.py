import pandas as pd

excel_file_path = 'Assignment_Timecard.xlsx'  
df = pd.read_excel(excel_file_path)

#To print the name of employees who worked for consecutive 7 days
df['Time in'] = pd.to_datetime(df['Time'])
df['Time out'] = pd.to_datetime(df['Time Out'])
df.sort_values(by=['Employee Name', 'Time in'], inplace=True)
consecutive_days_counts = df.groupby('Employee Name')['Time in'].diff().dt.days.fillna(0).eq(1).groupby(df['Employee Name']).cumsum() + 1

employees_worked_7_consecutive_days = df[consecutive_days_counts == 7][['Employee Name', 'Position ID']].drop_duplicates()

print("Employees who worked for 7 consecutive days:")
print(employees_worked_7_consecutive_days)



#To print the name of employees who worked less than 10 hours but more than 1 hour
df['Work duration'] = (df['Time out'] - df['Time in']).dt.total_seconds() / 3600
employees_less_than_10_hours_between_shifts = df[(df['Work duration'] < 10.0) & (df['Work duration'] > 1.0)][['Employee Name', 'Position ID']].drop_duplicates()

print("\nEmployees who worked less than 10 hours between shifts but more than 1 hour:")
print(employees_less_than_10_hours_between_shifts)



#To print the name of employees who worked more than 14 hours in a single shift
employees_more_than_14_hours_in_single_shift = df[df['Work duration'] > 14.0][['Employee Name', 'Position ID']].drop_duplicates()

print("\nEmployees who worked more than 14 hours in a single shift:")
print(employees_more_than_14_hours_in_single_shift)
