import yaml
import datetime
import csv
import time

with open('Milestone1\Milestone1A.yaml') as f:
    mil_1a = yaml.load(f, Loader = yaml.FullLoader)
# prev_log = str()
# def task_func():
    
    
# def flow_func(flow, name):
#     prev_log = flow_func_entry(name, prev_log)
#     if flow['Execution'] == 'Sequential':
#         activities = flow['Activities']
#         for i in activities:
#             for j in activities[i]:
#                 if activities[i][j] == 'Flow':
#                     flow_func(activities[i], i)
        
    
# def flow_func_entry(name):
#     with open('Log_mil1A.csv', 'w', encoding = 'UTF8') as f:
#         writer = csv.writer(f, delimiter = ';')
#         log = [str(datetime.datetime.now()), str(name) + ' ' + str('Entry')]
#         writer.writerow(log)
#     return ";".join(log)

def milestone1(data):
    with open('Log_mil1A.txt', 'w', encoding = 'UTF8') as f:
        log = str(datetime.datetime.now()) + ';' + str(list(data)[0]) + ' ' + str('Entry')
        f.write(log)
        
        activities = data[str(list(data)[0])]['Activities']
        for i in activities:
            if activities[i]['Type'] == 'Task':
                log = 
            
print(milestone1(mil_1a))
    
    
    
    
