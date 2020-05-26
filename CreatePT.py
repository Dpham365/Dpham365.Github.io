def Conversion(value, user):
                if user == "kilometers":
                    output = value/0.621
                else:
                    output = value  * 0.621
                return output     
raw_input("This is a measurement converter. It is able to provide accurate conversions between units of measurement to the thousandths place.")
answer = raw_input ("Please specify a conversion method from one of the following: distance, weight, or volume. ")
if answer.lower() == "distance":
    user = raw_input("Please state unit to convert: kilometers or miles ")
    if user == "kilometers":
            def AskKilometers():
                value  = float(raw_input("Please input the distance in kilometers: "))
                return value 
            def KilometerstoMiles():
                UserKilometer = AskKilometers()
                ValueMile = Conversion(UserKilometer, user)
                print(str(UserKilometer) + " kilometer(s) converted to mile(s) is " + str(ValueMile) + " miles(s).")
            KilometerstoMiles()
    else:
            def AskMiles():
                mile = float(raw_input("Please input the distance in miles: "))
                return mile
            def KilometersConversion(mile):
                kilometer = mile/0.621
                return kilometer
            def MilestoKilometers():
                UserMile = AskMiles()
                ValueKilometer = KilometersConversion(UserMile)
                print(str(UserMile) + " miles(s) converted to kilometer(s) is " + str(ValueKilometer) + " miles(s).")
            MilestoKilometers()
elif answer.lower() == "weight":
    user = raw_input("Please state unit to convert: lb or kg ")
    if user == "lb":
            def AskPounds():
                pound = float(raw_input("Please input the weight in pounds: "))
                return pound
            def KilogramConversion(pound):
                kilogram = pound/2.20462
                return kilogram
            def PoundstoKilograms():
                UserPound = AskPounds()
                ValueKilogram = KilogramConversion(UserPound)
                print(str(UserKilogram) + " kilograms(s) converted to pound(s) is " + str(ValuePound) + " pound(s).")
            PoundstoKilograms()
    else:
            def AskKilograms():
                kilogram = float(raw_input("Please input the weight in kilograms: "))
                return kilogram
            def PoundConversion(kilogram):
                pound = kilogram * 2.20462
                return pound
            def KilogramstoPounds():
                UserKilogram = AskKilograms()
                ValuePound = PoundConversion(UserKilogram)
                print(str(UserKilogram) + " kilograms(s) converted to pound(s) is " + str(ValuePound) + " pound(s).")
            KilogramstoPounds()
elif answer.lower() == "volume.":
    user = raw_input("Please state unit to convert: cup or fl oz. ")
    if user == "cup":
            def AskCups():
                cup = float(raw_input("Please input the volume in cups: "))
                return cup
            def FlozConversion(cup):
                floz = cup * 8
                return floz
            def CupstoFloz():
                UserCup = AskCups()
                ValueFloz = FlozConversion(UserCup)
                print(str(UserCup) + " cup(s) converted to fluid ounce(s) is " + str(ValueFloz) + " fluid ounce(s).")
            CupstoFloz()
    else:
            def AskFloz():
                floz = float(raw_input("Please input the volume in fluid ounces: "))
                return floz
            def CupConversion(floz):
                cup = floz/8
                return cup
            def FloztoCups():
                UserFloz = AskFloz()
                ValueCup = CupConversion(UserFloz)
                print(str(UserFloz) + " fluid ounces(s) converted to cup(s) is " + str(ValueCup) + " cup(s).")
            FloztoCups()
else:
    print("Invalid selection. Please try again.")
