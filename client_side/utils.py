import numpy as np
import pandas as pd
import librosa
import os

def extract_mfcc_features(file_name):
    '''
    Extracts mfcc features from a selected file for machine learning.

    Defaults to 20 features.
    '''
    audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate)
    mfccs_processed = np.mean(mfccs.T,axis=0)
    return mfccs_processed

def extract_mfcc_features_ds(data, samplerate):
    '''
    Extracts mfcc features from a selected file for machine learning.

    Defaults to 20 features.
    '''
    mfccs = librosa.feature.mfcc(y=data, sr=samplerate)
    mfccs_processed = np.mean(mfccs.T,axis=0)
    return mfccs_processed

def prepare_sample(mfccs_processed):
    '''
    Prepares a librosa mfcc field for sending via JSOn
    '''
    temp = []
    temp.append("value")
    temp.extend(mfccs_processed)
    return temp