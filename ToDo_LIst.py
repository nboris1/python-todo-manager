todo_list = []
print("===================================")
print(    "PYTHON   TODO LIST MANAGER"     )
print("===================================")



while 1>0:
    check = input("Type 'add'- to add a Task,'delete' to remove task, 'view' to see task or 'exit' to quit :").lower()
    if "exit" in check:
        break
    elif "add" in check:
        add_task = input("add task : ").lower()
        todo_list.append(add_task)
        print("added succefully!")
    elif "view" in check:
        if not todo_list:
            print("Your to do list is empty!")
        else:
            for index , task in enumerate(todo_list,start=1):
                print(f"{index}. {task}")
    elif "delete" in check:
        if not todo_list:
            print("No task to delete!")
        else:
            task_num = int(input("Enter Task number to remove task : "))
            list_index = task_num - 1

            if list_index < 0 or list_index >= len(todo_list):
                print("invalid task number!")
            else:
                
                removed_task = todo_list.pop(list_index)
                print(f"Success!!: {removed_task} removed.")
    else:
        print("wrong input, retry")