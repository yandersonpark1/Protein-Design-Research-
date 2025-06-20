
#Possible things to consider for the AF2proteinfilter class:
# - plDDT: per chain, average, and per residue if 70-90 possible to recycle 
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
        where x is the chain of the protein binder. Our plDDT y where y is the N terminal residue (ligand) is not considered 
        as it is not a protein binder we are creating. Our plDDT All is the average of all chains in the protein,
        which should not be used as plDDT y is also considered in the calculation of the average.
        """
    
    
    def ipTM(): 
        """
        ipTM measures relative accuracy of predicted position of subunits forming protein-protein complexes.
        > 0.8 is confident in a high quality prediction,
        < 0.6 is low confidence in the prediction and likely failed prediction. 
        You could recycle the predictions until a degree of convergence is reached (Maybe a good protein binder should be individually
        recycled until convergence is reached and then compare back to filter)
        Metric is somewhat correlated to plDDT y, and therfore takes it place
        """
        
    
    def PAEperContact(): 
        """
        PAE is the predicted aligned error, which is a measure of the uncertainty in the predicted structure.  
        Considers the total number of contacts between the two chains (more contacts means possibly more stable interface) 
        as well as contact score (accuracy and strength of the contact).
        PAE/Contact looks at the expected uncertainity 
        For the purpose of this filter, we will consider the PAE/Contact of chain x relative to y
        where x is the chain of the protein binder and y is the N terminal residue (ligand).
        We want a lower score meaning that there is less uncertainty in the predicted structure where contact between the residues
        of chain x and chain y is considered.
        Note: does not consider the whole domain of chain x and chain y, but rather the contact between the two residues of the chain.
        """
        
    



def main(): 
    """
    Main function to test the AF2proteinfilter class
    Run an excel file with proteins
    """""