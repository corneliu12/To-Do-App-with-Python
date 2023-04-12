from functions import get_to_do_list, write_to_do_list


while True:
    user_input = input("Enter add, show, edit, complete, or exit: ")
    user_input = user_input.strip().lower()
    
    #Add new To-do itme
    if user_input.startswith('add'):
        new_item = user_input[4:]

        to_do_list = get_to_do_list()
        to_do_list.append(new_item + '\n')
        
        write_to_do_list(to_do_list)
        print(f"-- {new_item} -- was added to the list.")
            
    #SHOW the list
    elif user_input.startswith('show'):
        to_do_list = get_to_do_list()

        print("\nTo Do List\n")
        for index, item in enumerate(to_do_list):
            item = item.strip("\n")
            print(f"{index+1}. {item}")
        print("")    
        

    #EDIT the list
    elif user_input.startswith('edit'):

        try:
            number = int(user_input[5:])
            print(f"Editing number {number}")
            number -= 1

            to_do_list = get_to_do_list()
            
            new_item = input("Enter new to do item: ")
            to_do_list[number] = new_item + '\n'
            
            write_to_do_list(to_do_list)
            print("Item value changed...")
        except ValueError:
            print("You enter wrong command.")

    #COMPLETE a to-do (erase)
    elif user_input.startswith('complete'):
        
        try:
            number = int(user_input[9:])

            to_do_list = get_to_do_list()

            index = number - 1        
            item_removed = to_do_list.pop(index).strip('\n')
            print(f"{item_removed} was removed from the to do list.")
            write_to_do_list(to_do_list)
        except ValueError:
            print("There is no item with that number.")
            continue


    #EXIT PROGRAM ON "exit"
    elif user_input.startswith('exit'):
        print("Bye!...")
        break


