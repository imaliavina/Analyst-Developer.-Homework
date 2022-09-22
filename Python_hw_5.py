# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = '''оаоор ораор орв АБВ ваа вваАБВАБВ аАБВ аааАБВ ывв вав укк вта ппАБВлл
аааАБВ рпр дон кевев оодд рпрАБВ роопр гргп олол ропрп гнгн'''

text2 = list(filter(lambda x: 'абв' not in x.lower(), text.split()))
print(text2)

#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

#Сжатие


def compress(in_str):

    count = 0
    pr_ch = ''
    out_str = ''

    for ch in in_str:
        if ch == pr_ch:
            count += 1
        else:
            if pr_ch != '':
                out_str += str(count) + pr_ch
            count = 1
        pr_ch = ch

    else:
        out_str += str(count) + pr_ch

    print(out_str)


#Восстановление


def decompress(in_str):

    numbers = '0123456789'
    num = ''
    out_str = ''

    for ch in in_str:
        if ch in numbers:
            num += ch
        else:
            if num != '':
                out_str += int(num) * ch
                num = ''

    print(out_str)


compress('AAABCCDDDEEEEEFFF')
decompress('3A1B2C3D5E3F')

compress('AAABCCDDD111EEEEE0000FFF')
decompress('3A1B20C3D5E3F')

compress('AAABCCDDDEEEEEFFF')
decompress('3A10B2C3D15E3F')


























