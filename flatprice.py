total_area = int(input("Enter total area: "))
people = 5

room1 = int(input("Enter the area of room 1: "))
room2 = int(input("Enter the area of room 2: "))
room3 = int(input("Enter the area of room 3: "))
room4 = int(input("Enter the area of room 4: "))
room5 = int(input("Enter the area of room 5: "))

rooms = [room1, room2, room3, room4, room5]

price = int(input("Enter the rent per month: "))

price_meter = price / total_area

communal_area = total_area - sum(rooms)
communal_price = communal_area * price_meter

print(price_meter)

def cost_for_room(r):
    proportional_area = r / sum(rooms)
    return price * proportional_area

person1 = communal_price + cost_for_room(room1)
person2 = communal_price + cost_for_room(room2)
person3 = communal_price + cost_for_room(room3)
person4 = communal_price + cost_for_room(room4)
person5 = communal_price + cost_for_room(room5)

print("The person in room 1 should pay " + str(cost_for_room(room1)))
print("The person in room 2 should pay " + str(cost_for_room(room2)))
print("The person in room 3 should pay " + str(cost_for_room(room3)))
print("The person in room 4 should pay " + str(cost_for_room(room4)))
print("The person in room 5 should pay " + str(cost_for_room(room5)))



