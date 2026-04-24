-- Create Dimension Tables
CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id TEXT PRIMARY KEY,
    preferred_vehicle_type TEXT
);

CREATE TABLE IF NOT EXISTS dim_time (
    time_id INTEGER PRIMARY KEY AUTOINCREMENT,
    raw_timestamp TEXT,
    hour INTEGER,
    day_name TEXT,
    is_rush_hour INTEGER
);

-- Create Fact Table
CREATE TABLE IF NOT EXISTS fact_trips (
    trip_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id TEXT,
    time_id INTEGER,
    booking_value REAL,
    ride_distance REAL,
    is_success INTEGER,
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id)
);