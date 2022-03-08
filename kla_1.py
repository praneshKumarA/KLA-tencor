import yaml
import datetime
import time
import threading

with open('Milestone1\Milestone1A.yaml') as f:
    mil_1a = yaml.load(f, Loader = yaml.FullLoader)
    
with open('Milestone1\Milestone1B.yaml') as f:
    mil_1b = yaml.load(f, Loader = yaml.FullLoader)

def task_func(tasks, log, i, file):
    with open(file, 'a', encoding = 'UTF8') as f:
        log1 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Entry' + '\n'
        f.write(log1)
        time.sleep(int(tasks[i]['Inputs']['ExecutionTime']))
        log2 = str(datetime.datetime.now()) + log1[log1.index(';'):len(log) - 7] + '.' + str(i) + ' Executing ' + str(tasks[i]['Function']) + '(' + str(tasks[i]['Inputs']['FunctionInput']) + ', ' + str(tasks[i]['Inputs']['ExecutionTime']) + ')' + '\n'
        f.write(log2)
        log3 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Exit' + '\n'
        f.write(log3)
        f.close()

def flow_func_conc(tasks, log, i , file):
    with open(file, 'a', encoding = 'UTF8') as f:
        log1 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Entry' + '\n'
        f.write(log1)
        f.close()
    threads = []
    for x in tasks[i]['Activities']:
        if tasks[i]['Activities'][x]['Type'] == 'Task':
            t = threading.Thread(target = task_func, args = (tasks[i]['Activities'], log1, x, file, ))
            t.start()
            threads.append(t)
            # task_func(tasks[i]['Activities'], log1, x, file)
        if tasks[i]['Activities'][x]['Type'] == 'Flow':
            t = threading.Thread(target = flow_func, args = (tasks[i]['Activities'], log1, x, file, ))
            t.start()
            threads.append(t)
            # flow_func(tasks[i]['Activities'], log1, x, file)
    for thread in threads:
        thread.join()
    with open(file, 'a', encoding = 'UTF8') as f:
        log2 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Exit' + '\n'
        f.write(log2)
        f.close()

def flow_func(tasks, log, i, file):
    with open(file, 'a', encoding = 'UTF8') as f:
        log1 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Entry' + '\n'
        f.write(log1)
        f.close()
    for x in tasks[i]['Activities']:
        if tasks[i]['Activities'][x]['Type'] == 'Task':
            task_func(tasks[i]['Activities'], log1, x, file)
        if tasks[i]['Activities'][x]['Type'] == 'Flow' and tasks[i]['Activities'][x]['Execution'] == 'Sequential':
            flow_func(tasks[i]['Activities'], log1, x, file)
        if tasks[i]['Activities'][x]['Type'] == 'Flow' and tasks[i]['Activities'][x]['Execution'] == 'Concurrent':
            flow_func_conc(tasks[i]['Activities'], log1, x, file)
        
        
    with open(file, 'a', encoding = 'UTF8') as f:
        log2 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Exit' + '\n'
        f.write(log2)
        f.close()
            
def milestone1(data, file):
    with open(file, 'w', encoding = 'UTF8') as f:
        log = str(datetime.datetime.now()) + ';' + str(list(data)[0]) + ' ' + str('Entry') + '\n'
        f.write(log)
        f.close()

    activities = data[str(list(data)[0])]['Activities']
    for i in activities:
        if activities[i]['Type'] == 'Task':
            task_func(activities, log, i, file)
        
        if activities[i]['Type'] == 'Flow' and activities[i]['Execution'] == 'Concurrent':
            flow_func_conc(activities, log, i,  file)
        
        if activities[i]['Type'] == 'Flow' and activities[i]['Execution'] == 'Sequential':
            flow_func(activities, log, i,  file)
            
    with open(file, 'a', encoding = 'UTF8') as f:
        log_exit = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + ' Exit'
        f.write(log_exit)
        f.close()
                
print(milestone1(mil_1a, 'Log_mil1A.txt'))
print(milestone1(mil_1b, 'Log_mil1B.txt'))
    
    
    
