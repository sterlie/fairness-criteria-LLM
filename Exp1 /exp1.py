from chat import chat
from prompts import occupations1, occupations2
from prompts import experiment1
import pandas as pd
import time

df_name = ''
df = pd.DataFrame(columns = ['proffesion', 'gender', 'output'])

gender = ["F"]*len(occupations1) + ["M"]*len(occupations2)

proffesions_comb = occupations1 + occupations2

def request(i):
  print("Connecting")
  try:
    for prof in proffesions_comb[i:]:
        answer = chat(prof, experiment1)
        df.loc[i] = [prof, gender[i], answer]
        print(answer)
        i = i + 1
  except:
    print('Error: Limit reached at index ' + str(i))
    df.to_csv(df_name, sep=' ', mode='a')
    time.sleep(60) 
    request(i)
  else:
    df.to_csv(df_name, sep=' ', mode='a')

