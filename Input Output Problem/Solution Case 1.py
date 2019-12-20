dictionary = {
"G": "C",
"C": "G",
"T": "A",
"A": "U"
}
string = input("").upper()
output = ""
for item in string:
    
    if item in dictionary:
        item = dictionary[item]
        output = output + item
    else:
        print("Invalid Input")
        exit()
print(output)