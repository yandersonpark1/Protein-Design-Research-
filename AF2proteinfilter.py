

class AF2proteinfilter: 
    def __init__(self, af2protein): 
        self.af2protein = af2protein
    
    def plDDT(): 
        """
        plDDT is a measure of the local distance difference test, which is a metric for the quality of protein structure predictions.
        > 90 is considered high confidence with confidence in backbone and side chains, 
        70-90 is medium confidence with confidence in backbone but maybe not the greatest confidence in the sidechains, 
        and < 70 is low confidence with possible disordered regions or low confidence in the structure. 
        For the purpose of this filter, and N terminal residue protein binders, we will only need to consider the plDDT of chain x
        where x is the chain of the protein binder.
        """
        



def main(): 
    """
    Main function to test the AF2proteinfilter class
    Run an excel file with proteins
    """""