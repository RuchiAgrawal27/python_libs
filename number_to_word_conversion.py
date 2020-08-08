def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def convert(num):
    units = (
        "", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ",
        "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens = ("", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety ")

    if num < 0:
        return "minus " + convert(-num)

    if num < 20:
        return units[num]

    if num < 100:
        return tens[num // 10] + units[int(num % 10)]

    if num < 1000:
        if num % 100 == 0:
            return units[num // 100] + "hundred " + convert(int(num % 100))
        else:
            return units[num // 100] + "hundred and " + convert(int(num % 100))

    if num < 100000:
        return convert(num // 1000) + "thousand " + convert(int(num % 1000))

    if num < 10000000:
        return convert(num // 100000) + "Lakh " + convert(int(num % 100000))

    if num > 10000000:
        return ""


def number_to_word(submitted_number):
    print ("conversion to word for given currency number Rs." + str(submitted_number) + " is")
    if is_number(submitted_number):
        numbers = str(submitted_number).split('.')
        result = convert(int(numbers[0]));
        if result != "":
            if len(numbers) > 1:
                result = "Rs. " + result + "" + str(int(numbers[1])) + "/100 only"
            else:
                result =  "Rs. " + result + "only"
        else:
            result = "number out of range"
    else:
        result = "string must be number"

    print(result+" \n\n")
    return result;

if __name__ == "__main__":
    submitted_number = raw_input("The conversion of given currency number in to word : ")
    number_to_word(submitted_number)


