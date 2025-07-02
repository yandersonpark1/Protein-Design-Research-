import pandas as pd

#Possible things to consider for the AF2proteinfilter class:
# - plDDT: per chain, average, and per residue if 70-90 possible to recycle 
class LMPNN_dist_Af3proteinfilter(): 
    """
    AF2proteinfilter class to filter AlphaFold protein predictions based on metrics [plDDT, pTM, iPTM, PAE/Contact, hbonding, SASA]
    """
    
    def __init__(self, input_file): 
        ''' Change depending on the input file format '''
        self.df = pd.read_excel(input_file, header=0, usecols=['diff', 'bb', 'seq #', 'plDDT', 'plDDT A', 'plDDT B', 'pTM', 'ipTM', 'evo pro', 'ctct score', '# ctct', 'PAE/ ctct', '# ctct@residue', 'PAE/ ctct@residue','ctct score@residue', 'hbond count', 'hbond b1', 'hbond b2', 'hbond b3', 'B1 total SASA', 'b1 bb', 'b1 sc', 'B2 total SASA', 'b2 bb', 'b2 sc', 'B3 total SASA', 'b3 bb', 'b3 sc'])
        self.filtered_df = self.df.copy()
    
    def plDDT(self, min_plDDT = 89.5, column = "plDDT A"): 
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
        self.filtered_df = self.filtered_df[self.filtered_df[column] > min_plDDT]
        
        
    
    def pTM(self, min_pTM = 0.5, column = "pTM"): 
        """
        pTM is the predicted template modeling score, which is a measure of the quality of protein structure predictions.
        Checks if all chains are corretly folded and positioned globally. In this case, we would want to consider iPTM a little bit more
        because we would have to consider the global structure of the protein binder and the N terminal residue (ligand) and their
        relative positions based on their possible interactions. 
        In general though, we want a pTM score above .5. Anything else is considered low confidence and likely a failed prediction.
        """
        self.filtered_df = self.filtered_df[self.filtered_df[column] > min_pTM]
    
    def ipTM(self, min_ipTM = 0.6, column = "ipTM"): 
        """
        ipTM measures relative accuracy of predicted position of subunits forming protein-protein complexes.
        > 0.8 is confident in a high quality prediction,
        < 0.6 is low confidence in the prediction and likely failed prediction. 
        You could recycle the predictions until a degree of convergence is reached (Maybe a good protein binder should be individually
        recycled until convergence is reached and then compare back to filter)
        Metric is somewhat correlated to plDDT y, and therfore takes it place
        Ideally at end we have greater than or equal to 0.8 but for initial filtering, we will consider 0.6 as the minimum.
        """
        self.filtered_df = self.filtered_df[self.filtered_df[column] > min_ipTM]
    
    def PAEperContact(self, max_PAE_per_contact = 10, column = "PAE/ ctct"): 
        """
        PAE is the predicted aligned error, which is a measure of the uncertainty in the predicted structure.  
        Considers the total number of contacts between the two chains (more contacts means possibly more stable interface) 
        as well as contact score (accuracy and strength of the contact).
        PAE/Contact looks at the expected uncertainity 
        For the purpose of this filter, we will consider the PAE/Contact of chain x relative to y
        where x is the chain of the protein binder and y is the N terminal residue (ligand).
        We want a lower score meaning that there is less uncertainty in the predicted structure where contact between the residues
        of chain x and chain y is considered.
        We want to be less than 5 because around 5 is max angstroms for a non covalent interaction to be considered a contact.
        Note: does not consider the whole domain of chain x and chain y, but rather the contact between the two residues of the chain.
        """
        self.filtered_df = self.filtered_df[self.filtered_df[column] < max_PAE_per_contact]
        
    def hbonding(self, min_hbonds = 2, column = "hbond b1"): 
        #may want to consider number of h bonds that should not be formed on [b2:] 
        """
        We want to look at the number of hydrogen bonds between the n terminal residue and the protein binder. One thing to consider
        is we do not want a lot of hydorgen bonds between the whole chain of the ligand because that might imply that the ligand will not 
        only be binded by N terminal residue, but also by other residues in the chain. In this case, for tyrosine, we want two hydrogen bonds to form 
        off the oxyegn on the side chain and possibly three hydrogen bonds to form off the Nitrogen on the amine group. 
        While we may not be able to configure the hydrogen bonds (we could but would need to implmemnt a graph algorithm) we could 
        say that there should be at least two hydorgen bonds off the b1 residue of the ligand in the case of tyrosine. 
        min_hbonds is an integer representing the minimum number of hydrogen bonds that should be formed between the n terminal residue 
        and the protein binder where you can find the min by taking the number of polar atoms on the n terminal residue that may form 
        h bonds. 
        """
        
        self.filtered_df = self.filtered_df[self.filtered_df[column] >= min_hbonds]
        
    
    
    def SASA(self, max_SASA_b1 = 100, column = "B1 total SASA"): 
        """
        SASA is the solvent accessible surface area, which is a measure of the surface area of a protein that is accessible to solvent.
        In our case, the Solvent is water as we have soluble proteins. We want to consider the SASA of the N terminal residue (ligand) and the protein binder. 
        If the SASA of the N terminal residue is too high, it may indicate that the ligand is exposed and not properly binded and concealed.
        If the SASA of the protein binder is too low, it may indicate that the binder has completely binded to more than just the N terminal residue.
        However, a low SASA is still good but should not be considered for final product. A good way to consider this would be 
        the b2 to bn side chain where n represents the last number of the residue on the sidechain.
        """
        self.filtered_df = self.filtered_df[self.filtered_df[column] <= max_SASA_b1]
        
        # Find all SASA columns except original column
        SASA_cols = set()
        SASA_cols = [col for col in self.filtered_df.columns if ("sc" in col) and (col != "B1 sc")]

        # Create a mask: True if any other hbonding column > reference column
        mask = (self.filtered_df[SASA_cols] < 30).all(axis=1)

        # Keep only rows where no other hbonding column exceeds the reference
        self.filtered_df = self.filtered_df[~mask]
        
    def save_filtered_data(self, version):
        """
        Save the filtered DataFrame to an Excel file.
        """
        output_file=f"lMPNN_dist_v{version}filtered_protein_predictions.xlsx"
        self.filtered_df.to_excel((output_file), index=False)
        print(f"Filtered data saved to {output_file}")
    



def main(): 
    """
    Main function to test the AF2proteinfilter class
    Reads Excel Sheet with AlphaFold protein predictions
    """""
    file = input(str("Enter the path to the Excel file with AlphaFold protein predictions: "))
    version = int(input(("Enter the version of the LMPNN_dist you are using (e.g., 1, 2, 3): ")))
    df = pd.read_excel(file)
    print(df.columns)
    filter_data = LMPNN_dist_Af3proteinfilter(file)
    filter_data.plDDT()
    filter_data.pTM()
    filter_data.ipTM()
    filter_data.PAEperContact()
    filter_data.hbonding()
    filter_data.SASA()
    filter_data.save_filtered_data(version)

if __name__ == "__main__":
    main()
    