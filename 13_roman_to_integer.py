# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_number={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        int_number=0
        previous_number=0
        for i in s:
            new_num=roman_number[i]
            if new_num > previous_number:
                new_num -= previous_number*2
            int_number+=new_num
            previous_number=new_num
        return int_number

        
