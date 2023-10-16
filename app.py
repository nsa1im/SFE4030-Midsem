def changeFromRoman(user_input):
    roman_numerals = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
    single_roman_numerals ={"V" : 5,"L" : 50,"D" : 500}
    int_value = 0

    if(user_input==None): #checks if None has been inputted
        return "invalid"
    
    user_input = user_input.upper()

    for i in range(len(user_input)):
        if user_input[i] not in roman_numerals: #checks if any letter is not in the roman numbers
            return "invalid"
        if user_input[i:i+4]==(user_input[i]+user_input[i]+user_input[i]+user_input[i]): #checks if the roman numbers has more than 3 repeating letters
            return "invalid"
        if len(user_input)>=i+2 and user_input[i] in single_roman_numerals and user_input[i+1] in single_roman_numerals: #checks if there is more than 1 repeating letter for single romans
            return "invalid"
        else:
            i += 1
    for i in range(len(user_input)):
        if user_input[i] in roman_numerals: #generates the integer value from the correct roman numbers
            if i + 1 < len(user_input) and roman_numerals[user_input[i]] < roman_numerals[user_input[i + 1]]:
                int_value -= roman_numerals[user_input[i]]
            else:
                int_value += roman_numerals[user_input[i]]
        else:
            return "invalid"

    return int_value #returns the integer value