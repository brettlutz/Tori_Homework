def celsius_to_fahrenheit(temp):
    return (temp - 32) * 5/9


def fahrenheit_to_celsius(temp):
    return (9 / 5) * temp + 32


def is_a_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def calculate_windchill(temp, type):
    print("\n")
    if (not is_a_number(temp)):
        print("** You have entered and invalid temperature. **")
        start()
        return
    beginning_temp = float(temp)
    if type.lower() == 'c':
        beginning_temp = celsius_to_fahrenheit(beginning_temp)
    for speed in list(range(5, 65, 5)):
        chill = 35.74 + 0.6215 * beginning_temp - 35.75 * \
            speed**0.16 + 0.4275 * beginning_temp * speed**0.16
        print(
            f"At temperature {'{: .2f}'.format(beginning_temp)}°F, and wind speed of {speed} mph, the windchill is: {'{: .2f}'.format(chill)}°F")


def start():
    temperature = input("\nWhat is the temperature? ")
    celsius_fahrenheit = input("Fahrenheit or Celsius (F/C)? ")
    calculate_windchill(temperature, celsius_fahrenheit)


start()
