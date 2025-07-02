import pandas as pd
class combinehbond_SASA_AF3: 
    """
    Class to combine hbonding and SASA metrics for AlphaFold protein predictions.
    """
    
    def __init__(self, input_file): 
        ''' Change depending on the input file format '''
        self.df = pd.read_excel(input_file, header=0, usecols=['diff', 'bb', 'seq #', 'plDDT', 'pTM', 'ipTM', 'hbonding', 'SASA'])
        self.filtered_df = self.df.copy()
    
    def hbonding(self, min_hbonding = 2, column = "hbonding"): 
        """
        Filter based on the number of hydrogen bonds.
        A minimum of 2 hydrogen bonds is considered a good indicator of stability.
        """
        self.filtered_df = self.filtered_df[self.filtered_df[column] >= min_hbonding]
    
    def SASA(self, max_SASA = 1000, column = "SASA"): 
        """
        Filter based on Solvent Accessible Surface Area (SASA).
        A maximum value indicates a compact structure; values above this may indicate potential issues.
        """
        self.filtered_df = self.filtered_df[self.filtered_df[column] <= max_SASA]