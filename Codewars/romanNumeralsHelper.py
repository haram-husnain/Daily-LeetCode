class RomanNumerals:

    pairs = [
        ("M", 1000), ("CM", 900), ("D", 500), 
        ("CD", 400), ("C", 100), ("XC", 90),
        ("L", 50), ("XL", 40), ("X", 10),
        ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]

    @staticmethod
    def to_roman(val : int) -> str:
        if isinstance(val, int) and 0 < val < 4000:
            result = ""
            while val > 0:
                for a, b in RomanNumerals.pairs:
                    if val >= b:
                        val -= b
                        result += str(a)
                        break
            return result
        else:
            raise ValueError("input integers between 1 and 3999")
        
    @staticmethod
    def from_roman(roman_num : str) -> int:
        if isinstance(roman_num, str):
            result = 0
            for a, b in RomanNumerals.pairs:
                while roman_num.startswith(a):
                    result += b
                    roman_num = roman_num[len(a):]         
            return result
        else:
            raise ValueError("input a string of roman numerals")

#left most digit first
#skip the zeros

#FOR FROM_ROMAN FUNCTION
#

#FOR TO_ROMAN FUNCTION
#make a conversion table or an array or dict for roman numerals and integers - DONE
#check if the input is between 1 and 4000 - DONE
#subtract the number from which the input is higher or equal to in the conv dict
#a for loop maybe? "for a, b in pairs"
#and then convert it to that roman numeral, so it becomes the leftmost
#and then repeat until the difference is 0
#then join them
