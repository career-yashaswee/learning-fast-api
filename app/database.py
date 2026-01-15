import json 

books = {}

print("before load : ",books)
with open("books.json") as json_file:
    data = json.load(json_file)

    for value in data:
        books[value["id"]] = value

print("after load : ",books)