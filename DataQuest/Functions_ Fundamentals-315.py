## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

sum_manual = 0

for item in a_list:
    sum_manual = int(item) + sum_manual

print(sum_manual)
sum(a_list)

## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}

for item in ratings:
    if item in content_ratings:
        content_ratings[item] += 1
    else:
        content_ratings[item] = 1
        
print(content_ratings)

## 3. Creating Our Own Functions ##

def square(number):
    return number * number

squared_10 = square(10)
squared_16 = square(16)

## 4. The Structure of a Function ##

def add_10(number):
    return number + 10

add_30 = add_10(30)
add_90 = add_10(90)

## 5. Parameters and Arguments ##

def square(num):
    return num * num

squared_6 = square(6)
squared_11 = square(11)

## 6. Extract Values From Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(col):
    list = []
    for item in apps_data[1:]:
        list.append(item[col])
    return list

genres = extract(11)

print(genres)
        

## 7. Creating Frequency Tables ##

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)

def freq_table(list):
    empty_dict = {}
    for item in list:
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1
            
    return empty_dict
            
genres_ft = freq_table(genres)
print(genres_ft)

## 8. Writing a Single Function ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(col):
    empty_dict = {}
    for row in apps_data[1:]:
        item = row[col]
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1
    return empty_dict

ratings_ft = freq_table(7)

print(ratings_ft)



## 9. Reusability and Multiple Parameters ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# INITIAL FUNCTION
def freq_table(index, data_set):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

ratings_ft = freq_table(7, apps_data)

## 10. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_ratings_ft = freq_table(apps_data, 10)
ratings_ft = freq_table(data_set=apps_data, index=7)
genres_ft = freq_table(index=11, data_set=apps_data)


## 11. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    extract_data = extract(apps_data, index)
    return find_sum(extract_data) / find_length(extract_data)
    
avg_price = mean(apps_data, 4)

## 12. Debugging Functions ##

# INITIAL CODE
def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)