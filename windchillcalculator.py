

## based on National Weather Service's the formula to calculate wind chill is 35.74 + 0.6215T – 35.75(V**0.16) + 0.4275T(V**0.16).
def calculate_wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temperature * (wind_speed ** 0.16))
    return wind_chill

def WindChillCalculator():
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    if unit == 'C':
        temperature = (temperature * 9/5) + 32
    
    wind_speeds = range(5, 61, 5)

    for wind_speed in wind_speeds:
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

WindChillCalculator()
