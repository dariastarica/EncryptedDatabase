import Database
from RSA import crypt, decrypt

# base_path = "C:\\Users\\Daria\\Desktop\\"
# print("The file path is: ", base_path)
# file_name = input("Type in the file name: ")
# file_path = base_path+file_name
# file = open(file_path, "r")
# print(file.read())


def menu():
    print(">1. Add document in database")
    print(">2. Delete document from database")
    print(">3. Read document from database")
    data_input = input("Type in command:\n")
    split_command = data_input.split(" ")
    if len(split_command) != 2:
        print("Invalid command! Please type add|delete|read <path>")
    else:
        command = split_command[0]
        path = split_command[1]
        print(command)
        print(path)


menu()



