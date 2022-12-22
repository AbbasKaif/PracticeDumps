#Develop a program in python to create a dictionary of five elements. Now traverse the dictionary.
print("Develop a program in python to create a dictionary of five elements. Now traverse the dictionary.\n")
mydict={"1":'Nokia',"2":"Samsung","3":'Vivo',"4":"Oppo","5":'Hawaii'}
print("List of mobile brands.")
for key,value in mydict.items():
    print(key,":",value)