#This program takes distance in km or miles and coverts the input into it's equivalent miles or km respectively

print("This program takes distance in km or miles and coverts the input into it's equivalent miles or km respectively")

unit_of_distance = input("To convert  distance into Kilometers enter \"Km\" or enter \"miles\" for converting distance in miles: ")

distance_before_conversion = -1.0


while unit_of_distance != "km" and unit_of_distance != "miles":
    unit_of_distance = input("To convert  distance into Kilometers enter \"Km\" or enter \"miles\" for converting distance in miles: ")
    



while distance_before_conversion <=  0.0:
    try:
        distance_before_conversion = float(input(f'Please enter the distance in {unit_of_distance}: '))
    except:
        distance_before_conversion = float(input(f'Please enter the distance in {unit_of_distance}: '))



if unit_of_distance == "km":
    distance_after_conversion = distance_before_conversion * 1.6
    print(f'{distance_before_conversion} miles = {distance_after_conversion} {unit_of_distance}')
else:
    distance_after_conversion = distance_before_conversion / 1.6
    print(f'{distance_before_conversion} Km = {distance_after_conversion} {unit_of_distance}')








 

