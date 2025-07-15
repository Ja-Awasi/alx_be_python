# Weather conditions
weather = input("What is the weather like today? (sunny/ rainy/ cloudy): ").lower()
# Clothing recomendations based on weather
if weather == "sunny":
    print("wear a t-shirt and sunglasses")
elif weather == "rainy":
    print(" Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")