import math
import os

#Подсчет количества символов
def count_symvol(string):
    list_for_symvol = {}
    for char in string:
        if char not in list_for_symvol.keys():
            list_for_symvol[char] = 1
        else:
            list_for_symvol[char] += 1
    
    return list_for_symvol

#Подсчет относительной вероятности
def probability(ch):
    list = {}
    all_symvol = sum(ch.values())
    for i in ch.keys():
        list[i] = ch[i] * 1. / all_symvol
    return list

#Подсчет Энтропии 
def count_entropy(freq):
    entropy = 0
    for char in freq:
        entropy -= freq[char] * math.log(freq[char], 2)

    return entropy

#Возращение результатов функций (     (-_-)....// так удобно    )
def get_res(string):
    chars = count_symvol(string) 
    freq = probability(chars)
    entropy = count_entropy(freq)

    return chars, freq, entropy


#Алгоритм для подсчета количество информации из файла()   
def count_information_in_file(file, print_text):
    
    string = file.read() 
    chars, freq, entropy = get_res(string)
    
    symvol_keys = [*chars]
    symvol_keys.sort()
    
    print('Chars probability in %s' % print_text)
    for symvol in symvol_keys:
        print('%s: %f' % (symvol, freq[symvol]))
    print('Entropy: %f' % entropy)

    quant = entropy * sum(chars.values()) / 8 

    print('Quantity of information: %f' % quant)
   
    return quant
#============================================================================================
#                                    Якобы необходимые данные(Метаданные)
#============================================================================================

text1_name = '\"Бешеные Псы (разговор за несчастный долар)\"'
text2_name = '\"Jimi Hendrix - Stone Free (Jojo reference)\"'
text3_name = '\"Коротка історія Моровінда (Джанет Сіте)\"'

text1_txt = 'text1.txt'
name_text1_without_extension = 'text1'
text1_bz2 = name_text1_without_extension + '.bz2'
text1_zip = name_text1_without_extension + '.zip'
text1_gz = name_text1_without_extension + '.gz'
text1_7z = name_text1_without_extension + '.7z'
text1_xz = name_text1_without_extension + '.xz'

text2_txt = 'text2.txt'
name_text2_without_extension = 'text2'

text2_BZ2 = name_text2_without_extension + '.bz2'
text2_ZIP = name_text2_without_extension + '.zip'
text2_GZ = name_text2_without_extension + '.gz'
text2_7z = name_text2_without_extension + '.7z'
text2_XZ = name_text2_without_extension + '.xz'

text3_txt = 'text3.txt'
name_text3_without_extension = 'text3'

text3_bz2 = name_text3_without_extension + '.bz2'
text3_zip = name_text3_without_extension + '.zip'
text3_gz = name_text3_without_extension + '.gz'
text3_7z = name_text3_without_extension + '.7z'
text3_xz = name_text3_without_extension + '.xz'

label_for_text_size = 'text_size = '
label_for_Bz2_size = 'bz2_size = '
label_for_Zip_size = 'zip_size = '
label_for_Gz_size = 'gz_size = '
label_for_7z_size = '7z_size = '
label_for_Xz_size = 'xz_size = '
label_for_qantity_size = 'quantity_of_information = '
#=================================================================================================================

text1_text_readed = open(text1_txt, encoding='utf-8')
quantity_information_from_text1 = count_information_in_file(text1_text_readed, text1_name)

text2_text_readed = open(text2_txt,  encoding='utf-8')
quantity_information_from_text2 = count_information_in_file(text2_text_readed, text2_name )

text3_text_readed = open(text3_txt,  encoding='utf-8')
quantity_information_from_text3 = count_information_in_file(text3_text_readed, text3_name )
#=================================================================================================================

file_sizes_for_text1 = list(map(os.path.getsize, [text1_txt, text1_bz2, text1_zip, text1_gz, text1_7z, text1_xz]))
file_sizes_for_text1.append(round(quantity_information_from_text1))
List_with_file_sizes_for_text1 = [label_for_text_size  + str(file_sizes_for_text1[0]), label_for_Bz2_size + str(file_sizes_for_text1[1]), label_for_Zip_size + str(file_sizes_for_text1[2]), label_for_Gz_size + str(file_sizes_for_text1[3]), label_for_7z_size + str(file_sizes_for_text1[4]), label_for_Xz_size + str(file_sizes_for_text1[5]), label_for_qantity_size + str(file_sizes_for_text1[6])]

print(text1_name, List_with_file_sizes_for_text1, sep="\n||\n||\n===>")
#=================================================================================================================

file_sizes_for_text2 = list(map(os.path.getsize, [text2_txt, text2_BZ2, text2_ZIP, text2_GZ, text2_7z, text2_XZ]))
file_sizes_for_text2.append(round(quantity_information_from_text2))
List_with_file_sizes_for_text2 = [label_for_text_size  + str(file_sizes_for_text2[0]), label_for_Bz2_size + str(file_sizes_for_text2[1]), label_for_Zip_size + str(file_sizes_for_text2[2]), label_for_Gz_size + str(file_sizes_for_text2[3]), label_for_7z_size + str(file_sizes_for_text2[4]), label_for_Xz_size + str(file_sizes_for_text2[5]), label_for_qantity_size + str(file_sizes_for_text2[6])]

print(text2_name, List_with_file_sizes_for_text2, sep="\n||\n||\n===>")
#=================================================================================================================

file_sizes_for_text3 = list(map(os.path.getsize, [text3_txt, text3_bz2, text3_zip, text3_gz, text3_7z, text3_xz]))
file_sizes_for_text3.append(round(quantity_information_from_text3))
List_with_file_sizes_for_text3 = [label_for_text_size +  str(file_sizes_for_text3[0]), label_for_Bz2_size + str(file_sizes_for_text3[1]), label_for_Zip_size + str(file_sizes_for_text3[2]), label_for_Gz_size + str(file_sizes_for_text3[3]), label_for_7z_size + str(file_sizes_for_text3[4]), label_for_Xz_size + str(file_sizes_for_text3[5]), label_for_qantity_size + str(file_sizes_for_text3[6])]

print(text3_name, List_with_file_sizes_for_text3, sep="\n||\n||\n===>")
#=================================================================================================================