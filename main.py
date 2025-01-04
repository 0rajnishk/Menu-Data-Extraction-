from processor import process_files
from utils import save_to_csv

def main():
    input_directory = "./data"  # Folder containing menu files
    output_file = "menu_data.csv"

    # Process files and extract menu data
    menu_data = process_files(input_directory)

    # Save the extracted data to a CSV file
    save_to_csv(menu_data, output_file)
    print(f"Menu data saved to {output_file}")

if __name__ == "__main__":
    main()
