import os
import json
import pandas as pd
import numpy as np
import re

def kaggle_auth(kaggle_json_path):
    with open(kaggle_json_path, 'r') as f:
        kaggle_pat_dict = json.load(f)

    os.putenv('KAGGLE_USERNAME', kaggle_pat_dict['username'])
    os.putenv('KAGGLE_KEY', kaggle_pat_dict['key'])

print('get_kaggle_data.py: authorizing')
kaggle_auth('/Users/brentbrewington/.kaggle/kaggle.json')

print('get_kaggle_data.py: downloading data')
os.system(f'kaggle competitions download kaggle-survey-2021 --path data/raw')

from zipfile import ZipFile

def extract_zipfile(zip_filepath, extract_output_dirpath):
# Create a ZipFile Object and load sample.zip in it
    with ZipFile(zip_filepath, 'r') as z:
       # Get a list of all archived file names from the zip
       filename_list = z.namelist()
       # Iterate over the file names
       for filename in filename_list:
           # Check filename endswith csv
           if filename.endswith('.csv'):
               # Extract a single file from zip
               z.extract(filename, extract_output_dirpath)

    print(f'  zip contents {zip_filepath} extracted to directory {extract_output_dirpath}')

print('get_kaggle_data.py: extracting zip')
extract_zipfile(zip_filepath='data/raw/kaggle-survey-2021.zip', extract_output_dirpath='data/raw')
# output file path: data/interim/kaggle_survey_2021_repsonses.csv

# Output data for parse_questions
df_raw = pd.read_csv('data/raw/kaggle_survey_2021_responses.csv', dtype='object')

df_questions = df_raw.iloc[0].to_frame().reset_index().set_axis(['question_key', 'description'], axis=1, inplace=False)

df_questions.to_csv('data/raw/questions.csv', index=False)

df_raw.drop(index=df_raw.index[0], axis=0, inplace=True)

df_raw.to_csv('data/interim/kaggle_survey_2021_responses.csv', index=False)
