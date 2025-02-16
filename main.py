# Different ways of doing this
# type1 
# print("Enter todo:")

# type2
# user_text = input("Enter todo:")
# print(user_text)

# type3
# user_prompt="Enter a todo :"
# user_text = input(user_prompt)
# print(user_text)



todos = []

while True :
    action1 = input("Type add,show , edit or exit :")
    action1 = action1.strip()

    match action1:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
            # print("The todo list :" ,todos)

        case 'edit':
            number = int(input("Number of the todo to edit :"))
            number = number -1
            new_todo = input("Enter new todo:")
            todos[number] = new_todo

        case 'exit':
            break

        case x:
            print("You entered and unknown command !")

        


print("Exiting from the todo list !")
   
   
    
