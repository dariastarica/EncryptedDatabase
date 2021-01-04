from Database import metadata_table
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
            file = open(file_path, "r")
            content = file.read()
        except Exception as e:
            print(e)
        else:
            if command == 'add':
                metadata_table.insert_one({
                    # "_id": metadata_table.count_documents()+1,
                    "Name": file_name,
                    "Encryption Method": "RSA",
                    "Public Key": 4324,
                    "Content": crypt(content),
                    "File size": 34243,
                    "ctime": 342,
                    "mtime": 432
                })
            elif command == 'delete':
                metadata_table.delete_many({"Name": file_name})
                print("File ", file_name, "deleted!")
            elif command == 'read':
                enc_content_cursor = metadata_table.find({"Name": file_name})
                for enc_content in enc_content_cursor:
                    print("enc: ", enc_content)
                    print(decrypt(enc_content["Content"]))


menu()

