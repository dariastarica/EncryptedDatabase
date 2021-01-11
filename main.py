from Database import metadata_table
from RSA import crypt, decrypt

import os


def menu():
    print(">1. Add document in database")
    print(">2. Delete document from database")
    print(">3. Read document from database")
    print(">Exit")


def parse_command():
    base_path = "C:\\Users\\Daria\\Desktop\\"
    print("The file path is: ", base_path)
    data_input = input("Type in command:\n")
    split_command = data_input.split(" ")
    print(split_command)
    while len(split_command) != 2:
        print("Invalid command! Please type add|delete|read <file_name>")
        data_input = input("Type in command:\n")
        split_command = data_input.split(" ")
    else:
        command = split_command[0]
        file_name = split_command[1]
        try:
            file_path = base_path + file_name
            file = open(file_path, "rb")
            content = file.read()
        except Exception as e:
            print(e)
        else:
            return command, content, file_path, file_name


def add(file_name, content, file_path):
    metadata_table.insert_one({
        # "_id": metadata_table.count_documents()+1,
        "Name": file_name,
        "Encryption Method": "RSA",
        "Public Key": 65537,
        "Content": crypt(content),
        "File size": os.path.getsize(file_path),
        "ctime": os.path.getctime(file_path),
        "mtime": os.path.getmtime(file_path),
        "atime": os.path.getatime(file_path)
    })
    print("File ", file_name, " added!")


def delete(file_name):
    metadata_table.delete_many({"Name": file_name})
    print("File ", file_name, " deleted!")


def read(file_name, file_path):
    enc_content_cursor = metadata_table.find({"Name": file_name})
    for enc_content in enc_content_cursor:
        print("enc: ", enc_content)
        dc = decrypt(enc_content["Content"])
        name, ext = os.path.splitext(file_path)
        if ext == ".txt":
            print(dc.decode("utf-8"))
        else:
            print("Check ", file_path, " for the decoded content! ")
        try:
            print_file = open(file_path, "wb")
            print_file.write(dc)
            print_file.close()
        except Exception as e:
            print(e)


def main_fct():
    menu()
    command, content, file_path, file_name = parse_command()
    if command == 'add':
        add(file_name, content, file_path)
    elif command == 'delete':
        delete(file_name)
    elif command == 'read':
        read(file_name, file_path)
    elif command == "Exit":
        SystemExit()


while 1:
    main_fct()
    print("--------------------------------------\n")
