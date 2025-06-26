import pandas as pd
import os

class CSVtoXcl: 
    def __init__(self, input_file, output_file): 
        """
        CSVtoXcl classs to convert a CSV file to an Excel file.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.df = pd.read_csv(input_file)
        self.columns = ['plDDT', 'plDDT A', 'plDDT B', 'pTM', 'ipTM', 'evo pro', 'ctct score', '# ctct', 'PAE/ ctct']
    
    def convert(self): 
        self.df.columns = self.columns
        self.df.to_excel(self.output_file, index=False)
        print(f"Converted {self.input_file} to {self.output_file}")

def convert_csvs_in_folder(input_file, folder_path = '/Tyr_ClpS_250624/V7'):
    # List all files in the folder
    for filename in os.listdir(folder_path):
        if filename == input_file:
            input_path = os.path.join(folder_path, filename)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(folder_path, base_name + '.xlsx')
            
            converter = CSVtoXcl(input_file, output_path)
            converter.convert()
         
def main(): 
    input_file = input("Enter the name of the CSV file to convert (e.g., 'data.csv'): ")
    convert_csvs_in_folder(input_file)
    
if __name__ == "__main__":
    main()
    