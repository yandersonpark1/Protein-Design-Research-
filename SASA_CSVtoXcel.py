import pandas as pd
import os

class SASA_CSVtoXcl: 
    def __init__(self, input_file, output_file): 
        """
        CSVtoXcl classs to convert a CSV file to an Excel file.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.df = pd.read_csv(input_file, skiprows = 0)
        self.columns = ['B1 total SASA', 'b1 bb', 'b1 sc'] #, 'B2 total SASA', 'b2 bb', 'b2 sc', 'B3 total SASA', 'b3 bb', 'b3 sc']
    
    def convert(self): 
        self.df = self.df.iloc[:, 3:6]  
        self.df.columns = self.columns
        self.df.to_excel(self.output_file, index=False)
        print(f"Converted {self.input_file} to {self.output_file}")

def convert_csvs(input_file):
    output_path = (input_file.removesuffix('.csv') + '.xlsx')
    converter = SASA_CSVtoXcl(input_file, output_path)
    converter.convert()
         
def main(): 
    input_file = input("Enter the name of the CSV file to convert (e.g., 'data.csv'): ")
    convert_csvs(input_file)
    
if __name__ == "__main__":
    main()