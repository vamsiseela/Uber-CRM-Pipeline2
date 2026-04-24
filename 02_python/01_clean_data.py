import pandas as pd
import numpy as np

df = pd.read_csv('/Users/vamsi/Desktop/uber-crm-pipeline/01_data/raw/uber_analytics_raw.csv')

df['Booking ID'] = df['Booking ID'].str.replace('"', '')
df['Customer ID'] = df['Customer ID'].astype(str).str.replace('"', '')
df['Date'] = pd.to_datetime(df['Date'])
df['Booking Value'] = df['Booking Value'].fillna(0)
df['Ride Distance'] = df['Ride Distance'].fillna(0)

reason_cols = ['Reason for cancelling by Customer', 'Driver Cancellation Reason', 'Incomplete Rides Reason']
for col in reason_cols:
    df[col] = df[col].fillna('None')

df['is_success'] = df['Booking Status'].apply(lambda x: 1 if x == 'Completed' else 0)
df['day_name'] = df['Date'].dt.day_name()
df['hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour
df['is_rush_hour'] = df['hour'].apply(lambda x: 1 if (7 <= x <= 10) or (16 <= x <= 19) else 0)

output_path = '/Users/vamsi/Desktop/uber-crm-pipeline/01_data/processed/trips_clean.csv'
df.to_csv(output_path, index=False)

print(f"Process complete. Cleaned data exported to: {output_path}")