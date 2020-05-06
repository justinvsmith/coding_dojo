#1.
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1 
x[1][0] = 15

#2
students[0]['last_name']="Bryant"

#3
sports_directory['soccer'][0] = "Andres"

#4
z[0]['y']=30


#2.
def iterateDictionary(some_list):
    for a in range(len(some_list)):
        index = some_list[a]
        for x, y in index.items():
            print(f"{x} - {y}")

# def iterateDictionary(students):
#     #this is going to loop through each item in the list, called students
#     for item in students: 
#         #to loop through the keys of items
#         for key in item:
#             print(key + " - " + item[key])
#             print(f"{key} - {item[key]}")

#to print fancy: 
def iterateDictionary(students):
    #this is going to loop through each item in the list, called students
    for item in students: 
        toPrint = ""
        for key in item:
            toPrint += f"{key} - {item[key]},"
        print(toPrint    )

#3.
def iterate2(key_name,some_list):
    for i in range(len(some_list)):
        print(some_list[i][f"{key_name}"])

    for item in some_list
        print(item[key_name])

#4.
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        length = len((some_dict[key]))
        print(f"\n{length} {key}".upper())
        for x in range(len(some_dict[key])):
            print(some_dict[key][x])
        

printInfo(dojo)


for key, value in some_dict:
    print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)



