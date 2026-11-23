students_set = {"Alice", "Bob", "Charlie", "Diana", "Ethan"}
print("Q1:", students_set)

numbers_set = {10, 20, 30, 10, 20, 40}
print("Q2:", numbers_set)  

fruits_set = {"Apple", "Mango", "Orange", "Banana", "Pineapple"}
print("Q3:", fruits_set)

students = set()  
print("Q4:", students)

colors_set = {"Red", "Green", "Blue"}
colors_set.add("Yellow")
print("Q5:", colors_set)

num_set = {10, 20, 30}
num_set.update({40, 50, 60})
print("Q6:", num_set)

class_students = {"Alice", "Bella", "Charlotte", "Davis", "Ethan"}
class_students.remove("Ethan")
print("Q7:", class_students)

basket = {"Apple", "Mango", "Orange"}
basket.discard("Pineapple")  
print("Q8:", basket)

python_students = {"Bella", "Charlotte", "Davis", "Ethan"}
java_students = {"Charlotte", "Davis", "Ethan", "Frank"}
all_students = python_students.union(java_students)
print("Q9:", all_students)

both_languages = python_students.intersection(java_students)
print("Q10:", both_languages)

python_only = python_students.difference(java_students)
print("Q11:", python_only)

exclusive_students = python_students.symmetric_difference(java_students)
print("Q12:", exclusive_students)

names_list = ["John", "Mary", "John", "Victor", "Mary", "David", "Victor"]
unique_names_set = set(names_list)
print("Q13:", unique_names_set)

set_a = {10, 20, 30, 40}
set_b = {30, 40, 50, 60}
common_numbers = set_a.intersection(set_b)
print("Q14:", common_numbers)

teams = {"Arsenal", "Chelsea", "Liverpool", "Manchester United", "Barcelona"}
teams.add("Real Madrid")
teams.add("Bayern Munich")
teams.remove("Chelsea")
print("Q15:", teams)

student_tuple = ("Alice", "Bob", "Charlie", "Diana", "Ethan")
print("Q16:", student_tuple)


my_info = ("Alex", 17, "Greenfield High", "Nigeria")
print("Q17:", my_info)

numbers_tuple = (10, 20, 30, 40, 50)
print("Q18:", numbers_tuple[0])

fruits_tuple = ("Apple", "Mango", "Orange", "Banana", "Pineapple")
print("Q19:", fruits_tuple[2])


names_tuple = ("John", "Mary", "Victor", "David")
print("Q20:", names_tuple[-1])


num_tuple_2 = (10, 20, 30, 40, 50, 60)
print("Q21:", num_tuple_2[1:4])

six_nums = (5, 10, 15, 20, 25, 30)
print("Q22:", six_nums[:3])

print("Q23:", six_nums[2:])

t_fruits = ("Apple", "Mango", "Orange")
l_fruits = list(t_fruits)
print("Q24:", l_fruits)

t_fruits_2 = ("Apple", "Mango", "Orange")
l_fruits_2 = list(t_fruits_2)
l_fruits_2[1] = "Banana"
t_fruits_2 = tuple(l_fruits_2)
print("Q25:", t_fruits_2)

t_nums = (10, 20, 30, 40, 50)
l_nums = list(t_nums)
l_nums[0] = 100
t_nums = tuple(l_nums)
print("Q26:", t_nums)

s_tuple = ("John", "Mary", "Victor", "David", "Peter")
s_list = list(s_tuple)
s_list.append("Sarah")
s_tuple = tuple(s_list)
print("Q27:", s_tuple)

fruit_tuple_dup = ("Apple", "Mango", "Apple", "Orange", "Apple")
print("Q28:", fruit_tuple_dup.count("Apple"))

name_tuple_2 = ("John", "Mary", "Victor", "David")
print("Q29:", name_tuple_2.index("Victor"))

student_info = ("John", 20, "Python", "Nigeria")
print("Q30:")
print("Name:", student_info[0])
print("Age:", student_info[1])
print("Course:", student_info[2])
print("Country:", student_info[3])

print("A set is an unordered collection of unique elements, while a tuple is an ordered collection that can contain duplicate elements.")
print("a set remove duplicate value because it is unordered and does not allow duplicates.")
print("remove() method is used to remove an element from a set, while discard() method is used to remove an element from a set without raising an error if the element does not exist.")
print("union() method is used to combine two sets, intersection() method is used to find common elements between two sets.")
print("tuples are immutable, meaning their elements cannot be changed after creation.")