from chat import chat2
import pandas as pd 
import time
from prompts import baseline_prompt, prompt


questions = pd.read_csv('MEDQA.txt', sep=',, ', index_col=None, header=None, engine='python')

answer_dict = {'A':'B', 'B':'C', 'D':'A', 'C':'B'}
identifier_dict = {'M':'he', 'F':'she'}


df = pd.DataFrame(col = ['mcq_no', 'gender', 'ground_truth', 'correct_answer', 'output'])
df_base = pd.DataFrame(columns = ['mcq_no', 'ground_truth', 'output'])


def request(ground_truth, gender_var, df, prompt, file_out):
    if ground_truth:
        gt = 'nurse'
    else: 
        gt = 'doctor'

    for i in range(14):
        mcq = str(questions.iloc[i][0]) + str(questions.iloc[i][1])
        correct_answer = str(questions.iloc[i][2])
   
        request = prompt.format(not_correct=answer_dict[correct_answer], correct=correct_answer, pronoun = identifier_dict[gender_var])
        input = mcq + request
        output = chat2(input, 'user')

        df.loc[i] = [i, gender_var , gt, correct_answer, output]

    df.to_csv(f'{file_out}.txt', sep=' ', mode='a', index_label=False)



def baseline(file_out):
    for i in range(14):
        mcq = str(questions.iloc[i][0]) + str(questions.iloc[i][1])
        inp = mcq + baseline_prompt
        correct_answer = questions.iloc[i][2]

        output = chat2(inp, 'user')

        df_base.loc[i] = [i, correct_answer, output]

    df_base.to_csv(f'{file_out}.txt', sep=' ', mode='a', index_label=False)

