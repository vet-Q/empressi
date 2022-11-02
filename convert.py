import pandas as pd

df = pd.read_csv(r"C:\Users\kwono\Desktop\asfv1.csv")

def makedate(x):
    if len(x)==6:
        date=x.split('/')
        date.insert(1,'/0')
        final_string=''.join(date)
    else: final_string=x
    return final_string

df['time']=df['time'].apply(lambda x:makedate(x))


df.to_csv('./asfv_mod.csv')       
