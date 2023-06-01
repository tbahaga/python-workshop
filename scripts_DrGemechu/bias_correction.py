
#The second NMA training
#prepared by Gemechu Fanta (PhD)

from bias_correction import BiasCorrection
#Instantiate the bias correction class as:
bc = BiasCorrection(reference, model, data_to_be_corrected)
#Perform correction specifying the method to be used:
#Gamma and normal correction
corrected = bc.correct(method='gamma_mapping')
#modified quantile
corrected = bc.correct(method='modified quantile')

