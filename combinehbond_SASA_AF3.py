import pandas as pd
class combinehbond_SASA_AF3: 
    """
    Class to combine hbonding and SASA metrics for AlphaFold protein predictions.
    """
    
    def __init__(self, hbond_file, SASA_file, AF3_file): 
        ''' Change depending on the input file format '''
        self.hbond_df = pd.read_excel(hbond_file, header=0, usecols=['hbond count', 'hbond b1', 'hbond b2', 'hbond b3'])
        self.SASA_file = pd.read_excel(SASA_file, header=0, usecols=['B1 total SASA', 'b1 bb', 'b1 sc', 'B2 total SASA', 'b2 bb', 'b2 sc', 'B3 total SASA', 'b3 bb', 'b3 sc'])
        '''for non parsing use: ['diff', 'bb', 'seq #', 'seq', 'plDDT', 'plDDT A', 'plDDT B', 'pTM', 'ipTM', 'evo pro', 'ctct score', '# ctct', 'PAE/ ctct']'''
        self.Af3_file = pd.read_excel(hbond_file, header=0, usecols=['diff', 'bb', 'seq #', 'seq', 'plDDT', 'plDDT A', 'plDDT B', 'pTM', 'ipTM', 'evo pro', 'ctct score', '# ctct', 'PAE/ ctct'])
    
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