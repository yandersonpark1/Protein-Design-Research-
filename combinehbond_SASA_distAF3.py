
import pandas as pd
class combinehbond_SASA_distAF3: 
    """
    Class to combine hbonding and SASA metrics for AlphaFold protein predictions.
    """
    
    def __init__(self, AF3_file, hbond_file, SASA_file): 
        ''' Change depending on the input file format '''
        self.hbond_df = pd.read_excel(hbond_file, header = 0, usecols=['hbond count', 'hbond b1', 'hbond b2', 'hbond b3'])
        self.SASA_file = pd.read_excel(SASA_file, header = 0, usecols=['B1 total SASA', 'b1 bb', 'b1 sc']) #, 'B2 total SASA', 'b2 bb', 'b2 sc', 'B3 total SASA', 'b3 bb', 'b3 sc'])
        self.AF3_file = pd.read_excel(AF3_file, header = 0, usecols=['diff', 'bb', 'seq #', 'seq name', 'plDDT', 'plDDT A', 'plDDT B', 'pTM', 'ipTM', 'evo pro', 'ctct score', '# ctct', 'PAE/ ctct', '# ctct@residue', 'PAE/ ctct@residue','ctct score@residue'])
    
    def combine(self, version, scaffold): 
        combined = pd.concat([self.AF3_file, self.hbond_df, self.SASA_file], axis=1)
        combined.to_excel(f'{version}_{scaffold}_dist_metrics.xlsx', index=False)
    

def main():
    AF3_file = input("Enter the name of the AF3 Xcl file: ")
    hbond_file = input("Enter the name of the hbond Xcl file: ")
    SASA_file = input("Enter the name of the SASA Xcl file: ")
    version = input("Enter the version for the output file (e.g., '1'): ")
    scaffold = input("Enter the scaffold name (e.g., 'ClpS'): ")
    
    combiner = combinehbond_SASA_distAF3(AF3_file, hbond_file, SASA_file)
    combiner.combine(version, scaffold)

if __name__ == "__main__":
    main()