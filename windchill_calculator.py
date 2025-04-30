# W07 Project: Windchill Calculator
# Author: Blessing Glory Tsikey
# This program calculates wind chill based on temperature and wind speed. 
# It allows temperature input in either Fahrenheit or Celsius.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate_wind_chill(temp_f, wind_speed):
    return 35.74 + (0.6215 * temp_f) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp_f * (wind_speed ** 0.16))

temperature = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

if unit == "C":
    temperature = celsius_to_fahrenheit(temperature)

for wind_speed in range(5, 65, 5):
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")
