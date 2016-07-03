# -*- coding: utf-8 -*-
"""

authors: Dawud Hage, Joost Meulenbeld, Joost Dorscheidt and Dennis van der Hoff
written for the NN course IN4015 of the TUDelft

"""

##### SETTINGS: #####
# Number of epochs to train the network over
n_epoch = 0

# Folder where the training superbatches are stored
training_folder= 'selection'
# Folder where the validation superbatches are stored
validation_folder= 'selection'

# The colorspace to run the NN in
colorspace= 'CIELab'

# Parameter folder where the parameter files are stored
param_folder = 'params_final_final'
# Parameter file to initialize the network with (do not add .npy), None for no file
param_file = 'params_fruit_Compact_more_end_fmaps_dilation_k10_T02_sigma5_nbins20_labda_03_gridsize10_epoch_25.0'
# Parameter file to save the trained parameters to every epoch (do not add .npy), None for no file
param_save_file = 'params_fruit_Compact_more_end_fmaps_dilation_k10_T02_sigma5_nbins20_labda_03_gridsize10_epoch_25.0'

# error folder where the error files are stored
error_folder = 'errors_final'
# Error file to append with the new training and validation errors (do not add .npy), None dont save
error_file = 'errors_fruit_Compact_more_end_fmaps_classifier_k10_T02_sigma5_nbins20_labda_03_gridsize10_epoch22'

# The architecture to use, can be 'Dahl' or 'Compact' or 'Compact_more_end_fmaps' or 'Dahl_classifier' or 'Dahl_Zhang' or 'Dahl_Zhang_NO_VGG16' or 'Compact_more_end_fmaps_classifier'
architecture= 'Compact_more_end_fmaps_dilation'

# Blur radius
sigma = 3;

# Turn on classification
classification=True

# Colorbin settings:
colorbins_k = 10 # k nearers neughbours
colorbins_T = 0.4 # Temperature
colorbins_sigma = 5 # K nearest neighbour sigma (blur the distance to the bin)
colorbins_nbins = 20 # Number of colorbins
colorbins_labda = 0.5 # Uniform distributie mix factor
colorbins_gridsize=10
