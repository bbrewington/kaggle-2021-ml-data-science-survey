import pandas as pd
import numpy as np
import re

df = pd.read_csv('data/interim/kaggle_survey_2021_responses.csv', dtype = 'object')

df_questions = pd.read_csv('data/raw/questions.csv', dtype = 'object')

def parse_question(question_key, question_description):
    # realize this is a pretty terse regex...look at output data/.../questions.csv to see what it's doing
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
        'part': parse_results(results, 'part'),
        'description': question_description
    }

    return return_dict

print('parse_questions.py: parsing questions')
questions_parsed_list = []
for _, row in df_questions.iterrows():
    question_key = row['question_key']
    description = row['description']
    questions_parsed_list.append(parse_question(question_key, description))

questions_parsed = pd.DataFrame(questions_parsed_list)

print('parse_questions.py: writing parsed questions to data/interim/questions.csv')
questions_parsed.to_csv('data/interim/questions.csv', index=False)
