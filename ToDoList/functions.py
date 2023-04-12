def get_to_do_list(filepath='to_do.txt'):
    with open(filepath, 'r') as file:
        to_do_list = file.readlines()
    return to_do_list

def write_to_do_list(my_list, filepath='to_do.txt'):
    with open(filepath, 'w') as file:
        file.writelines(my_list)