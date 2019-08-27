zoo = ("pig","cow","dog","rabbit","goat","fish","horse","cat","mouse","snake")
print (zoo.index("rabbit"))
# find an animal in zoo and display if the animal is in the list or not
animal_to_find = "giraffe"
if animal_to_find in zoo:
    print(animal_to_find.capitalize(), " is in the list.")
else:
        print(animal_to_find.capitalize(), "is not in the list.")

(first_animal,second_animal,third_animal,fourth_animal,fifth_animal,sixth_animal,seventh_animal,eighth_animal,nineth_animal,tenth_animal) = zoo
print (first_animal)
print (second_animal)
print (third_animal)
print (fourth_animal)
print (fifth_animal)
print (sixth_animal)
print (seventh_animal)
print (eighth_animal)
print (nineth_animal)
print (tenth_animal)
# convert tuple to a list
zoo = list(zoo)
print(f'Zoo is now a list: ', list(zoo))
new_animal = ["iguana","racoon","kangaroo"]
# Use extend() to add three more animals to your zoo
zoo.extend(new_animal)
print(f'Zoo has been extended with 3 new animals!', zoo)