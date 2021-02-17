from Database import metadata_table
from RSA import crypt, decrypt

import os


def menu():
    """
    Prints the available actions in the console
    :return: None
    """
    print(">1. Add document in database")
    print(">2. Delete document from database")
    print(">3. Read document from database")
    print(">Exit")


def parse_command():
    """
    This function parses the input from the user and extracts the information that is needed further
    Throws an error if the file cannot be opened or read
    :return: a tuple that consists in the requested action (add/delete/read from Database), the content of the file,
    the path, and the file name
    """
    base_path = "C:\\Users\\Daria\\Desktop\\"
    print("The file path is: ", base_path)
    data_input = input("Type in command:\n")
    split_command = data_input.split(" ")
    if len(split_command) != 2:
        print("Invalid command! Please type add|delete|read <file_name>")
        data_input = input("Type in command:\n")
    else:
        split_command = data_input.split(" ")
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
    """
    Adds file information in the Database
    :param file_name: The name of the file
    :param content: The content of the file, encrypted
    :param file_path: The path
    :return: None
    """
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
    """
    Deletes a file from the Database
    :param file_name: The file name
    :return: None
    """
    metadata_table.delete_many({"Name": file_name})
    print("File ", file_name, " deleted!")


def read(file_name, file_path):
    """
    Prints in console the decrypted content and/or creates a file in which the decrypted content can be found.
    Throws an exception if the output file cannot be opens or if it cannot be written in
    :param file_name: The file name
    :param file_path: The file path
    :return: None
    """
    enc_content_cursor = metadata_table.find({"Name": file_name})
    for enc_content in enc_content_cursor:
        print("enc: ", enc_content)
        dc = decrypt(enc_content["Content"])
        name, ext = os.path.splitext(file_path)
        if ext == ".txt":
            print(dc.decode("utf-8"))
        else:
            print("Check the file \"result\" for the decoded content! ")
        try:
            path = "C:\\Users\\Daria\\Desktop\\"
            result = "result" + ext
            print_file = open(path+result, "wb")
            print_file.write(dc)
            print_file.close()
        except Exception as e:
            print(e)


def main_fct():
    """
    The main program that combines all the functions written previously
    :return: None
    """
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
