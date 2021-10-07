
numbers_in_texts = {
    0:'',
    1:'bir ',
    2:'ikki ',
    3:'uch ',
    4:"to'rt ",
    5:'besh ',
    6:'olti ',
    7:'yetti ',
    8:'sakkiz ',
    9:"to'qqiz ",
    10:"o'n ",
    20:"yigirma ",
    30:"o'ttiz ",
    40:"qirq ",
    50:"ellik ",
    60:"otmish ",
    70:"yetmish ",
    80:"sakson ",
    90:"to'qson ",
}

num10 = {
    0:'',
    1:"o'n ",
    2:'yigirma ',
    3:"o'ttiz ",
    4:"qirq ",
    5:'ellik ',
    6:'otmish ',
    7:'yetmish ',
    8:'sakson ',
    9:"to'qson "
}


def num_to_text(number):
    full_text = ''
    length_of_str_num = len(number)
    if len(number)<=18:
        for num in number:
            if length_of_str_num == 1:
                full_text+=numbers_in_texts[int(num)] 
           
            # o'nli sonlar uchun
            if length_of_str_num == 2:
                if (int(number) % 10) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num)*10]
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                    
            # Yuzli sonlar uchun  
            if length_of_str_num == 3:
                if (int(number) % 100) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num)]
                    full_text+='yuz '
                    return full_text
                elif int(num) != 0:
                    full_text+=numbers_in_texts[int(num)]
                    full_text+='yuz '
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1
           
            # Mingli sonlar uchun  
            if length_of_str_num == 4:
                if (int(number) % 1000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num)]
                    full_text+='ming '
                    return full_text
                elif int(num) != 0:
                    full_text+=numbers_in_texts[int(num)]
                    full_text+='ming '
                    length_of_str_num-=1
                else:
                    full_text+='ming '
                    length_of_str_num-=1
           
            # 10 Mingli sonlar uchun  
            if length_of_str_num == 5:
                if (int(number) % 10000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='ming '
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1
           
            # 100 Mingli sonlar uchun  
            if length_of_str_num == 6:
                if (int(number) % 100000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num)]
                    full_text+='yuz ming'
                    return full_text
                elif int(num) != 0:
                    full_text+=numbers_in_texts[int(num)]
                    full_text+='yuz '
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1
           
            # 1 Milyonli sonlar uchun  
            if length_of_str_num == 7:
                if (int(number) % 1000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num)]
                    full_text+='milyon'
                    return full_text
                elif int(num) != 0:
                    full_text+=numbers_in_texts[int(num)]
                    full_text+='milyon '
                    length_of_str_num-=1
                else:
                    full_text+='million '
                    length_of_str_num-=1
           
            # 10 Milyonli sonlar uchun  
            if length_of_str_num == 8:
                if (int(number) % 10000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='milyon'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1
           
            # 100 Milyonli sonlar uchun  
            if length_of_str_num == 9:
                if (int(number) % 100000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='milyon'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1
           
            # 1 milyardli sonlar uchun
            if length_of_str_num == 10:
                if (int(number) % 1000000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='milyard'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    full_text+='milyard '
                    length_of_str_num-=1
           
            # 10 milyardli sonlar uchun
            if length_of_str_num == 11:
                if (int(number) % 10000000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='milyard'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1
           
            # 100 milyardli sonlar uchun
            if length_of_str_num == 12:
                if (int(number) % 100000000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='milyard'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1
           
            # 1 trilyonli sonlar uchun
            if length_of_str_num == 13:
                if (int(number) % 1000000000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='trilyon'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    full_text+='trilyon'
                    length_of_str_num-=1
           
            # 10 trilyonli sonlar uchun
            if length_of_str_num == 14:
                if (int(number) % 10000000000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='trilyon'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1
           
            # 100 trilyonli sonlar uchun
            if length_of_str_num == 15:
                if (int(number) % 100000000000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='trilyon'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1

            # 1 Kvadrillion sonlar uchun
            if length_of_str_num == 16:
                if (int(number) % 1000000000000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='kvadrillion'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1

            # 10 Kvadrillion sonlar uchun
            if length_of_str_num == 17:
                if (int(number) % 10000000000000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='kvadrillion'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1
            # 100 Kvadrillion sonlar uchun
            if length_of_str_num == 18:
                if (int(number) % 100000000000000000) == 0 and int(num) != 0:
                    full_text+=numbers_in_texts[int(num*10)]
                    full_text+='kvadrillion'
                    return full_text
                elif int(num) != 0:
                    full_text+=num10[int(num)]
                    length_of_str_num-=1
                else:
                    length_of_str_num-=1

        return full_text
    else:
        return "afsuski o'qiya olmayman" 
    

print('Enter the number:')
number = input()
print(num_to_text(number))
