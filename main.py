from Database import metadata_table
from RSA import crypt, decrypt

import os


def menu():
    print(">1. Add document in database")
    print(">2. Delete document from database")
    print(">3. Read document from database")
    print(">Exit")
    base_path = "C:\\Users\\Daria\\Desktop\\"
    print("The file path is: ", base_path)
    data_input = input("Type in command:\n")
    split_command = data_input.split(" ")
    if len(split_command) != 2:
        print("Invalid command! Please type add|delete|read <file_name>")
    else:
        command = split_command[0]
        file_name = split_command[1]
        try:
            file_path = base_path+file_name
            file = open(file_path, "rb")
            content = file.read()
            print(content)
            # print(content, type(content))
        except Exception as e:
            print(e)
        else:
            if command == 'add':
                # public_key = input("Choose a public key: ")
                # while not is_e_ok(int(public_key)):
                #     print("This public key can't be used :(\n I recommend \"65537\"")
                #     public_key = input("Choose a public key: ")
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
            elif command == 'delete':
                metadata_table.delete_many({"Name": file_name})
                print("File ", file_name, " deleted!")
            elif command == 'read':
                enc_content_cursor = metadata_table.find({"Name": file_name})
                for enc_content in enc_content_cursor:
                    print("enc: ", enc_content)
                    dc = decrypt(enc_content["Content"])
                    print(dc)
                    print_file = open(file_path, "wb")
                    print_file.write(dc)
                    print_file.close()


while 1:
    menu()
    print("--------------------------------------\n")
