import pandas as pd
from supabase import create_client, Client

# Supabase credentials
url = "https://gqsobrbengdkxgfwzfcd.supabase.co"  # Replace with your Supabase URL
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imdxc29icmJlbmdka3hnZnd6ZmNkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI3MDEwNjYsImV4cCI6MjAzODI3NzA2Nn0.NkopgE1S4MIYK8ZLa_yGN09AFvZfzZJgjy2ufbP5_C8"  # Replace with your Supabase key

# Initialize Supabase client
supabase: Client = create_client(url, key)

# Read CSV file
csv_file_path = 'combined_movie_details.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path)

# Table name in Supabase
table_name = 'movies'

# Convert DataFrame to dictionary and insert into Supabase
records = df.to_dict(orient='records')

try:
    response = supabase.table(table_name).insert(records).execute()
    print("Insert response:", response.data)
except Exception as e:
    print("Error inserting records:", e)
