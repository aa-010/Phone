import json
def Parsing(str):

    book = []   
 
    startIndex = 0
    index = 0

    while str.find('{', startIndex) != -1:
        
        tempStr = str[str.find('{', startIndex): str.find('}', startIndex) + 1]
        #print(tempStr)
        book.append(json.loads(tempStr))
        #temp_dict = {"Name": book[index].pop("_Contact__firsName"), "Last Name": book[index].pop("_Contact__lastName"), "phone": book[index].pop("_Contact__phone")}
        #book.insert(index, temp_dict)
        #index += 1
        startIndex = (str.find('}', startIndex)) + 1
        
    for index in range(len(book)):
        temp_dict = {"NAME": book[index]["_Contact__firsName"], "LAST NAME": book[index]["_Contact__lastName"], "PHONE": book[index]["_Contact__phone"]}
        book[index] = temp_dict

    return book
