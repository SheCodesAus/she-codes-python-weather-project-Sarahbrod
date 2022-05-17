import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    date_new = datetime.strftime(date, "%A %d %B %Y")
    return date_new


def convert_f_to_c(temp_in_fahrenheit):
    """Converts an temperature from fahrenheit to celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_fahrenheit = float(temp_in_fahrenheit)
    temp_in_celsius = round((temp_in_fahrenheit - 32) * (5 / 9), 1)
    return temp_in_celsius


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data_float = [float(i) for i in weather_data]
    total = sum(weather_data_float)
    mean = total / len(weather_data_float)
    return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    csv_list = []
    with open(csv_file, encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if len(line) > 0:
                csv_list.append(line)
    return csv_list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if len(weather_data) == 0:
        return ()

    min_value = min(weather_data)
    min_index = weather_data.index(min(weather_data))

    idx = -1
    idx_list = []
    for num in weather_data:
        idx += 1
        if num == min(weather_data):
            idx_list.append(idx)

    min_index = idx_list[-1]

    return float(min_value), min_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data) == 0:
        return ()

    max_value = max(weather_data)
    max_index = weather_data.index(max(weather_data))

    idx = -1
    idx_list = []
    for num in weather_data:
        idx += 1
        if num == max(weather_data):
            idx_list.append(idx)

    max_index = idx_list[-1]
    return float(max_value), max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
