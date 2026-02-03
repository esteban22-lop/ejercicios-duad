#Diccionarios_3

keys_list = ["first","second","third","last_one"]

my_dictionary = {
    'first': 1,
    'second': 2,
    'third': 3,
}

for keys in keys_list:
    my_dictionary.pop(keys, None)
    

print(my_dictionary)

#I added another key to see if it prints none in case the key does not exist, but just prints {}
#I don't know if this is correct, but let me know about it, please :) 