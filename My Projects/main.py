# try:
#     number = int(input("Enter number: "))
#     1/number
# except ValueError:
#     print("Enter number idiot")
# except ZeroDivisionError:
#     print("don't enter 0 idiot")
# except Exception:
#     print("Some think error")
# finally:
#     print("cleanup code")

# detection file
# ------------------------------------------------------
# import os 
# name = input("name of file you want search about it: ")
# print()
# file_path = f"/home/kali/Desktop/Pyhon/My Projects/{name}"
#-------------------------------------------------------
# if os.path.exists(file_path):
#     print("is exists")
# else:
#     print("is not exists")
#-----------------------------------------------------------
# Python writing file = {txt, json, csv}
#--------txt

# employers = ["Abdou","Djamal","Khalil","Ayoub","Chihab"]
# file_name = input("Enter name of file: ")

# file_path = f"/home/kali/Desktop/{file_name}"
# try:
#     with open(file = file_path,mode = "a") as file:
#         for empleeye in employers:
#             file.write(f"{empleeye} \n")
#         print("file is created")
# except FileExistsError:
#     print("Error:the file is aready exists!!!")
#--------- json
# import json
# emplyee = {"name":"Abdou",
#            "age":12}
# file_name = input("Enter name of file: ")
#
# file_path = f"/home/kali/Desktop/{file_name}"
# try:
#     with open(file = file_path,mode = "a") as file:
#         json.dump(emplyee,file)
# except FileExistsError:
#     print("Error:the file is aready exists!!!")
#--------------------------------------------------
# read txt
# file_name = input("Enter name file: ")
# file_path = f"/home/kali/Desktop/{file_name}"
# print("------------------")
# try:
#     with open(file_path,"r") as file:
#         print(file.read())
       
# except FileNotFoundError:
#     print("the file is not found")       
#-----------------------------------------------------
#read json
# import json
# file_name = input("Enter name file: ")
# file_path = f"/home/kali/Desktop/{file_name}"
# print("------------------")
# try:
#     with open(file_path,"r") as file:
#         print(json.load(file))
       
# except FileNotFoundError:
#     print("the file is not found") 
#--------------------------------------------------------
# import datetime