import csv
import os


def add_to_inventory(inv, new_items):
    for item in new_items:
        inv[item] = inv.get(item, 0) + 1
    return inv


def display_inventory(inv):
    print('Inventory:')
    sum = 0
    for item in inv.items():
        sum += item[1]
        print(item[1], item[0])
    print('Total number of items: ', sum)


def print_table(inv, order=''):
    inv_list = [i for i in inv.items()]

    if order == "count,asc":
        inv_list.sort(key=lambda x: x[1])

    if order == "count,desc":
        inv_list.sort(key=lambda x: x[1], reverse=True)

    # creating sepatate lists for names and counts
    inv_list_names = [i[0] for i in inv_list]
    inv_list_numbers = [str(i[1]) for i in inv_list]

    # calculating max length of the content
    max_length_names = max(len(x) for x in inv_list_names)
    max_length_numbers = max(len(x) for x in inv_list_numbers)

    # defining table parameters
    header = ['count', 'item name']
    table_padding = 3
    # total table width = max length of characters + extra paddings by columns
    table_width = (
        max_length_names + max_length_numbers + (2 * table_padding) + 1
    )

    # aligning the text with str.format() and specifying a width
    format_template = '{0:>' + str(max_length_numbers + table_padding) + '} '
    format_template += '{1:>' + str(max_length_names + table_padding)+'}'

    # table header
    print('Inventory:')
    print(format_template.format(header[0], header[1]))
    print('-' * table_width)

    sum = 0
    for i in range(0, len(inv_list)):
        sum += inv_list[i][1]
        print(format_template.format(
            inv_list_numbers[i], inv_list_names[i])
        )

    # table footer, summary
    print('-' * table_width)
    print('Total number of items: ', sum)


def import_inventory(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            DictReader_object = csv.DictReader(f)
            inv = {}
            for row in DictReader_object:
                if row['item_name'] in inv:
                    inv[row['item_name']] += int(row['count'])
                else:
                    inv.update({row['item_name']: int(row['count'])})
        return inv


def export_inventory(filename):
    with open(filename, 'w') as f:
        fieldnames = ['count', 'item_name']

        DictWriter_object = csv.DictWriter(f, fieldnames=fieldnames)
        DictWriter_object.writeheader()
        for item in inventory.items():
            DictWriter_object.writerow(
                {'count': item[1], 'item_name': item[0]}
            )

print("\n========== GAME INVENTORY ==========\n")

inventory = {'rope': 1, 'torch': 600, 'gold coin': 4, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print("inventory:", inventory)
print("dragon_loot:", dragon_loot)
print('\ndisplay_inventory() after adding loot:')
add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)

print('\n=============================\n')
print('\ndisplay in table - without order:')
print_table(inventory)
print('\ndisplay in table - count, asc:')
print_table(inventory, 'count,asc')
print('\ndisplay in table - count, desc:')
print_table(inventory, 'count,desc')

print('\n=============================\n')
print('after importing import.csv:\n')
imported_inventory = import_inventory('import.csv')
print_table(imported_inventory, 'count,asc')

export_inventory('export.csv')
print('\ncheck export.csv !\n')
print("\n========= DONE =========\n")
