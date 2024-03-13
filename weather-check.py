temp = 70
forecast = "sunny"
raining = False

if temp > 80:
    print("It's too high!")
    print("Stay inside!")
elif temp < 60:
    print("It's too =low!")
    print("Stay inside!")
else:
    print("Enjoy outdoors!")

if temp < 80 and forecast != "rainy":
    print("Go outside!")
else:
    print("Stay Indoors!")

if not raining:
    print("Go outside and have fun!")
else:
    print("Stay indoors!")