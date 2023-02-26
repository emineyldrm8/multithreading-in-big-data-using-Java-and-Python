import pandas as pd
import csv
import string
from nltk.corpus import stopwords
stop = stopwords.words('english')
dataframe=pd.read_csv('rows.csv',low_memory=False)#veri setini okutma işlemi
print(dataframe.shape)#satır ve sutun sayısını ogrenme
dataframe= dataframe.drop(dataframe.columns[[0,2,4,5,6,10,11,12,13,14,15,16]], axis=1)#istenmeyen sutunları silme
#null degerleri kaldırma
dataframe.dropna(how="all",inplace=True)
dataframe.dropna(how="any",inplace=True)
#sutundakileri stringe cevirme
dataframe['Complaint ID'] =dataframe['Complaint ID'].astype(str)
dataframe['ZIP code'] =dataframe['ZIP code'].astype(str)
dataframe['Company'] =dataframe['Company'].astype(str)
dataframe['State'] = dataframe['State'].astype(str)
dataframe['Issue'] =dataframe['Issue'].astype(str)
dataframe['Product'] =dataframe['Product'].astype(str)
#sutunlardaki tum verileri  kucuk harfe cevirme
dataframe['Product']=dataframe['Product'].str.lower()
dataframe['Issue']=dataframe['Issue'].str.lower()
dataframe['Company']=dataframe['Company'].str.lower()
dataframe['State']=dataframe['State'].str.lower()
dataframe['ZIP code'] = dataframe['ZIP code'].str.lower()
dataframe['Complaint ID'] =dataframe['Complaint ID'].str.lower()
#veri setinden noktalama işaretlerini sildirme
dataframe['Complaint ID'] = dataframe['Complaint ID'].str.replace(r'[^\w\s]+', '', regex=True)
dataframe['ZIP code'] =dataframe['ZIP code'].str.replace(r'[^\w\s]+', '', regex=True)
dataframe['Company'] =dataframe['Company'].str.replace(r'[^\w\s]+', '', regex=True)
dataframe['State'] =dataframe['State'].str.replace(r'[^\w\s]+', '', regex=True)
dataframe['Issue'] =dataframe['Issue'].str.replace(r'[^\w\s]+', '', regex=True)
dataframe['Product'] =dataframe['Product'].str.replace(r'[^\w\s]+', '', regex=True)
#stop words kaldırma
dataframe['Complaint ID']= dataframe['Complaint ID'].apply(lambda i: ' '.join([kelimeindex for kelimeindex in i.split() if kelimeindex not in (stop)]))
dataframe['ZIP code'] =dataframe['ZIP code'].apply(lambda i: ' '.join([kelimeindex for kelimeindex in i.split() if kelimeindex not in (stop)]))
dataframe['Company']=dataframe['Company'].apply(lambda i: ' '.join([kelimeindex for kelimeindex in i.split() if kelimeindex not in (stop)]))
dataframe['State'] =dataframe['State'].apply(lambda i: ' '.join([kelimeindex for kelimeindex in i.split() if kelimeindex not in (stop)]))
dataframe['Issue']=dataframe['Issue'].apply(lambda i: ' '.join([kelimeindex for kelimeindex in i.split() if kelimeindex not in (stop)]))
dataframe['Product']=dataframe['Product'].apply(lambda i: ' '.join([kelimeindex for kelimeindex in i.split() if kelimeindex not in (stop)]))
#csv dosyasına cevirme
dataframe.to_csv('yazlab2',index=False)
    

      
      








