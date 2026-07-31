#task 3.1

def task3_1(quantity_of_data):
    units = {'KB' : 10**3, 'MB' : 10**6, 'GB' : 10**9, 'TB' : 10**12}
    if len(quantity_of_data) < 3:
        return "invalid data"
    
    value , unit = quantity_of_data[:-2] , quantity_of_data[-2:]
    if unit in units and value.isdigit():
        converted = int(value) * units[unit]
        return converted
    else:
        return "invalid data"


#print(task3_1("8KB"))
#print(task3_1("2MB"))
#print(task3_1("10GB"))
#print(task3_1("200TB"))
#print(task3_1("10JB"))
#print(task3_1("PMB"))
        
    



#task 3.2

def task3_2(quantity_of_data):
    result = task3_1(quantity_of_data)
    if str(result).isdigit():
        return result
    else:
        units = {'KiB' : 2**10 , 'MiB' : 2**20 , 'GiB' : 2**30 , 'TiB' : 2**40}
        if len(quantity_of_data) < 4:
            return "invalid data"
        
        value , unit = quantity_of_data[:-3] , quantity_of_data[-3:]
        if unit in units and value.isdigit():
            converted = int(value) * units[unit]
            return converted
        else:
            return "invalid data"


##print(task3_2("8KB"))
##print(task3_2("2MB"))
##print(task3_2("10GB"))
##print(task3_2("200TB"))
##print(task3_2("10JB"))
##print(task3_2("PMB"))
##print(task3_2("8KiB"))
##print(task3_2("10MiB"))
##print(task3_2("7GiB"))
##print(task3_2("20TiB"))
##print(task3_2("10GBB"))
##print(task3_2("XTiB"))





#task 3.3

def task3_3(quantity_of_data , target_unit):
    units = {'KB' : 10**3, 'MB' : 10**6, 'GB' : 10**9, 'TB' : 10**12, 'KiB' : 2**10 , 'MiB' : 2**20 , 'GiB' : 2**30 , 'TiB' : 2**40}
    if target_unit not in units:
        return "invalid data"
    else:
        converted = task3_2(quantity_of_data)
        if str(converted).isdigit():
            result = converted / units[target_unit]
            return result
        else:
            return "invalid data"


print(task3_3("512MiB" , "GiB"))
print(task3_3("2MB" , "TiB"))
print(task3_3("17MB" , "VB"))


        
    
