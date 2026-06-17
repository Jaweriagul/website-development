city=input("Enter the city name: ")
temperature=float(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("The weather in", city, "is hot.")
elif temperature <= 25:
    print("The weather in", city, "is pleasant.")
elif temperature <= 10:
    print("The weather in", city, "is cold.")
else:
    print("The weather in", city, "is moderate.")
import datetime
now=datetime.datetime.now()
print("current date and time:", now)