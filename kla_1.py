import yaml
import datetime
import time

with open('Milestone1\Milestone1A.yaml') as f:
    mil_1a = yaml.load(f, Loader = yaml.FullLoader)

def milestone1(data):
    with open('Log_mil1A.txt', 'w', encoding = 'UTF8') as f:
        log = str(datetime.datetime.now()) + ';' + str(list(data)[0]) + ' ' + str('Entry') + '\n'
        f.write(log)
        
        activities = data[str(list(data)[0])]['Activities']
        for i in activities:
            if activities[i]['Type'] == 'Task':
                log1 = log[:len(log) - 7] + '.' + str(i) + ' Entry' + '\n'
                f.write(log1)
                log2 = log1[:len(log) - 7] + ' Executing ' + str(activities[i]['Function']) + '(' + str(activities[i]['Inputs']['FunctionInput']) + ', ' + str(activities[i]['Inputs']['ExecutionTime']) + ')' + '\n'
                f.write(log2)
                log3 = log[:len(log) - 7] + '.' + str(i) + ' Exit' + '\n'
                f.write(log3)
                
                
            
print(milestone1(mil_1a))
    
    
    
    
