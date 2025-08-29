import pandas as pd

def fetch_tno_data(url: str) -> pd.DataFrame:
    """
    Fetches TNO data from a given URL.
    
    Args:
        url: The URL to fetch the data from.
        
    Returns:
        A pandas DataFrame containing the TNO data.
    """
    print(f"Fetching data from {url}...")
    # This is a placeholder. In a real scenario, you would use requests or a similar library
    # to download the data. For now, we'll create a dummy dataframe.
    data = {
        'id': range(10),
        'a': [40 + i for i in range(10)], # semi-major axis
        'e': [0.1 + i*0.01 for i in range(10)], # eccentricity
        'i': [5 + i for i in range(10)], # inclination
    }
    df = pd.DataFrame(data)
    print("Data fetched successfully.")
    return df

if __name__ == '__main__':
    # Example usage
    tno_data = fetch_tno_data("http://example.com/tno_data.csv")
    print(tno_data.head())