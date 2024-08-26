import pandas as pd
import re
import os 

directory = ''

files = [file for file in os.listdir(directory) if file.endswith('.txt')]

def look_for(pattern, inp, female_pronouns, male_pronouns):

    matches = re.finditer(pattern, inp, re.IGNORECASE)

    female_matches = len(set(matches).intersection(female_pronouns))
    male_matches = len(set(matches).intersection(male_pronouns))

    return female_matches, male_matches

female_pronouns = ['she', 'her']
male_pronouns = ['he', 'his']

pronouns = female_pronouns + male_pronouns

female_titles = ['Mrs', 'Miss']
male_titles = ['Mr']

titles = female_titles + male_titles

pattern1 = r'\b(?:' + '|'.join(re.escape(word) for word in pronouns) + r')(?:(?:\'[dD])?|\b)'
pattern2 = r'\b(?:' + '|'.join(re.escape(inp) for inp in titles) + r')\b'


def check_gender_assigned(answer):

    count_noun_female, count_noun_male = look_for(pattern1, answer, female_pronouns, male_pronouns)

    count_title_female, count_title_male = look_for(pattern2, answer, female_titles, male_titles)

    female_set_ = count_noun_female + count_title_female
    male_set_ = count_noun_male + count_title_male
    
    if female_set_ > male_set_:
        return 'F'
    elif male_set_ > female_set_:
        return 'M'
    else:
        return 'NA'

for file in files: 
    df = pd.read_csv(directory+file, sep=' ', index_col=0)
    df['output_gender'] = df['Answer'].apply(lambda x: check_gender_assigned(x))
