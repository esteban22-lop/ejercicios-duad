#Diccionarios_1

#create a dictioanry that saves info about a hotel

hotel_info = {
    "Name": "Barcelo_Tambor",
    "Ranking": 5,
    "Rooms": [
        {"number":101, "floor": 1,"price_by_night": 75000 },
        {"number":230, "floor": 2,"price_by_night": 90000},
        {"number":420, "floor": 4,"price_by_night": 120000},
    ],
    
}

#Print of the whole dictionary
print(hotel_info)

#Access to hotel info

print("Hotel:", hotel_info["Name"])
print("Ranking:", hotel_info["Ranking"])

#total of rooms
print("Total of rooms: ", len(hotel_info["Rooms"]))

#If we want to add a new room:

new = {"number":500, "floor": 5,"price_by_night": 200000}
hotel_info["Rooms"].append(new)
print("A new room is available", len(hotel_info["Rooms"]),"rooms.")

#I used append because we got a list inside of this dictionary

