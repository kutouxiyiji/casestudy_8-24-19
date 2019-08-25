
import numpy as np
import pandas as pd

def load_csv(path, filename):
    df = pd.read_csv(path + filename)
    return(df)

def save_csv(save_path,save_filename,df):
    df.to_csv(save_path+save_filename)
    
if __name__ == '__main__':
    path = 'C:/Users/ywu156243/Documents/Yong Wu/My Docs/my paper/'
    filename = 'TEST11111.csv'
    save_filename = 'DATA_RMA_only_clean1.csv'
    df_raw = load_csv(path, filename)
    df_RMA= pd.DataFrame()
    for i in range(len(df_raw)):
        dfrow = df_raw.iloc[i]
        row = dfrow.copy()
        if 'CRMA' not in row['Geography'] and 'SRMA' not in row['Geography'] and 'RMA' in row['Geography']:
            row['Time'] = row['Time'].strip('4 Weeks Ending ')
            if i%1000==0:
                print(row)
            df_RMA = df_RMA.append(row,ignore_index=True)
    print(len(df_RMA))
    save_csv(path, save_filename,df_RMA)