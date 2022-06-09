import dataiku
from dataiku import pandasutils as pdu
import pandas as pd
import json

this_client  = dataiku.api_client()
dss_projects = this_client.list_project_keys()

wrong_report={}
wrong_config={}
for this_project in dss_projects:
    curr_project = this_client.get_project(this_project)
    s=[]
    c=[]
    for scenario in curr_project.list_scenarios(as_type="objects"):
        settings = scenario.get_settings()
        for reporter in settings.raw_reporters:
            # Only look into 'email' kind of reporters
            if reporter["messaging"]["type"] == "mail-scenario":
                messaging_configuration = reporter["messaging"]["configuration"]
                try:
                    if (messaging_configuration['channelId'] != 'Office365') & (messaging_configuration['channelId'] != 'OfficeSMTP'):
                        s.append({'name': settings.get_raw()['id'], 'active': reporter['active'], 'channel': messaging_configuration['channelId']})
                        print("Nome del progetto: ", settings.get_raw()['projectKey'])
                        print("-> Nome dello scenario: ", settings.get_raw()['id'])
                        print("--> Configurazione e-mail: ", str(messaging_configuration))
                except:
                    c.append({'name': settings.get_raw()['id'], 'active': reporter['active']})
    if len(s)>0:
        wrong_report[this_project]= s
    if len(c)>0:
        wrong_config[this_project]= c
for this_project in wrong_report.keys():
   curr_project = this_client.get_project(this_project)
   s=[]
   c=[]
   for scenario in curr_project.list_scenarios(as_type="objects"):
       settings = scenario.get_settings()
       for reporter in settings.raw_reporters:
           # Only look into 'email' kind of reporters
           if reporter["messaging"]["type"] == "mail-scenario":
               messaging_configuration = reporter["messaging"]["configuration"]
               try:
                   if messaging_configuration['channelId'] != 'OfficeSMTP':
                       messaging_configuration['channelId'] = 'OfficeSMTP'
                       settings.save()
               except:
                   continue
wrong_report={}
wrong_config={}
for this_project in dss_projects:
    curr_project = this_client.get_project(this_project)
    s=[]
    c=[]
    for scenario in curr_project.list_scenarios(as_type="objects"):
        settings = scenario.get_settings()
        for reporter in settings.raw_reporters:
            # Only look into 'email' kind of reporters
            if reporter["messaging"]["type"] == "mail-scenario":
                messaging_configuration = reporter["messaging"]["configuration"]
                try:
                    if messaging_configuration['channelId'] != 'OfficeSMTP':
                        s.append({'name': settings.get_raw()['id'], 'active': reporter['active'], 'channel': messaging_configuration['channelId']})
                        print("Nome del progetto: ", settings.get_raw()['projectKey'])
                        print("-> Nome dello scenario: ", settings.get_raw()['id'])
                        print("--> Configurazione e-mail: ", str(messaging_configuration))
                except:
                    c.append({'name': settings.get_raw()['id'], 'active': reporter['active']})
    if len(s)>0:
        wrong_report[this_project]= s
    if len(c)>0:
        wrong_config[this_project]= c
        
for this_project in dss_projects:
    curr_project = this_client.get_project(this_project)
    for scenario in curr_project.list_scenarios(as_type="objects"):
        settings = scenario.get_settings()
        for reporter in settings.raw_reporters:
            # Only look into 'email' kind of reporters
            if reporter["messaging"]["type"] == "mail-scenario":
                messaging_configuration = reporter["messaging"]["configuration"]
                try:
                    print(this_project, scenario.id, messaging_configuration['sender'])
                except:
                    print(messaging_configuration)
for this_project in dss_projects:
    curr_project = this_client.get_project(this_project)
    for scenario in curr_project.list_scenarios(as_type="objects"):
        settings = scenario.get_settings()
        for reporter in settings.raw_reporters:
            # Only look into 'email' kind of reporters
            if reporter["messaging"]["type"] == "mail-scenario":
                messaging_configuration = reporter["messaging"]["configuration"]
                try:
                    if messaging_configuration['sender']!=  'dataiku@amplifon.com':
                        messaging_configuration['sender']=  'dataiku@amplifon.com'
                        settings.save()
                except:
                    continue
for this_project in dss_projects:
    curr_project = this_client.get_project(this_project)
    for scenario in curr_project.list_scenarios(as_type="objects"):
        settings = scenario.get_settings()
        for reporter in settings.raw_reporters:
            # Only look into 'email' kind of reporters
            if reporter["messaging"]["type"] == "mail-scenario":
                messaging_configuration = reporter["messaging"]["configuration"]
                try:
                    print(this_project, scenario.id, messaging_configuration['sender'])
                except:
                    print(messaging_configuration)
