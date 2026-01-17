import module

"""We have file module.py with some code. Use this module in your script to print the state of the water 
if its temperature is determined with input from the user. We assume that the freezing point is 0 degrees 
and the boiling point is 100 degrees."""


module.BOILING_POINT = 100
module.FREEZING_POINT = 0
temperature = int(input('Please, enter the water temperature '))
module.print_water_state(temperature)