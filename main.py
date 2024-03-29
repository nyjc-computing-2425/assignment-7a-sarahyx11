def text_numeral(num):
    '''
    takes in integer num that is less than 100
    returns num in text form
    eg >>> text_numeral(15)
    'fifteen'
    '''
    NUM_WORD = {
                1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine",
                10: "ten",
                11: "eleven",
                12: "twelve",
                13: "thirteen",
                14: "fourteen",
                15: "fifteen",
                16: "sixteen",
                17: "seventeen",
                18: "eighteen",
                19: "nineteen",
                20: "twenty",
                30: "thirty",
                40: "forty",
                50: "fifty",
                60: "sixty",
                70: "seventy",
                80: "eighty",
                90: "ninety"
            }
    count_dict = {}
    key_list = list(NUM_WORD.keys())[::-1]
    for i in range(len(NUM_WORD)):
        value = key_list[i]
        if num > value and num >= 20:
                    num -= value
                    count_dict[NUM_WORD.get(value)] = 1
        elif num < 20 and num == value:
            num -= value
            count_dict[NUM_WORD.get(value)] = 1


    text_list = count_dict.keys()
    return(' '.join(text_list))