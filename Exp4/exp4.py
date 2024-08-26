from chat import chat
import pandas as pd
import time

from prompts import experiment2, female_names, male_names
 
all_names = female_names + male_names
gender = ["F"]*len(female_names) + ["M"]*len(male_names) 

df = pd.DataFrame(columns = ['Group', 'Gender', 'Answer'])
df_name = ''

def request(i):
  print("Working")
  try:
    for name in all_names[i:]:
        print("Request no.: " + str(i))
        answer = chat(name, experiment2)
        df.loc[i] = [name, gender[i], answer]
        df.to_csv(df_name, sep=' ', mode='a')
        print(answer)
        i = i + 1
  except:
    print('Error: Limit reached at request ' + str(i))
    df.to_csv(df_name, sep=' ', mode='a')
    time.sleep(60) 
    request(i)
  else:
    df.to_csv(df_name, sep=' ', mode='a')

