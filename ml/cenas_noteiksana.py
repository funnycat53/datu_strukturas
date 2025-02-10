import pandas as pd
from sklearn.linear_model import LinearRegression
import re

CSV_FILE = "ml/dati/sslv.csv"

def clean_value(value):
    """
    Since the scraped CSV stores some fields as list-like strings (for example "[' 2010']"),
    we extract the first numeric part.
    """
    # If the value is a string representing a list, remove brackets and quotes.
    # Then use regex to extract the number.
    if isinstance(value, str):
        # Remove brackets and quotes if present
        value = re.sub(r"[\[\]']", "", value)
    match = re.search(r"[\d\.]+", value)
    if match:
        return match.group(0)
    return None

def load_and_clean_data(csv_file):
    # Read CSV file. Depending on how the data was written, you might need to adjust parameters.
    df = pd.read_csv(csv_file, encoding="utf-8")
    
    # Clean the columns we need. They might be stored as string representations of lists.
    # We assume that each cell contains something like: "['123456']" or "['2010']"
    for col in ['nobraukums', 'gads', 'tilpums', 'cena']:
        df[col] = df[col].apply(lambda x: clean_value(str(x)))
    
    # Convert columns to numeric types. Use errors='coerce' to set problematic values to NaN.
    df['nobraukums'] = pd.to_numeric(df['nobraukums'], errors='coerce')
    df['gads'] = pd.to_numeric(df['gads'], errors='coerce')
    df['tilpums'] = pd.to_numeric(df['tilpums'], errors='coerce')
    df['cena'] = pd.to_numeric(df['cena'], errors='coerce')
    
    # Drop rows with any missing values in the columns of interest.
    df = df.dropna(subset=['nobraukums', 'gads', 'tilpums', 'cena'])
    
    return df

def train_price_model(csv_file):
    df = load_and_clean_data(csv_file)
    
    # Define X (features) and y (target price)
    X = df[['nobraukums', 'gads', 'tilpums']]
    y = df['cena']
    
    # Create and train a linear regression model
    model = LinearRegression()
    model.fit(X, y)
    return model

# Train the model (this may take a moment, depending on your data size)
price_model = train_price_model(CSV_FILE)

def predict_price(mileage, year, engine_volume):
    """
    Given a car's mileage (nobraukums), year (gads), and engine volume (tilpums),
    predicts the price based on the linear regression model trained from the scraped data.
    
    Parameters:
      - mileage: int or float, the car's mileage (for example in km)
      - year: int, the production year of the car
      - engine_volume: float, the engine volume (for example in liters)
      
    Returns:
      - predicted_price: float, the estimated price
    """
    # Arrange input in the same order as the model expects
    X_new = [[mileage, year, engine_volume]]
    predicted_price = price_model.predict(X_new)[0]
    return predicted_price

# Example usage:
if __name__ == "__main__":
    # Example car: 150,000 km mileage, produced in 2010, engine volume 1.8 L
    mileage_example = 220000
    year_example = 2001
    engine_volume_example = 2
    
    price_estimate = predict_price(mileage_example, year_example, engine_volume_example)
    print(f"Predicted price for a car with {mileage_example} km, year {year_example}, and {engine_volume_example}L engine: {price_estimate:.2f} EUR")
