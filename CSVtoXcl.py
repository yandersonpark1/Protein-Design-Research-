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
    
    def convert(self): 
        self.df.to_excel(self.output_file, index=False)
        print(f"Converted {self.input_file} to {self.output_file}")

def main(): 
    input_file = input("Enter the path to the CSV file: ")
    output_file = input("Enter the path to save the Excel file: ")
    converter = CSVtoXcl(input_file, output_file)
    converter.convert()
    