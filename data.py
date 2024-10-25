# Victoria Lutz


import pathlib
from pathlib import Path

maximum = 0
minimum = 100
minimum_country = ''
maximum_country = ''

input_country_max = ''
input_country_min = ''
min_year = ''
max_year = ''
year_maximum = 0
# TODO from dad. You want this to start high so it will decrease
year_minimum = 100
year = 0
year_sum = 0
year_count = 0
year_average = 0


file_path = Path('../life-expectancy.csv')
text = file_path.read_text()
lines = text.splitlines()

year_input = int(input('Please enter the year of interest: '))


for index, line in enumerate(lines):

    if index > 0:
        parts = line.split(',')
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        if life_expectancy < minimum:
            minimum = life_expectancy
            minimum_country = country
            min_year = year

        if life_expectancy > maximum:
            maximum = life_expectancy
            maximum_country = country
            max_year = year

        if year_input == year:
            year_sum += life_expectancy
            year_count += 1
            # TODO from dad. I moved the if statements up here. Down below it is outside
            # the loop. The if statement is on the same column as the for loop that's why it
            # only hit zimbabwe
            if life_expectancy < year_minimum:
                year_minimum = life_expectancy
                input_country_min = country
            if life_expectancy > year_maximum:
                year_maximum = life_expectancy
                input_country_max = country

# TODO from dad. you removed two print statements here that showed the overall min and max
# I copied these back over from your original file.
print(
    f'The max life expectancy was in {maximum_country} with {maximum} in the year {max_year}')
print(
    f'The minimum life expectancy was in {minimum_country} with {minimum} in the year {min_year}')

if year_count > 0:
    year_average = year_sum / year_count

    print(f"For the year {year_input}:")
    # TODO from dad. You might want to do some formatting here, like indent everything after
    # the year with a \t in the print statement to group the year specific data. maybe add some \n
    # to give some space to make it more readable
    print(
        f"The average life expectancy across all countries was {year_average}")
    print(
        f'"The max life expectancy was in {input_country_max} with {year_maximum}"')
    print(
        f'The min life expectancy was in {input_country_min} with {year_minimum}')
else:
    print("There is no data available for the year you entered. ")
