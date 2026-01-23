
"""
=================================================================================
This function is the general function that asks the user the type of conversion
they want to perform. Once the function receives the right selection, then it
directs the user to the specific function.
=================================================================================
"""

def get_conversion():
    while True:
        print("""What type of conversion do you want to do? 
        1. Length Conversion
        2. Area Conversion
        3. Volume Conversion
        4. Mass/Weight Conversion
        5. Time Conversion
        6. Temperature Conversion
        """)
        type_of_conversion = input("Enter your selection (1 - 6): ")
        print("\n")

        if type_of_conversion.isdigit():
            type_of_conversion = int(type_of_conversion)

            if 1 <= type_of_conversion <= 6:
                if type_of_conversion == 1:
                    length_converter()
                elif type_of_conversion == 2:
                    area_converter()
                elif type_of_conversion == 3:
                    volume_converter()
                elif type_of_conversion == 4:
                    mass_weight_converter()
                elif type_of_conversion == 5:
                    time_converter()
                else:
                    temperature_converter()

                break
            else:
                print("Please enter a number between 1 and 6")
        else:
            print("Please enter a valid number: ")

    return

"""
=================================================================================
"""



"""
======================================================================================
This is the complete Length converter. The length_converter function takes
the user choice and directs the operations to the specific function.
=======================================================================================
"""

def length_converter():
    while True:
        print("""Welcome to Length Converter. What conversion do you want to do? 
        1. Kilometers to Meters
        2. Kilometers to Centimeters
        3. Kilometers to Millimeters
        4. Meters to Kilometers
        5. Meters to Centimeters
        6. Meters to Millimeters
        7. Centimeters to Meters
        8. Centimeters to Millimeters
        9. Centimeters to Kilometers
        10. Millimeters to Meters
        11. Millimeters to Centimeters
        12. Millimeters to Kilometers
        """)

        type_of_length = input("Enter your selection (1 - 12): ")
        print("\n")

        if type_of_length.isdigit():
            type_of_length = int(type_of_length)

            if 1 <= type_of_length <= 12:
                if type_of_length == 1:
                    kilometers_to_meters()
                elif type_of_length == 2:
                    kilometers_to_centimeters()
                elif type_of_length == 3:
                    kilometers_to_millimeters()
                elif type_of_length == 4:
                    meters_to_kilometers()
                elif type_of_length == 5:
                    meters_to_centimeters()
                elif type_of_length == 6:
                    meters_to_millimeters()
                elif type_of_length == 7:
                    centimeters_to_meters()
                elif type_of_length == 8:
                    centimeters_to_millimeters()
                elif type_of_length == 9:
                    centimeters_to_kilometers()
                elif type_of_length == 10:
                    millimeters_to_meters()
                elif type_of_length == 11:
                    millimeters_to_centimeters()
                else:
                    millimeters_to_kilometers()

                break

            else:
                print("Please enter a number between 1 and 12")
        else:
            print("Please enter a valid number: ")

    return


def kilometers_to_meters():
    kilometers = input("Enter the value in Kilometers: ")
    if kilometers.isdigit():
        kilometers = int(kilometers)
        meters = kilometers * 1000
        print(f"{kilometers} kilometers is equal to {meters} Meters")
    else:
        print("Please enter a valid number!!!")

    return


def kilometers_to_centimeters():
    kilometers = input("Enter the value in Kilometers: ")
    if kilometers.isdigit():
        kilometers = int(kilometers)
        centimeters = kilometers * 100000
        print(f"{kilometers} kilometers is equal to {centimeters} Centimeters")
    else:
        print("Please enter a valid number!!!")
    return


def kilometers_to_millimeters():
    kilometers = input("Enter the value in Kilometers: ")
    if kilometers.isdigit():
        kilometers = int(kilometers)
        millimeters = kilometers * 1000000
        print(f"{kilometers} kilometers is equal to {millimeters} Millimeters")
    else:
        print("Please enter a valid number!!!")
    return

def meters_to_kilometers():
    meters = input("Enter the value in Meters: ")
    if meters.isdigit():
        meters = int(meters)
        kilometers = meters / 1000
        print(f"{meters} Meters is equal to {kilometers} Kilometers")
    else:
        print("Please enter a valid number!!!")
    return


def meters_to_centimeters():
    meters = input("Enter the value in Meters: ")
    if meters.isdigit():
        meters = int(meters)
        centimeters = meters * 100
        print(f"{meters} Meters is equal to {centimeters} Centimeters")
    else:
        print("Please enter a valid number!!!")
    return


def meters_to_millimeters():
    meters = input("Enter the value in Meters: ")
    if meters.isdigit():
        meters = int(meters)
        millimeters = meters * 1000
        print(f"{meters} Meters is equal to {millimeters} Millimeters")
    else:
        print("Please enter a valid number!!!")
    return


def centimeters_to_meters():
    centimeters = input("Enter the value in Centimeters: ")
    if centimeters.isdigit():
        centimeters = int(centimeters)
        meters = centimeters / 100
        print(f"{centimeters} Centimeters is equal to {meters} Meters")
    else:
        print("Please enter a valid number!!!")
    return


def centimeters_to_millimeters():
    centimeters = input("Enter the value in Centimeters: ")
    if centimeters.isdigit():
        centimeters = int(centimeters)
        millimeters = centimeters * 10
        print(f"{centimeters} Centimeters is equal to {millimeters} Millimeters")
    else:
        print("Please enter a valid number!!!")
    return


def centimeters_to_kilometers():
    centimeters = input("Enter the value in Centimeters: ")
    if centimeters.isdigit():
        centimeters = int(centimeters)
        kilometers = centimeters / 100000
        print(f"{centimeters} Centimeters is equal to {kilometers} Kilometers")
    else:
        print("Please enter a valid number!!!")
    return


def millimeters_to_meters():
    millimeters = input("Enter the value in Millimeters: ")
    if millimeters.isdigit():
        millimeters = int(millimeters)
        meters = millimeters / 1000
        print(f"{millimeters} Millimeters is equal to {meters} Meters")
    else:
        print("Please enter a valid number!!!")
    return


def millimeters_to_centimeters():
    millimeters = input("Enter the value in Millimeters: ")
    if millimeters.isdigit():
        millimeters = int(millimeters)
        centimeters = millimeters / 10
        print(f"{millimeters} Millimeters is equal to {centimeters} Centimeters")
    else:
        print("Please enter a valid number!!!")
    return


def millimeters_to_kilometers():
    millimeters = input("Enter the value in Millimeters: ")
    if millimeters.isdigit():
        millimeters = int(millimeters)
        kilometers = millimeters / 1000000
        print(f"{millimeters} Millimeters is equal to {kilometers} Kilometers")
    else:
        print("Please enter a valid number!!!")
    return

"""
=================================================================================
"""



"""
======================================================================================
This is the complete Area converter. The area_converter function takes
the user choice and directs the operations to the specific function.
=======================================================================================
"""

def area_converter():
    while True:
        print("""Welcome to Area Converter. What conversion do you want to do? 
        1. Square Kilometers to Square Meters
        2. Square Meters to Square Kilometers
        3. Hectares to Square Meters
        4. Square Meters to Hectares
        5. Square Meters to Square Centimeters
        6. Square Centimeters to Square Meters
        7. Square Centimeters to Square Millimeters
        8. Square Millimeters to Square Centimeters
        """)
        type_of_area = input("Enter your selection (1 - 6): ")
        print("\n")

        if type_of_area.isdigit():
            type_of_area = int(type_of_area)

            if 1 <= type_of_area <= 6:
                if type_of_area == 1:
                    squarekilometers_to_squaremeters()
                elif type_of_area == 2:
                    squaremeters_to_squarekilometers()
                elif type_of_area == 3:
                    hectares_to_squaremeters()
                elif type_of_area == 4:
                    squaremeters_to_hectares()
                elif type_of_area == 5:
                    squaremeters_to_squarecentimeters()
                elif type_of_area == 6:
                    squarecentimeters_to_squaremeters()
                elif type_of_area == 7:
                    squarecentimeters_to_squaremillimeters()
                else:
                    squaremillimeters_to_squarecentimeters()

                break
            else:
                print("Please enter a number between 1 and 6")
        else:
            print("Please enter a valid number: ")
    return

def squarekilometers_to_squaremeters():
    squarekilometers = input("Enter the value in Square Kilometers: ")
    if squarekilometers.isdigit():
        squarekilometers = float(squarekilometers)
        squaremeters = squarekilometers * 1000000
        print(f"{squarekilometers} Square Kilometers is equal to {squaremeters} Square Meters")
    else:
        print("Please enter a valid number!!!")
    return


def squaremeters_to_squarekilometers():
    squaremeters = input("Enter the value in Square Meters: ")
    if squaremeters.isdigit():
        squaremeters = float(squaremeters)
        squarekilometers = squaremeters / 1000000
        print(f"{squaremeters} Square Meters is equal to {squarekilometers} Square Kilometers")
    else:
        print("Please enter a valid number!!!")
    return


def hectares_to_squaremeters():
    hectares = input("Enter the value in Hectares: ")
    if hectares.isdigit():
        hectares = float(hectares)
        squaremeters = hectares * 10000
        print(f"{hectares} Hectares is equal to {squaremeters} Meters")
    else:
        print("Please enter a valid number!!!")
    return


def squaremeters_to_hectares():
    squaremeters = input("Enter the value in Square Meters: ")
    if squaremeters.isdigit():
        squaremeters = float(squaremeters)
        hectares = squaremeters / 10000
        print(f"{squaremeters} Square Meters is equal to {hectares} Hectares")
    else:
        print("Please enter a valid number!!!")
    return


def squaremeters_to_squarecentimeters():
    squaremeters = input("Enter the value in Square Meters: ")
    if squaremeters.isdigit():
        squaremeters = float(squaremeters)
        squarecentimeters = squaremeters * 10000
        print(f"{squaremeters} Square Meters is equal to {squarecentimeters} Square Centimeters")
    else:
        print("Please enter a valid number!!!")
    return


def squarecentimeters_to_squaremeters():
    squarecentimeters = input("Enter the value in Square Centimeters: ")
    if squarecentimeters.isdigit():
        squarecentimeters = float(squarecentimeters)
        squaremeters = squarecentimeters / 10000
        print(f"{squarecentimeters} Square Centimeters is equal to {squaremeters} Square Meters")
    else:
        print("Please enter a valid number!!!")
    return


def squarecentimeters_to_squaremillimeters():
    squarecentimeters = input("Enter the value in Square Centimeters: ")
    if squarecentimeters.isdigit():
        squarecentimeters = float(squarecentimeters)
        squaremillimeters = squarecentimeters * 100
        print(f"{squarecentimeters} Square Centimeters is equal to {squaremillimeters} Square Millimeters")
    else:
        print("Please enter a valid number!!!")
    return


def squaremillimeters_to_squarecentimeters():
    squaremillimeters = input("Enter the value in Square Millimeters: ")
    if squaremillimeters.isdigit():
        squaremillimeters = float(squaremillimeters)
        squarecentimeters = squaremillimeters / 100
        print(f"{squaremillimeters} Square Millimeters is equal to {squarecentimeters} Square Centimeters")
    else:
        print("Please enter a valid number!!!")
    return


"""
=================================================================================
"""



"""
======================================================================================
This is the complete Volume converter. The volume_converter function takes
the user choice and directs the operations to the specific function.
=======================================================================================
"""


def volume_converter():
    while True:
        print("""Welcome to Volume Converter. What conversion do you want to do? 
        1. Cubic Meters to Liters
        2. Liters to Cubic Meters
        3. Liters to Milliliters
        4. Milliliters to Liters
        5. Cubic Centimeters to Milliliters
        6. Milliliters to Cubic Centimeters
        7. Cubic Meters to Cubic Centimeters
        8. Cubic Centimeters to Cubic Meters
        """)
        type_of_volume = input("Enter your selection (1 - 6): ")
        print("\n")

        if type_of_volume.isdigit():
            type_of_volume = int(type_of_volume)

            if 1 <= type_of_volume <= 6:
                if type_of_volume == 1:
                    cubicmeters_to_liters()
                elif type_of_volume == 2:
                    liters_to_cubicmeters()
                elif type_of_volume == 3:
                    liters_to_milliliters()
                elif type_of_volume == 4:
                    milliliters_to_liters()
                elif type_of_volume == 5:
                    cubiccentimeters_to_milliliters()
                elif type_of_volume == 6:
                    milliliters_to_cubiccentimeters()
                elif type_of_volume == 7:
                    cubicmeters_to_cubiccentimeters()
                else:
                    cubiccentimeters_to_cubicmeters()

                break
            else:
                print("Please enter a number between 1 and 6")
        else:
            print("Please enter a valid number: ")
    return

def cubicmeters_to_liters():
    cubicmeters = input("Enter the value in Cubic Meters: ")
    if cubicmeters.isdigit():
        cubicmeters = float(cubicmeters)
        liters = cubicmeters * 1000
        print(f"{cubicmeters} Cubic Meters is equal to {liters} Liters")
    else:
        print("Please enter a valid number!!!")
    return


def liters_to_cubicmeters():
    liters = input("Enter the value in Liters: ")
    if liters.isdigit():
        liters = float(liters)
        cubicmeters = liters / 1000
        print(f"{liters} Liters is equal to {cubicmeters} Cubic Meters")
    else:
        print("Please enter a valid number!!!")
    return


def liters_to_milliliters():
    liters = input("Enter the value in Liters: ")
    if liters.isdigit():
        liters = float(liters)
        milliliters = liters * 1000
        print(f"{liters} Liters is equal to {milliliters} Milliliters")
    else:
        print("Please enter a valid number!!!")
    return


def milliliters_to_liters():
    milliliters = input("Enter the value in Milliliters: ")
    if milliliters.isdigit():
        milliliters = float(milliliters)
        liters = milliliters / 1000
        print(f"{milliliters} Milliliters is equal to {liters} Liters")
    else:
        print("Please enter a valid number!!!")
    return


def cubiccentimeters_to_milliliters():
    cubiccentimeters = input("Enter the value in Cubic Centimeters: ")
    if cubiccentimeters.isdigit():
        cubiccentimeters = float(cubiccentimeters)
        milliliters = cubiccentimeters
        print(f"{cubiccentimeters} Cubic Centimeters is equal to {milliliters} Milliliters")
    else:
        print("Please enter a valid number!!!")
    return


def milliliters_to_cubiccentimeters():
    milliliters = input("Enter the value in Milliliters: ")
    if milliliters.isdigit():
        milliliters = float(milliliters)
        cubiccentimeters = milliliters
        print(f"{milliliters} Milliliters is equal to {cubiccentimeters} Cubic Centimeters")
    else:
        print("Please enter a valid number!!!")
    return


def cubicmeters_to_cubiccentimeters():
    cubicmeters = input("Enter the value in Cubic Meters: ")
    if cubicmeters.isdigit():
        cubicmeters = float(cubicmeters)
        cubiccentimeters = cubicmeters * 1000000
        print(f"{cubicmeters} Cubic Meters is equal to {cubiccentimeters} Cubic Centimeters")
    else:
        print("Please enter a valid number!!!")
    return


def cubiccentimeters_to_cubicmeters():
    cubiccentimeters = input("Enter the value in Cubic Centimeters: ")
    if cubiccentimeters.isdigit():
        cubiccentimeters = float(cubiccentimeters)
        cubicmeters = cubiccentimeters / 1000000
        print(f"{cubiccentimeters} Cubic Centimeters is equal to {cubicmeters} Cubic Meters")
    else:
        print("Please enter a valid number!!!")
    return


"""
=================================================================================
"""



"""
======================================================================================
This is the complete Mass/Weight converter. The mass_weight_converter function takes
the user choice and directs the operations to the specific function.
=======================================================================================
"""

def mass_weight_converter():
    while True:
        print("""Welcome to Mass/Weight Converter. What conversion do you want to do? 
        1. Kilograms to Pounds
        2. Kilograms to Ounces
        3. Kilograms to Tonnes (Metric tonnes)
        4. Kilograms to Grams 
        5. Grams to Pounds
        6. Grams to Ounces
        7. Grams to Tonnes (Metric tonnes)
        8. Grams to Kilograms
        9. Pounds to Kilograms
        10. Pounds to Ounces
        11. Pounds to Tonnes (Metric tonnes)
        12. Pounds to Grams
        13. Tonnes (Metric tonnes) to Kilograms
        14. Tonnes (Metric tonnes) to Ounces
        15. Tonnes (Metric tonnes) to Grams
        16. Tonnes (Metric tonnes) to Pounds
        """)

        type_of_mass = input("Enter your selection (1 - 16): ")
        print("\n")

        if type_of_mass.isdigit():
            type_of_mass = int(type_of_mass)

            if 1 <= type_of_mass <= 16:
                if type_of_mass == 1:
                    kilograms_to_pounds()
                elif type_of_mass == 2:
                    kilograms_to_ounces()
                elif type_of_mass == 3:
                    kilograms_to_tonnes()
                elif type_of_mass == 4:
                    kilograms_to_grams()
                elif type_of_mass == 5:
                    grams_to_pounds()
                elif type_of_mass == 6:
                    grams_to_ounces()
                elif type_of_mass == 7:
                    grams_to_tonnes()
                elif type_of_mass == 8:
                    grams_to_kilograms()
                elif type_of_mass == 9:
                    pounds_to_kilograms()
                elif type_of_mass == 10:
                    pounds_to_ounces()
                elif type_of_mass == 11:
                    pounds_to_tonnes()
                elif type_of_mass == 12:
                    pounds_to_grams()
                elif type_of_mass == 13:
                    tonnes_to_kilograms()
                elif type_of_mass == 14:
                    tonnes_to_ounces()
                elif type_of_mass == 15:
                    tonnes_to_grams()
                else:
                    tonnes_to_pounds()

                break

            else:
                print("Please enter a number between 1 and 16")
        else:
            print("Please enter a valid number: ")

    return

def kilograms_to_pounds():
    kilogram = input("Enter the value in kilograms: ")
    if kilogram.isdigit():
        kilogram = float(kilogram)
        pounds = kilogram * 2.20462
        print(f"{kilogram} kilograms is equal to {pounds} Pounds")
    else:
        print("Please enter a valid number: ")
    return


def kilograms_to_ounces():
    kilogram = input("Enter the value in kilograms: ")
    if kilogram.isdigit():
        kilogram = float(kilogram)
        ounce = kilogram * 35.27396
        print(f"{kilogram} kilograms is equal to {ounce} Ounces")
    else:
        print("Please enter a valid number: ")
    return


def kilograms_to_tonnes():
    kilogram = input("Enter the value in kilograms: ")
    if kilogram.isdigit():
        kilogram = float(kilogram)
        tonnes = (kilogram * 2.20462) / 2204.62262
        print(f"{kilogram} kilograms is equal to {tonnes} Tonnes")
    else:
        print("Please enter a valid number: ")
    return


def kilograms_to_grams():
    kilogram = input("Enter the value in kilograms: ")
    if kilogram.isdigit():
        kilogram = float(kilogram)
        grams = (kilogram / 0.45359237) * 453.59237
        print(f"{kilogram} kilograms is equal to {grams} Grams")
    else:
        print("Please enter a valid number: ")
    return


def grams_to_pounds():
    gram = input("Enter the value in Grams: ")
    if gram.isdigit():
        gram = float(gram)
        pounds = gram * 0.00220462
        print(f"{gram} Grams is equal to {pounds} Pounds")
    else:
        print("Please enter a valid number: ")
    return


def grams_to_ounces():
    gram = input("Enter the value in Grams: ")
    if gram.isdigit():
        gram = float(gram)
        ounce = gram * 0.03527396
        print(f"{gram} Grams is equal to {ounce} Ounces")
    else:
        print("Please enter a valid number: ")
    return


def grams_to_tonnes():
    gram = input("Enter the value in Grams: ")
    if gram.isdigit():
        gram = float(gram)
        tonnes = (gram / 453.59237) * 0.00045359237
        print(f"{gram} Grams is equal to {tonnes} Tonnes")
    else:
        print("Please enter a valid number: ")
    return


def grams_to_kilograms():
    gram = input("Enter the value in Grams: ")
    if gram.isdigit():
        gram = float(gram)
        kilogram = (gram / 453.59237) * 0.45359237
        print(f"{gram} Grams is equal to {kilogram} Kilograms")
    else:
        print("Please enter a valid number: ")
    return


def pounds_to_kilograms():
    pounds = input("Enter the value in Pounds: ")
    if pounds.isdigit():
        pounds = float(pounds)
        kilograms = pounds * 0.45359237
        print(f"{pounds} Pounds is equal to {kilograms} Kilograms")
    else:
        print("Please enter a valid number: ")
    return


def pounds_to_ounces():
    pounds = input("Enter the value in Pounds: ")
    if pounds.isdigit():
        pounds = float(pounds)
        ounces = (pounds * 453.59237) / 28.349523125
        print(f"{pounds} Pounds is equal to {ounces} Ounces")
    else:
        print("Please enter a valid number: ")
    return


def pounds_to_tonnes():
    pounds = input("Enter the value in Pounds: ")
    if pounds.isdigit():
        pounds = float(pounds)
        tonnes = pounds * 0.00045359237
        print(f"{pounds} Pounds is equal to {tonnes} Tonnes")
    else:
        print("Please enter a valid number: ")
    return


def pounds_to_grams():
    pounds = input("Enter the value in Pounds: ")
    if pounds.isdigit():
        pounds = float(pounds)
        grams = pounds * 453.59237
        print(f"{pounds} Pounds is equal to {grams} Grams")
    else:
        print("Please enter a valid number: ")
    return


def tonnes_to_kilograms():
    tonnes = input("Enter the value in Tonnes: ")
    if tonnes.isdigit():
        tonnes = float(tonnes)
        kilograms = (tonnes * 2204.62262) / 2.20462
        print(f"{tonnes} Tonnes is equal to {kilograms} Kilograms")
    else:
        print("Please enter a valid number: ")
    return


def tonnes_to_ounces():
    tonnes = input("Enter the value in Tonnes: ")
    if tonnes.isdigit():
        tonnes = float(tonnes)
        ounces = (tonnes * 1000000) / 28.349523125
        print(f"{tonnes} Tonnes is equal to {ounces} Ounces")
    else:
        print("Please enter a valid number: ")
    return


def tonnes_to_grams():
    tonnes = input("Enter the value in Tonnes: ")
    if tonnes.isdigit():
        tonnes = float(tonnes)
        grams = (tonnes / 0.00045359237) * 453.59237
        print(f"{tonnes} Tonnes is equal to {grams} Grams")
    else:
        print("Please enter a valid number: ")
    return


def tonnes_to_pounds():
    tonnes = input("Enter the value in Tonnes: ")
    if tonnes.isdigit():
        tonnes = float(tonnes)
        pounds = tonnes * 2204.622623
        print(f"{tonnes} Tonnes is equal to {pounds} Pounds")
    else:
        print("Please enter a valid number: ")
    return

"""
=================================================================================
"""



"""
======================================================================================
This is the complete Time converter. The time_converter function takes
the user choice and directs the operations to the specific function.
=======================================================================================
"""

def time_converter():
    while True:
        print("""Welcome to Time Converter. What conversion do you want to do? 
        1. Seconds to Days
        2. Minutes to months
        3. Hours to Years
        4. Days to Seconds
        5. Months to Minutes
        6. Years to Hours
        """)
        type_of_time = input("Enter your selection (1 - 6): ")
        print("\n")

        if type_of_time.isdigit():
            type_of_time = int(type_of_time)

            if 1 <= type_of_time <= 6:
                if type_of_time == 1:
                    seconds_to_days()
                elif type_of_time == 2:
                    minutes_to_months()
                elif type_of_time == 3:
                    hours_to_years()
                elif type_of_time == 4:
                    days_to_seconds()
                elif type_of_time == 5:
                    months_to_minutes()
                else:
                    years_to_hours()

                break

            else:
                print("Please enter a number between 1 and 6")
        else:
            print("Please enter a valid number: ")
    return


# This is Seconds to Days converter function
def seconds_to_days():
    seconds = input("Enter the value in Seconds: ")
    if seconds.isdigit():
        seconds = float(seconds)
        days = (seconds / 3600) / 24
        print(f"{seconds} Seconds is equal to {days} Days")
    else:
        print("Please enter a valid number: ")
    return


# This is Minutes to Months converter function
def minutes_to_months():
    minutes = input("Enter the value in Minutes: ")
    if minutes.isdigit():
        minutes = float(minutes)
        months = minutes / 43200
        print(f"{minutes} Minutes is equal to {months} Months")
    else:
        print("Please enter a valid number: ")
    return


# This is Hours to Years converter function
def hours_to_years():
    hours = input("Enter the value in Hours: ")
    if hours.isdigit():
        hours = float(hours)
        years = hours / 8760
        print(f"{hours} Hours is equal to {years} Years")
    else:
        print("Please enter a valid number: ")
    return


# This is Days to Seconds converter function
def days_to_seconds():
    days = input("Enter the value in Days: ")
    if days.isdigit():
        days = float(days)
        seconds = days * 3600 * 24
        print(f"{days} Days is equal to {seconds} Seconds")
    else:
        print("Please enter a valid number: ")
    return


# This is Months to Minutes converter function
def months_to_minutes():
    months = input("Enter the value in Months: ")
    if months.isdigit():
        months = float(months)
        minutes = months * 43200
        print(f"{months} Months is equal to {minutes} Minutes")
    else:
        print("Please enter a valid number: ")
    return


# This is Years to Hours converter function
def years_to_hours():
    years = input("Enter the value in Years: ")
    if years.isdigit():
        years = float(years)
        hours = years * 8760
        print(f"{years} Years is equal to {hours} Hours")
    else:
        print("Please enter a valid number: ")
    return

"""
=================================================================================
"""


"""
======================================================================================
This is the complete temperature converter. The temperature_converter function takes
the user choice and directs the operations to the specific function.
=======================================================================================
"""

print()
def temperature_converter():
    while True:
        print("""Welcome to Temperature Converter. What do you want to do? 
        1. Celsius to Fahrenheit
        2. Celsius to Kelvin
        3. Fahrenheit to Celsius
        4. Fahrenheit to Kelvin
        5. Kelvin to Celsius
        6. Kelvin to Fahrenheit
        """)
        type_of_temperature = input("Enter your selection (1 - 6): ")
        print("\n")

        if type_of_temperature.isdigit():
            type_of_temperature = int(type_of_temperature)

            if 1 <= type_of_temperature <= 6:
                if type_of_temperature == 1:
                    celsius_to_fahrenheit()
                elif type_of_temperature == 2:
                    celsius_to_kelvin()
                elif type_of_temperature == 3:
                    fahrenheit_to_celsius()
                elif type_of_temperature == 4:
                    fahrenheit_to_kelvin()
                elif type_of_temperature == 5:
                    kelvin_to_celsius()
                else:
                    kelvin_to_fahrenheit()

                break

            else:
                print("Please enter a number between 1 and 6")
        else:
            print("Please enter a valid number: ")

    return

# This is Celsius to Fahrenheit converter function

def celsius_to_fahrenheit():
    celsius = input("Enter your Temperature in Celsius: ")
    if celsius.isdigit():
        celsius = int(celsius)
        fahrenheit = round(((celsius * 9 / 5) + 32), 2)
        print(f"{celsius} Celsius is {fahrenheit} Fahrenheit")
    else:
        print("Please enter a valid number: ")
    return


# This is Celsius to Kelvin converter function

def celsius_to_kelvin():
    celsius = input("Enter your Temperature in Celsius: ")
    if celsius.isdigit():
        celsius = int(celsius)
        kelvin = round((celsius + 273.15), 2)
        print(f"{celsius} Celsius is {kelvin} Kelvin")
    else:
        print("Please enter a valid number: ")
    return

# This is Fahrenheit to Celsius converter function

def fahrenheit_to_celsius():
    fahrenheit = input("Enter your Temperature in Fahrenheit: ")
    if fahrenheit.isdigit():
        fahrenheit = int(fahrenheit)
        celsius = round(((fahrenheit * 9 / 5) - 32), 2)
        print(f"{fahrenheit} Fahrenheit is {celsius} Celsius")
    else:
        print("Please enter a valid number: ")
    return

# This is Fahrenheit to Kelvin converter function

def fahrenheit_to_kelvin():
    fahrenheit = input("Enter your Temperature in Fahrenheit: ")
    if fahrenheit.isdigit():
        fahrenheit = int(fahrenheit)
        kelvin = round((((fahrenheit - 32) * 9 / 5) + 273.15), 2)
        print(f"{fahrenheit} Fahrenheit is {kelvin} Kelvin")
    else:
        print("Please enter a valid number: ")
    return


# This is Kelvin to Celsius converter function

def kelvin_to_celsius():
    kelvin = input("Enter your Temperature in Kelvin: ")
    if kelvin.isdigit():
        kelvin = int(kelvin)
        celsius = round((kelvin - 273.15), 2)
        print(f"{kelvin} Kelvin is {celsius} Celsius")
    else:
        print("Please enter a valid number: ")
    return


# This is Kelvin to Fahrenheit converter function

def kelvin_to_fahrenheit():
    kelvin = input("Enter your Temperature in Kelvin: ")
    if kelvin.isdigit():
        kelvin = int(kelvin)
        fahrenheit = round((((kelvin - 273.15) * 9 / 5) + 32), 2)
        print(f"{kelvin} Kelvin is {fahrenheit} Fahrenheit")
    else:
        print("Please enter a valid number: ")
    return

"""
=============================================================================
"""



# This is the main function that calls the values function
def main():
    get_conversion()

    while True:
        print()
        condition = input("Do you want to perform another conversion? (Y/N): ")
        print()
        if condition.upper() == "Y":
            get_conversion()
        else:
            print("""
===========================================
Thank you for using Jamal's Unit Converter
===========================================
            """)
            break

    return

main()
