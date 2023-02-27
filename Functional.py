people = [
    {"name":"Paula Key", "age":23},
     {"name":"Riya Dickerson" , "age":99},
     {"name":"Layne Colon" , "age":53},
     {"name":"Pranav Giles" , "age":51},
     {"name":"Kamryn Davis" , "age":27},
     {"name":"Taniyah Yu" , "age":17},
     {"name":"Brendon Porter" , "age":23},
     {"name":"Jordin Hancock" , "age":86},
     {"name":"Shawn Vargas" , "age":88},
     {"name":"Sawyer Copeland" , "age":14},
     {"name":"Gustavo Baldwin" , "age":7},
     {"name":"Renee Wilson" , "age":29}
]

#1
def reduce(function, sequence, initial=None):
    if initial is None:
        result = sequence[0]
        start = 1
    else:
        result = initial
        start= 0
    for i in range(start, len(sequence)):
        result = function(result, sequence[i])
        return result
    

count = reduce(lambda x, y: x + (y["age"] > 50), people, 0)

print(count)

#2

def forEach(function, sequence):
    for item in sequence:
        function(item)

persons = ["Paula Key","Riya Dickerson", "Layne Colon", "Pranav Giles", "Kamryn Davis", "Taniyah Yu", "Brendon Porter", "Jordin Hancock", "Shawn Vargas", "Sawyer Copeland", "Gustavo Baldwin", "Renee Wilson"]

def greet_person(person):
    print("Hi, " + person + "!")

forEach(greet_person, persons)

#3

def map(function, sequence):
    result = []
    for item in sequence:
        result.append(function(item))
    return result

def make_older(person):
    person["age"] += 1
    return person

people_older = map(make_older, people)

print(people_older)

#4

def filter(function, sequence):
    result = []
    for item in sequence:
        if function(item):
            result.append(item)
    return result

drinking_age = 18

def under_drinking_age(person):
    return person["age"] < drinking_age

underage_people = filter(under_drinking_age, people)

print(underage_people)

#5

def sum(sequence):
    total = 0
    for item in sequence:
        total += item
    return total

total_age = sum(map(lambda person: person["age"], people))

print(total_age)

#6

def average(sequence):
    if len(sequence) == 0:
        return None
    total = sum(sequence)
    return total / len(sequence)

average_age = average(list(map(lambda person: person["age"], people)))

print(average_age)

#7

def max(sequence):
    if len(sequence) == 0:
        return None
    current_max = sequence[0]
    for item in sequence:
        if item > current_max:
            current_max = item
    return current_max

def min(sequence):
    if len(sequence) == 0:
        return None
    current_min = sequence[0]
    for item in sequence:
        if item < current_min:
            current_min = item
    return current_min

ages = list(map(lambda person: person["age"], people))

min_age = min(ages)
max_age = max(ages)

print("Minimum age:", min_age)
print("Maximum age:", max_age)






