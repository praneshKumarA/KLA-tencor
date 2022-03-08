import yaml
import datetime
import time
import threading
import csv
import operator

with open('Milestone2\Milestone2A.yaml') as f:
    mil_1a = yaml.load(f, Loader = yaml.FullLoader)
    
with open('Milestone2\Milestone2B.yaml') as f:
    mil_1b = yaml.load(f, Loader = yaml.FullLoader)

dict = {}

def symbols(a, b, sym):
    if sym == '<':
        return operator.lt(a, b)
    elif sym == '>':
        return operator.gt(a, b)
    elif sym == '<=':
        return operator.le(a, b)
    elif sym == '>=':
        return operator.ge(a, b)
    elif sym == '==':
        return operator.eq(a, b)
    else:
        return operator.ne(a, b)
    

def task_func(tasks, log, i, file):
    if tasks[i]['Function'] == "DataLoad" and 'Condition' not in tasks[i].keys():
        file1 = 'Milestone2\\' + tasks[i]['Inputs']['Filename']
        with open(file1, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            nod = csvreader.line_num
            csvfile.close()
        tasks[i]['Outputs'][1] = nod
        with open(file, 'a', encoding = 'UTF8') as f:
            log1 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Entry' + '\n'
            dict[log[log.index(';'):len(log) - 7] + '.' + str(i) + '.' + str('NoOfDetects')] = nod
            f.write(log1)
            log2 = str(datetime.datetime.now()) + log1[log1.index(';'):len(log) - 7] + '.' + str(i) + ' Executing ' + str(tasks[i]['Function']) + '(' + str(tasks[i]['Inputs']['Filename']) + ')' + '\n'
            f.write(log2)
            log3 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Exit' + '\n'
            f.write(log3)
            f.close()
    
    if tasks[i]['Function'] == "DataLoad" and 'Condition' in tasks[i].keys():
        f1 = tasks[i]['Condition'].split()[0][2:-1]
        c = tasks[i]['Condition'].split()[2]
        sym = tasks[i]['Condition'].split()[1]
        if symbols(dict[f1], c, sym):
            file1 = 'Milestone2\\' + tasks[i]['Inputs']['Filename']
            with open(file1, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                headers = next(csvreader)
                nod = csvreader.line_num
                csvfile.close()
            # tasks[i]['Outputs'][1] = nod
            dict[log[int(log.index(';')) + 1:len(log) - 7] + '.' + str(i) + '.' + str('NoOfDetects')] = nod
            with open(file, 'a', encoding = 'UTF8') as f:
                log1 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Entry' + '\n'
                # dict[log[log.index(';'):len(log) - 7] + '.' + str(i) + '.' + str('NoOfDetects')] = nod
                f.write(log1)
                log2 = str(datetime.datetime.now()) + log1[log1.index(';'):len(log) - 7] + '.' + str(i) + ' Executing ' + str(tasks[i]['Function']) + '(' + str(tasks[i]['Inputs']['Filename']) + ')' + '\n'
                f.write(log2)
                log3 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Exit' + '\n'
                f.write(log3)
                f.close()    
        else:
            with open(file, 'a', encoding = 'UTF8') as f:
                log1 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Entry' + '\n'
                f.write(log1)
                log2 = str(datetime.datetime.now()) + log1[log1.index(';'):len(log) - 7] + '.' + str(i) + ' Skipped' + '\n'
                f.write(log2)
                log3 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Exit' + '\n'
                f.write(log3)
                f.close()
    
    
            
    if tasks[i]['Function'] == "TimeFunction" and 'Condition' in tasks[i].keys():
        f1 = tasks[i]['Condition'].split()[0][2:-1]
        c = tasks[i]['Condition'].split()[2]
        sym = tasks[i]['Condition'].split()[1]
        
        if symbols(dict[f1], c, sym):
            with open(file, 'a', encoding = 'UTF8') as f:    
                log1 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Entry' + '\n'
                f.write(log1)
                time.sleep(int(tasks[i]['Inputs']['ExecutionTime']))
                log2 = str(datetime.datetime.now()) + log1[log1.index(';'):len(log) - 7] + '.' + str(i) + ' Executing ' + str(tasks[i]['Function']) + '(' + str(tasks[i]['Inputs']['FunctionInput']) + ', ' + str(tasks[i]['Inputs']['ExecutionTime']) + ')' + '\n'
                f.write(log2)
                log3 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Exit' + '\n'
                f.write(log3)
                f.close()
        else:
            with open(file, 'a', encoding = 'UTF8') as f:
                log1 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Entry' + '\n'
                f.write(log1)
                log2 = str(datetime.datetime.now()) + log1[log1.index(';'):len(log) - 7] + '.' + str(i) + ' Skipped' + '\n'
                f.write(log2)
                log3 = str(datetime.datetime.now()) + log[log.index(';'):len(log) - 7] + '.' + str(i) + ' Exit' + '\n'
                f.write(log3)
                f.close()
        
        
    if tasks[i]['Function'] == "TimeFunction" and 'Condition' not in tasks[i].keys():
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
        if tasks[i]['Activities'][x]['Type'] == 'Flow' and tasks[i]['Activities'][x]['Execution'] == 'Sequential':
            t = threading.Thread(target = flow_func, args = (tasks[i]['Activities'], log1, x, file, ))
            t.start()
            threads.append(t)
        if tasks[i]['Activities'][x]['Type'] == 'Flow' and tasks[i]['Activities'][x]['Execution'] == 'Concurrent':
            t = threading.Thread(target = flow_func_conc, args = (tasks[i]['Activities'], log1, x, file, ))
            t.start()
            threads.append(t)
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
                

print(milestone1(mil_1a, 'Milestone2\Log_mil2A.txt'))
print(dict)
# print(milestone1(mil_1b, 'Milestone2\Log_mil2B.txt'))
    
    
    