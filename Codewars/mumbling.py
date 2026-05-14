def accum(st):
    
    a1 = []
    
    if st.isalpha():
        split_up = list(st.upper())
        
        for index, item in enumerate(split_up):
            item = (item + item.lower() * index)
            a1.append(item)
        
        return "-".join(a1)
        
    else: return None

accum("abcd")
# This time no story, no theory. The examples below show you how to write function accum:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"