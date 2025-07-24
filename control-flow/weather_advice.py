def main():
    weather = input("How is the weather today? (sunny/rainy/cold/snowy/windy/cloudy): ").strip().lower()

    if weather == "sunny":
        print("It's sunny out! Wear sunglasses, a hat, and light clothing.")
    elif weather == "rainy":
        print("It's rainy. Don't forget an umbrella and a waterproof jacket.")
    elif weather == "cold":
        print("It's cold. Wear a warm coat and maybe some gloves.")
    elif weather == "snowy":
        print("It's snowy. Bundle up with a heavy coat, gloves, and a warm scarf.")
    elif weather == "windy":
        print("It's windy. A windbreaker and layers are a good idea.")
    elif weather == "cloudy":
        print("It's cloudy. You might want a light jacket just in case.")
    else:
        print("Hmm, I'm not familiar with that weather—dress comfortably and check the forecast!")

if __name__ == "__main__":
    main()
