import yaml
import datetime
import time

with open('Milestone1\Milestone1A.yaml') as f:
    mil_1a = yaml.load(f, Loader = yaml.FullLoader)

def task_func(tasks, log, i):
    with open('Log_mil1A.txt', 'a', encoding = 'UTF8') as f:
        log1 = log[:len(log) - 7] + '.' + str(i) + ' Entry' + '\n'
        f.write(log1)
        log2 = log1[:len(log) - 7] + ' Executing ' + str(tasks[i]['Function']) + '(' + str(tasks[i]['Inputs']['FunctionInput']) + ', ' + str(tasks[i]['Inputs']['ExecutionTime']) + ')' + '\n'
        f.write(log2)
        log3 = log[:len(log) - 7] + '.' + str(i) + ' Exit' + '\n'
        f.write(log3)
        f.close()

def flow_func(tasks, log, i):
    

def milestone1(data):
    with open('Log_mil1A.txt', 'w', encoding = 'UTF8') as f:
        log = str(datetime.datetime.now()) + ';' + str(list(data)[0]) + ' ' + str('Entry') + '\n'
        f.write(log)
        f.close()
        
        activities = data[str(list(data)[0])]['Activities']
        for i in activities:
            if activities[i]['Type'] == 'Task':
                task_func(activities, log, i)
        
            if activities[i]['Type'] == 'Flow':
                
                for x in activities[i]:
                
print(milestone1(mil_1a))
    
    
    
    
