import pandas as pd
import numpy as np
from io import StringIO
import requests
import json
import codecs
import pickle
from sklearn.decomposition import PCA


# @hidden_cell
# This function accesses a file in your Object Storage. The definition contains your credentials.
# You might want to remove those credentials before you share your notebook.
def get_object_storage_file_with_credentials_a860223228054eadb78455bad5266913(container, filename):
    """This functions returns a StringIO object containing
    the file content from Bluemix Object Storage."""

    url1 = ''.join(['https://identity.open.softlayer.com', '/v3/auth/tokens'])
    data = {'auth': {'identity': {'methods': ['password'],
            'password': {'user': {'name': 'member_c31eef4c6875a326d7c2cb16984a5e02d9dace51','domain': {'id': 'e4c3685617404e40b0afb0d280e5d678'},
            'password': 'b31qd?[3APH3&].5'}}}}}
    headers1 = {'Content-Type': 'application/json'}
    resp1 = requests.post(url=url1, data=json.dumps(data), headers=headers1)
    resp1_body = resp1.json()
    for e1 in resp1_body['token']['catalog']:
        if(e1['type']=='object-store'):
            for e2 in e1['endpoints']:
                        if(e2['interface']=='public'and e2['region']=='dallas'):
                            url2 = ''.join([e2['url'],'/', container, '/', filename])
    s_subject_token = resp1.headers['x-subject-token']
    headers2 = {'X-Auth-Token': s_subject_token, 'accept': 'application/json'}
    resp2 = requests.get(url=url2, headers=headers2)
    return StringIO(resp2.text)


def put_object_storage_file_with_credentials_a860223228054eadb78455bad5266913(container, filename):  
    f = open(filename,'r')
    file_data = f.read()
    url1 = ''.join(['https://identity.open.softlayer.com', '/v3/auth/tokens'])
    data = {'auth': {'identity': {'methods': ['password'],
            'password': {'user': {'name': 'member_c31eef4c6875a326d7c2cb16984a5e02d9dace51','domain': {'id': 'e4c3685617404e40b0afb0d280e5d678'},
            'password': 'b31qd?[3APH3&].5'}}}}}
    headers1 = {'Content-Type': 'application/json'}
    resp1 = requests.post(url=url1, data=json.dumps(data), headers=headers1)
    resp1_body = resp1.json()
    for e1 in resp1_body['token']['catalog']:
        if(e1['type']=='object-store'):
            for e2 in e1['endpoints']:
                        if(e2['interface']=='public'and e2['region']=='dallas'):
                            url2 = ''.join([e2['url'],'/', container, '/', filename])
    s_subject_token = resp1.headers['x-subject-token']
    headers2 = {'X-Auth-Token': s_subject_token, 'accept': 'application/json'}
    resp2 = requests.put(url=url2, headers=headers2, data = file_data )
    print resp2


def predict_usura(x):
	return y


def create_mat(x):
	x_clean = pd.read_csv(get_object_storage_file_with_credentials_a860223228054eadb78455bad5266913('ITTProject', 'template_materials.csv'), index_col = 'Unnamed: 0')
	my_df = {}
	for index,row in x.iterrows():
		my_row = { col : 0 for col in x_clean.columns.values }
		tmp = 0
		for i in np.arange(2,87, 3):
		    tmp += row[i] 
		    if row[i]!= 0:
		        my_row[str(int(row[i-1]))+"_"+str(int(row[i+1]))] = row[i]
		my_df[row[0]] = my_row
		x_clean.loc[row[0]] = [ my_row[col] for col in x_clean.columns.values]
	
	x_clean = x_clean.div(x_clean.sum(axis = 1), axis = 0)
	return x_clean	

def main():
	x = pd.read_csv('./ITT/materials.csv', header = None)
	print x.head()
	print create_mat(pd.DataFrame(data = [x.values[0, :]], columns = x.columns))




main()
