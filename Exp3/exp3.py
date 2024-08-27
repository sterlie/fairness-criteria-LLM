import pandas as pd
from prompts import prompts01, prompts02, correct_answer01, correct_answer02
from chat import chat
import time


gender_dict = {'M':'he', 'F':'she'}

df = pd.DataFrame(columns = ['prompt', 'gender', 'output'])


def request(df, prompt, gender, index, filename ): 
    df = pd.DataFrame(columns = ['Prompt', 'Pronoun', 'A_generated'])
    
    input = prompt.format(pronoun = gender_dict[gender]) 
    try:
        while i < index:
            output = chat(input, 'user')
            df.loc[i] = [input, gender, output]
            print('index: ' + str(i))
            i += 1
    except:
        print('Error: Limit reached at index ' + str(i))
        df.to_csv(f'{filename}.txt', sep=' ', mode='a')
        time.sleep(60) 
        request(df, prompt, gender, i, filename)
    else:
        df.to_csv(f'{filename}.txt', sep=' ', mode='a')


        
