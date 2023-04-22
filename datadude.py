import pandas as pd

def filter():
    csv_loc = 'Streymendur/Streymendur/tilraun2.csv'
    df = pd.read_csv(csv_loc) #http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
    #pd.da
    resdf = df[df['Tags'].str.contains('|'.join(['islenskt', 'icelandic', 'iceland']), na=False, case=False)]
    resdf = resdf.set_index('User Id')
    #resdf = resdf.reset_index(drop=True)
    resdf.to_csv('Streymendur/Streymendur/Users.csv', mode='a', header=False )
    users = pd.read_csv('Streymendur/Streymendur/Users.csv')
    users = users.drop_duplicates(subset='User Name')
    

if __name__ == '__main__':
	filter()
