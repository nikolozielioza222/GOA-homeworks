#Flight time
print("Your are at the airport and u need to calculate the flight time of and upcoming trip. You are flying to LA to Sydney,coering a distance of 7425 miles and the plane flies at and average speed of 550 miles an hour.")

print(7425 / 550)











print("You are making a program that needs to calculate the points earned by a player in a chess tournament.A win is worth 1 point while a tie is worth 0.5 points.The given prgram declares two variables <b>wins</b> and <b>ties</b>")

win = input()
tie = input()

sum_points = win * 1 + tie * 0.5

wins = 5
ties = 3 

sum_points = wins * 1 + ties * 0.5

print("Total points earned:", sum_points)








print("You need to make a program to create country cards in which the names of the country and the capital are displayed")

print("country: ")
print("capital: ")

country_cards = [
    {"country": "France", "capital": "Paris"},
    {"country": "georgia", "capital": "Tbilisi"},
]

def display_country_cards(cards):
    for card in cards:
        print(f"Country: {card['country']}")
        print(f"Capital: {card['capital']}")
        print("-" * 20)  

display_country_cards(country_cards)
