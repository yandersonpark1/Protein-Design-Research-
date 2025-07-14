import pandas as pd
import os

class CSVtoXcl: 
    def __init__(self, input_file, output_file): 
        """
        CSVtoXcl classs to convert a CSV file to an Excel file.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.df = pd.read_csv(input_file, skiprows = 0)
        self.columns = ['diff', 'redesign', 'seq #', 'seq name', 'ligand', 'plDDT', 'plDDT A', 'plDDT B', 'pTM', 'ipTM', 'evo pro', 'ctct score', '# ctct', 'PAE/ ctct', '# ctct@residue', 'PAE/ ctct@residue','ctct score@residue']
    
    def convert(self): 
        self.df.columns = self.columns
        self.df.to_excel(self.output_file, index=False)
        print(f"Converted {self.input_file} to {self.output_file}")

def convert_csvs(input_file):
    output_path = (input_file.removesuffix('.csv') + '.xlsx')
    converter = CSVtoXcl(input_file, output_path)
    converter.convert()
         
def main(): 
    input_file = input("Enter the name of the CSV file to convert (e.g., 'data.csv'): ")
    convert_csvs(input_file)
    
if __name__ == "__main__":
    main()
    