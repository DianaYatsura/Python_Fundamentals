temperature_Celsius = int(input('Enter the temperature in Celsius: '))
if temperature_Celsius > -273.15:
    print(f'{temperature_Celsius}{chr(176)}C is equivalent to {temperature_Celsius*9/5 + 32}{chr(176)}F')
else:
    print(f'Temperature is below absolute zero (-273.15{chr(176)}C)')