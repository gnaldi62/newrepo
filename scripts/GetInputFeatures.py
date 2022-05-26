import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

project_list = ["PROJECT1", "PROJECT2", "PROJECT3", "PROJECT4"]

full_feature_list = []

for curr_project in project_list:
    project = dataiku.api_client().get_project(curr_project)
    saved_model_list = project.list_saved_models()
    for curr_model in saved_model_list:
        saved_model = project.get_saved_model(curr_model["id"])
        origin_ml_task = saved_model.get_origin_ml_task()
        dict_of_features = origin_ml_task.get_settings().get_raw()["preprocessing"]["per_feature"]
        for f_id, f_info in dict_of_features.items():
            for key in f_info:
                if key == 'role':
                    if f_info[key] == 'INPUT':
                        full_feature_list.append(f_id)

mylist = list(dict.fromkeys(full_feature_list))
mylist.sort()
print(mylist)
