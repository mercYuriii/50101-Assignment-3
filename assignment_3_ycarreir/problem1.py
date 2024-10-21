# Problem 1
#
# Yuri Carreira Alflen

# Receive input in Fahrenheit
fahrenheit = (input("Enter a temperature in Fahrenheit: "))


def fahrenheit_to_celsius(f):
# Apply temperature conversion
# Check if input is a whole number numeric temperature
    try:
        fahrenheit_integer = int(f)
        # Math to convert Fahrenheit to Celsius https://www.geeksforgeeks.org/fahrenheit-to-celsius-formula/
        celsius = round(((fahrenheit_integer - 32) * 5/9),2)
        return print("The temperature is %.2f in Celsius." % (celsius))
        
    except:
        return print("Please enter a whole number numeric temperature.")

fahrenheit_to_celsius(fahrenheit)
