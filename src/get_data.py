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

print('get_data.py: authorizing')
kaggle_auth('/Users/brentbrewington/.kaggle/kaggle.json')

print('get_data.py: downloading data')
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

print('get_data.py: extracting zip')
extract_zipfile(zip_filepath='data/raw/kaggle-survey-2021.zip', extract_output_dirpath='data/interim')
# output file path: data/interim/kaggle_survey_2021_repsonses.csv

df = pd.read_csv('data/interim/kaggle_survey_2021_responses.csv', dtype = 'object')

questions = df.iloc[0].to_dict()

def parse_question(question_key):
    pattern = "^Q(?P<id>\d+)((_(?P<id_sub>[A-Z]))?_(Part_)?(?P<part>(\d+|OTHER)))?$"
    results = re.match(pattern, question_key)

    def parse_results(results, key):
        if results is not None:
            results_value = results.group(key)
            return_val = results_value if results_value is not None else ''
            return return_val
        else:
            return np.NaN

    return_dict = {
        'question_key': question_key,
        'id': parse_results(results, 'id'),
        'id_sub': parse_results(results, 'id_sub'),
        'part': parse_results(results, 'part')
    }

    return return_dict

print('get_data.py: parsing questions')
questions_parsed_list = []
for q in questions:
    questions_parsed_list.append(parse_question(q))

questions_parsed = pd.DataFrame(questions_parsed_list)

print('get_data.py: writing parsed questions to data/interim/questions.csv')
questions_parsed.to_csv('data/interim/questions.csv', index=False)
