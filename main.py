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

action = "Enter a todo :"

todos = []

while True :
    todo=input(action)
    todos.append(todo)
    print("Here is the todo list : " , todos)

