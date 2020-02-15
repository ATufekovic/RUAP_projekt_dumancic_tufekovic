import numpy as np
import pandas as pd
import librosa
import os

def extract_mfcc_features(file_name):
    '''
    Extracts mfcc features from a selected file for machine learning.

    Extracts 20 features.
    '''
    audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate)
    mfccs_processed = np.mean(mfccs.T,axis=0)
    return mfccs_processed

features = [] # Iterate through each sound file and extract the features
directory = "D:/Fakultetlije/semestar_dipl_1/ruap/projekt/RUAP_projekt_dumancic_tufekovic/RUAP_projekt_dumancic_tufekovic/cats_dogs"
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        class_label = filename.split("_")[0]
        data = extract_mfcc_features(os.path.abspath(directory+"/"+filename)) #bad practice but it solved some errors
        temp = [class_label]
        temp.extend(data)
        features.append(temp)
        #print(temp, "\n")

for feat in features:
    print(feat)

features_df = pd.DataFrame(features, columns=['class_label','feature0','feature1','feature2','feature3','feature4','feature5','feature6','feature7','feature8','feature9','feature10','feature11','feature12','feature13','feature14','feature15','feature16','feature17','feature18','feature19'])
print(features_df)
features_df.to_csv("cat_dog_dataset.csv",index=False)