import pandas as pd
import combinehbond_SASA_AF3 
import hbondCSVtoXcl
import SASA_CSVtoXcel
import CSVtoXcl

#may have error trying to convert to xcel if we are rewriting the same file
class Run_distXcel: 
    def __init__(self, file, hbond_file=None, SASA_file=None):
        self.file = file
        self.hbond_file = hbond_file
        self.SASA_file = SASA_file
        
    def run(self):
        #Run the the hbond_file to xcel conversion
        if self.hbond_file:
            self.hbond_file = hbondCSVtoXcl.convert_csvs(self.hbond_file)
        #Run the SASA_file to xcel conversion
        if self.SASA_file:
            self.SASA_file = SASA_CSVtoXcel.convert_csvs(self.SASA_file)
        #Run the combine hbond and SASA to xcel conversion
        if self.hbond_file and self.SASA_file:
            combinehbond_SASA_AF3.run(self.hbond_file, self.SASA_file)
        #Run the CSV to xcel conversion
        CSVtoXcl.run(self.file)
        self.file = 