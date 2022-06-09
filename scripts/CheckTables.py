import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# Example: load a DSS dataset as a Pandas dataframe
mydataset = dataiku.Dataset("Amplifon_EMEA_SQLSERVER_BQ")
mydataset_df = mydataset.get_dataframe()

tables= mydataset_df['Table target'].tolist()


tables= ['adlp_dataset_etl_1.STG_CAR__FT_CAR']


tables_upper=[]
for el in tables:
    tables_upper.append(str.upper(str.split(el, '.')[1]))
tables_upper

this_client  = dataiku.api_client()
dss_projects = this_client.list_project_keys()

problem= []
for key in dss_projects:
    print(key)
    project= this_client.get_project(key)
    datasets= project.list_datasets()
    for i in range(len(datasets)):
        if datasets[i]['type']== 'BigQuery':
            if (datasets[i]['params']['mode']!= 'query'):
                if str.upper(project.list_datasets()[i]['params']['table']) in tables_upper:
                    problem.append(key)
                    break
###
problems={}
for key in problem:
    tmp=[]
    project= this_client.get_project(key)
    datasets= project.list_datasets()
    for i in range(len(datasets)):
        if datasets[i]['type']== 'BigQuery':
            if (datasets[i]['params']['mode']!= 'query'):
                tmp.append(datasets[i]['params']['schema']+ '.'+project.list_datasets()[i]['params']['table'])
    problems[key]=tmp
##

import dataiku
from dataiku import pandasutils as pdu
import pandas as pd
import json

this_client  = dataiku.api_client()
dss_users = this_client.list_users()
# dss_users is a list of dict. Each item represents one user
# Using dictionary comprehension + items()
# Extracting specifix keys from dictionary
for user in dss_users:
    res = {key: user[key] for key in user.keys()
                               & {"login","groups", "userProfile"}}
    res2 = {key: user[key] for key in user.keys()
                               & {"login"}}
    print("User: " + str(res2) + " - Info: " + str(res))

### new_dict_keys = ("login","groups", "userProfile")
### small_dict=dict_filter(dss_users, new_dict_keys)
###
### print(json.dumps(small_dict, indent=2))
