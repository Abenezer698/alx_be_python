# alx_be_python

# weather_advice.py

def main():
    print("Welcome to the Weather Advice Program!")
    print("Please enter the current weather condition.")
    print("Options: sunny, rainy, cold, windy, snowy")

    weather = input("What's the weather like today? ").lower()

    if weather == "sunny":
        print("It's sunny! Wear light clothes and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and wear waterproof shoes.")
    elif weather == "cold":
        print("It's cold outside. Wear a warm coat, gloves, and a hat.")
    elif weather == "windy":
        print("Wear a windbreaker or jacket to stay comfortable.")
    elif weather == "snowy":
        print("Bundle up! Wear a thick coat, boots, and a scarf.")
    else:
        print("Sorry, I don't have advice for that kind of weather.")

if __name__ == "__main__":
    main()
