from scipy.io import arff
import pandas as pd
import sys

def arff_to_csv(arff_file, csv_file):
    try:
        # Load the ARFF file
        data, meta = arff.loadarff(arff_file)
        
        # Convert to a pandas DataFrame
        df = pd.DataFrame(data)
        
        # If the target attribute is in byte format, decode it
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].str.decode('utf-8')
        
        # Save to CSV
        df.to_csv(csv_file, index=False)
        print(f"Successfully converted {arff_file} to {csv_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python arff_to_csv.py <input_arff_file> <output_csv_file>")
    else:
        arff_file = sys.argv[1]
        csv_file = sys.argv[2]
        arff_to_csv(arff_file, csv_file)
