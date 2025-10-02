# TODO: Create a list of your favorite fruits
# TODO: Add a new fruit to the end of the list
# TODO: Remove the second fruit from the list
# TODO: Sort the list alphabetically
# TODO: Create a new list with the first three fruits
# Print the original list and the new list

Fruits = ["Mango", "Apple", "strawberry", "orange"]
Fruits.append("pineapple")
Fruits.pop(1)
Fruits.sort()
top3 = Fruits[:3]
# print("original list: ", Fruits)
# print("top 3:", top3)

# TODO: Create a tuple with your favorite colors
# TODO: Try to modify one of the colors (this should raise an error)
# TODO: Count how many times a specific color appears in the tuple
# TODO: Find the index of a specific color
# TODO: Create a new tuple by concatenating two existing tuples
# Print the results of each operation

colors = ("Black", "Red", "Green", "Blue")
count_blue = colors.count("Blue")

# print(colors.index("Green"))

newcolors = ("purple", "white")
combined = colors + newcolors

# print(combined)

# TODO: Create a dictionary representing a person (name, age, city)
# TODO: Add a new key-value pair for the person's occupation
# TODO: Update the person's age
# TODO: Remove the 'city' key-value pair
# TODO: Print all keys, then all values
# TODO: Check if a specific key exists in the dictionary
# Print the final dictionary

person = {
    "name": "Kevin",
    "age": 25,
    "city": "Compiègne"
}
person["occupation"] = "étudiant"
person["age"] = 26
person.pop("city")

# print("Keys:", person.keys())
# print("Values:", person.values())

# print("age" in person)
# print("city" in person)
# print("final dict:", person)


# TODO: Create two sets of numbers
# TODO: Find the union of the two sets
# TODO: Find the intersection of the two sets
# TODO: Find the difference between the first and second set
# TODO: Add a new element to one of the sets
# TODO: Remove an element from one of the sets
# Print the results of each operation

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
# print(union_set)

intersec_set = set1.intersection(set2)
# print(intersec_set)

difference_set = set1.difference(set2)
# print(difference_set)

set2.add(10)
set1.remove(4)

# print(set1, set2)

# TODO: Create a list of dictionaries representing books (title, author, year)
# TODO: Add a new book to the list
# TODO: Sort the list of books by year
# TODO: Create a dictionary where keys are authors and values are lists of their books
# TODO: Print all books by a specific author
# Print the final nested data structure

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
]
books.append({"title": "Animal Farm", "author": "George Orwell", "year": 1945})
books.sort(key=lambda x: x["year"])
