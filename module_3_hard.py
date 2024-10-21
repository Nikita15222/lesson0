data_structure = [ 
    [1, 2, 3], 
    {'a': 4, 'b': 5}, 
    (6, {'cube': 7, 'drum': 8}), 
    "Hello", 
    ((), [{(2, 'Urban', ('Urban2', 35))}]) 
] 
 

def calculate_structure_sum(item): 
    total = 0
    if isinstance(item, int): 
        total += item 
    elif isinstance(item, str): 
        total += len(item) 
    elif isinstance(item, list): 
        for sub_item in item: 
            total += calculate_structure_sum(sub_item) 
    elif isinstance(item, dict): 
        for key, value in item.items(): 
            total += calculate_structure_sum(key) 
            total += calculate_structure_sum(value) 
    elif isinstance(item, tuple): 
        item = list(item) 
        for i in item: 
            total += calculate_structure_sum(i)
    elif isinstance(item, set): 
        item = list(item) 
        for i in item: 
            total += calculate_structure_sum(i) 
    return total 
 
result = calculate_structure_sum(data_structure)
print(result)