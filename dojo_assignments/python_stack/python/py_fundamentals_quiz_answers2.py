# Number 3 Part 1
hero = {
    'name': 'Superman',
    'powers': ['flight', 'superhuman strength', 'x-ray vision']
}
# print the statement "Superman has x-ray vision" using string interpolation
print(f"{} has {}")

** print(f"{hero['name']} has {hero['powers'][2]}")


# Number 3 Part 2
boy_wizard = {
    'name': 'Harry Potter',
    'student_info': {
        'house': 'Gryffindor', 
        'year': 1
    }
}

# print the statement "Harry Potter is a 1st year in Gryffindor"

print(f"{} is a {}st year in {}")

** print(f"{boy_wizard['name']} is a {boy_wizard['student_info']['year']}st year in {boy_wizard['student_info']['house']}")


# Number 3 Part 3

books = [
    {
        'title': 'Pride and Prejudice',
        'authors': [
            {
                'name': 'Jane Austen',
                'birth_year': 1775
            }
        ],
        'pub_year': 1813
    },
    {
        'title': 'Pride and Prejudice and Zombies', 
        'authors': [
            {
                'name': 'Jane Austen',
                'birth_year': 1775
            },
            {
                'name': 'Seth Grahame-Smith',
                'birth_year': 1976
            }
        ],
        'pub_year': 2009
    }
]


# Print the statement "Pride and Prejudice was written by Jane Austen in 1813"

print(f"{} was written by {} in {}.")

** print(f"{books[0]['title']} was written by {books[0]['authors'][0]['name']} in {books[0]['pub_year']}")

# Print the statement "Pride and Prejudice and Zombies was written by Seth Grahame-Smith in 2009."

print(f"{} was written by {} in {}.")

** print(f"{books[1]['title']}, was written by {books[1]['authors'][1]['name']} in {books[1]['pub_year']}")













