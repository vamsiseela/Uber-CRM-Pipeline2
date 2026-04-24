import pandas as pd
import sqlite3

df = pd.read_csv('/Users/vamsi/Desktop/uber-crm-pipeline/01_data/processed/trips_clean.csv')
conn = sqlite3.connect('/Users/vamsi/Desktop/uber-crm-pipeline/03_sql/uber_crm.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS dim_customers")
cursor.execute("DROP TABLE IF EXISTS dim_time")
cursor.execute("DROP TABLE IF EXISTS fact_trips")

df['Date'] = pd.to_datetime(df['Date'])

cust_dim = df[['Customer ID', 'Vehicle Type', 'Payment Method']].drop_duplicates('Customer ID')
cust_dim.columns = ['Customer_ID', 'Preferred_Vehicle', 'Preferred_Payment']
cust_dim.to_sql('dim_customers', conn, index=False, if_exists='replace')

time_dim = df[['Date', 'day_name']].drop_duplicates()
time_dim['Year'] = time_dim['Date'].dt.year
time_dim['Month'] = time_dim['Date'].dt.month
time_dim['Day'] = time_dim['Date'].dt.day
time_dim.columns = ['Date_Key', 'Day_Name', 'Year', 'Month', 'Day']
time_dim.to_sql('dim_time', conn, index=False, if_exists='replace')

fact_trips = df[['Booking ID', 'Customer ID', 'Date', 'Booking Value', 'Ride Distance', 'is_success', 'is_rush_hour', 'Customer Rating']]
fact_trips.columns = ['Booking_ID', 'Customer_ID', 'Trip_Date', 'Booking_Value', 'Ride_Distance', 'is_success', 'is_rush_hour', 'Customer_Rating']
fact_trips.to_sql('fact_trips', conn, index=False, if_exists='replace')

conn.close()
print("Database created and data loaded into Star Schema successfully.")
