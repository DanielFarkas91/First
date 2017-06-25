# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    sum = 0
    for key, value in inventory.items():
        print(value, key)
        sum = sum + value
    
    print("Total number of items: %d" % sum)
    return inventory


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for key in inventory.keys():
        for item in added_items:
            if item == key:
                inventory[item] += 1
                continue

    if item not in inventory.keys():
        inventory.update({item: 1})

    return inventory


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    if order == None:
        print("Inventory:")
        print("{:>7} {:>12}".format('count','item name'))
        print(('--------------------'))
        sum = 0
        for key, value in inventory.items():
            print("{:>7} {:>12}".format(value, key))
            sum = sum + value
        print(('--------------------'))
        print("Total number of items: %d" % sum)
    
    if order == "count,asc":
        inventory_list = []
        for key, value in inventory.items():
            inventory_items = [value, key]
            inventory_list.append(inventory_items)
    
        y = sorted(inventory_list)
        print("Inventory:")
        print("{:>7} {:>12}".format('count','item name'))
        print(('--------------------'))
        sum = 0
        for x, z in y:
            print("{:>7} {:>12}".format(x, z))
            sum = sum + x
        print(('--------------------'))
        print("Total number of items: %d" % sum)

    if order == "count,desc":
        inventory_list = []
        for key, value in inventory.items():
            inventory_items = [value, key]
            inventory_list.append(inventory_items)

        y = sorted(inventory_list, reverse=True)
        print("Inventory:")
        print("{:>7} {:>12}".format('count','item name'))
        print(('--------------------'))
        sum = 0
        for x, z in y:
            print("{:>7} {:>12}".format(x, z))
            sum = sum + x
        print(('--------------------'))
        print("Total number of items: %d" % sum) 


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    import csv
    with open("import_inventory.csv", "r") as importFile:
        importFileReader = csv.reader(importFile)
        itemsList = []
        for item in importFileReader:
            if len (item) != 0:
                itemsList = item
    for item in itemsList:
        for key, value in inventory.items():
            if item == key:
                inventory.update({item: value + 1})
                continue
                
        if item not in inventory.keys():
            inventory.update({item: 1})

    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    import csv
    with open("export_inventory.csv", 'w') as exportFile:
        exportFileReader = csv.writer(exportFile)
        
        lista = []
        for key, value in inventory.items():
            i = 0
            while i < value:
                lista.append(key)
                i = i + 1
        print(lista)
        for i in range(0,1):
            exportFileReader.writerow(lista)
