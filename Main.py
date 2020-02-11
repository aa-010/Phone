import json

from Menu import MainMenu
from Contact import Contact
from Fun import Parsing

menuItems = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]


#c1 = Contact("Name1","Lastname1", "1111-11-11")
#c2 = Contact("Name2","Lastname2", "2222-22-22")
#c3 = Contact("Name3","Lastname3", "3333-33-33")
#c4 = Contact("Name4","Lastname4", "4444-44-44")
#c5 = Contact("Name5","Lastname5", "5555-55-55")

#myfile = open("file.txt", "w")

#json.dump(c1.__dict__, myfile)
#json.dump(c2.__dict__, myfile)
#json.dump(c3.__dict__, myfile)
#json.dump(c4.__dict__, myfile)
#json.dump(c5.__dict__, myfile)

#myfile.close()


myfile = open("file.txt", "r")

book = myfile.read()
book = Parsing(book)

MainMenu(menuItems)

myfile.close()

change_item = MainMenu(book)

for index in range(len(book)):
    book[index] = Contact(book[index]["NAME"], book[index]["LAST NAME"], book[index]["PHONE"])

book[change_item].rename()
book.append(Contact("New Name","NEW Lastname5", "XXXX-XX-XX"))


myfile = open("file.txt", "w")

for i in range(len(book)):
    json.dump(book[i].__dict__, myfile)

myfile.close()

#print(type(temp))
#print(temp)

#print(type(book))
#myfile.close()
#myfile = open("file.txt", "w")

#c6 = Contact(book[1]["_Contact__firsName"],book[1]["_Contact__lastName"])
#json.dump(c6.__dict__, myfile)

