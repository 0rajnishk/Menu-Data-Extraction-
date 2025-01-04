import pandas as pd

def save_to_csv(data, output_file):
    """Save extracted menu data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")
