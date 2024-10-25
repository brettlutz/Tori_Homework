# Victoria Lutz
from pathlib import Path

maximum = 0
minimum = 100
minimum_country = ''
maximum_country = ''
min_year = ''
max_year = ''
# TODO from dad. I added these variables
year_sum = 0
year_count = 0
year_average = 0

file_path = Path('../life-expectancy.csv')
text = file_path.read_text().rstrip()
lines = text.splitlines()
# TODO from dad. I added this input
year_input = input("Enter the year of interest: ")

for index, line in enumerate(lines):
    if index > 0:
        parts = line.split(',')
        country = parts[0]
        code = parts[1]
        year = parts[2]
        life_expectancy = float(parts[3])
        if life_expectancy < minimum:
            minimum = life_expectancy
            minimum_country = country
            min_year = year
        if life_expectancy > maximum:
            maximum = life_expectancy
            maximum_country = country
            max_year = year
        # TODO from dad. I added this if statement. Getting the year minimum and
        # maximum would be handled in this if statement
        if year == year_input:
            # we start year_sum = 0, and now if the years match we add the life expectancy to the sum
            year_sum += life_expectancy
            # to take an average you have to know how many items you added together, so this starts at 0
            # and we add 1 each time the years match
            year_count += 1

print(
    f'The max life expectancy was in {maximum_country} with {maximum} in the year {max_year}')
print(
    f'The minimum life expectancy was in {minimum_country} with {minimum} in the year {min_year}')

# TODO from dad. I added the code below. Here we check if the year_count is 0, because if it
# is then dividing by it will result in an error. You can't divide by zero.
if year_count > 0:
    year_average = year_sum / year_count
    print(f"For the year {year_input}:")
    print(
        f"The average life expectancy across all countries was {year_average}")
    # TODO from dad. Have a year_minimum, year_minimum_country, year_maximum,
    # and year_maximum_country that you set like you do the other minimum, and
    # maximum. Then print out "The max life expectancy was in {country} with {year_maximum}",
    # and "The min life expectancy was in {country} with {year_minimum}"
else:
    print("There is no data available for the year you entered. ")

# TODO from dad. PEP TALK. You are doing very good. You took my hints and were
# pretty close to get this initially working. They are trying to teach you the basics
# and Google is trying to teach you the easy way to do it. Data Analysis is really
# just about going through each piece of data, and comparing it to the other pieces.
# You know how to do that, it's a loop! Then you just have to remember variable scope,
# and where you can access certain variables at. Your print statements can't happen until
# after the loop, so the variables need to be declared outside the loop. This assignment
# seems hard because you are opening a file and using the data inside it, and that makes
# it seem like you are going to need new special ways to do things, but just remember that
# all of the data is just different variables and you know how to use those. You got this!
# TODO from dad. END PEP TALK
