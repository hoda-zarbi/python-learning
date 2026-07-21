"""
Topic: Input and Output
Example: Weather Observation Log

This file demonstrates how to receive input from the user
and display the information using print().
"""

print(" Weather Observation Log ")
print()

# Receive weather information from the user
location = input("Enter the observation location: ")
temperature = input("Enter the temperature (°C): ")
humidity = input("Enter the humidity (%): ")
weather_condition = input("Enter the weather condition: ")
observation_date = input("Enter the observation date: ")

print()

# Display the weather observation report
print("==== Weather Observation Report ====")
print("Location:", location)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Weather Condition:", weather_condition)
print("Observation Date:", observation_date)
