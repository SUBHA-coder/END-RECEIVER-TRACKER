import pandas as pd

def load_data(file_path):
    """Loads and preprocesses the data from the CSV file."""
    df = pd.read_csv(file_path)
    return df

# Example usage
if __name__ == "__main__":
    data_file = 'ETHlabel.csv'
    df = load_data(data_file)
    print(df.head())  # Preview the first few rows of the data
