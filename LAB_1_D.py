from LAB_1_E import count_information_in_file, get_res
import os

#===========================================================================================
name1_txt = '\"Бешеные Псы (разговор за несчастный долар)\"'
name2_txt = '\"Jimi Hendrix - Stone Free (Jojo reference)\"'
name3_txt = '\"Коротка історія Моровінда (Джанет Сіте)\"'

text_1 = 'text1.txt'
name_text_1_Enc = 'text1_enc'
name_text_1_Bz2 = 'text1.bz2'
name_text_1_Bz2_Enc = 'text1_bz2_enc'

text_2 = 'text2.txt'
name_text_2_Enc = 'text2_enc'
name_text_2_Bz2 = 'text2.bz2'
name_text_2_Bz2_Enc = 'text2_bz2_enc'

text_3 = 'text3.txt'
name_text_3_Enc = 'text3_enc'
name_text_3_Bz2 = 'text3.bz2'
name_text_3_Bz2_Enc = 'text3_bz2_enc'

#===========================================================================================
text_1_binary = open(text_1, 'rb')
text_2_binary = open(text_2, 'rb')
text_3_binary = open(text_3, 'rb')

#===========================================================================================

with open(name_text_1_Enc, 'w', encoding='utf-8') as file:
    file.write(base_64_encoding(text_1_binary.read()))

with open(name_text_2_Enc, 'w', encoding='utf-8') as file:
    file.write(base_64_encoding(text_2_binary.read()))

with open(name_text_3_Enc, 'w', encoding='utf-8') as file:
    file.write(base_64_encoding(text_3_binary.read()))

#===========================================================================================

with open(name_text_1_Bz2, 'rb') as source, open(name_text_1_Bz2_Enc, 'w', encoding='utf-8') as file:
    file.write(base_64_encoding(source.read()))

with open(name_text_2_Bz2, 'rb') as source, open(name_text_2_Bz2_Enc, 'w', encoding='utf-8') as file:
    file.write(base_64_encoding(source.read()))

with open(name_text_3_Bz2, 'rb') as source, open(name_text_3_Bz2_Enc, 'w', encoding='utf-8') as file:
    file.write(base_64_encoding(source.read()))

#===========================================================================================

text_1_text = open(text_1, encoding='utf-8')
text_2_text = open(text_2, encoding='utf-8')
text_3_text = open(text_3, encoding='utf-8')

text_1_Enc = open(name_text_1_Enc)
text_2_Enc = open(name_text_2_Enc)
text_3_Enc = open(name_text_3_Enc)

text_1_Bz2 = open(name_text_1_Bz2_Enc)
text_2_Bz2 = open(name_text_2_Bz2_Enc)
text_3_Bz2 = open(name_text_3_Bz2_Enc)


#==========================================================================================

info_text_1_binary_size = os.path.getsize(text_1)

info_text_1_Enc = count_information_in_file(text_1_Enc, name1_txt + 'text1_encoded')
info_text_1_Enc_size = os.path.getsize(name_text_1_Enc)

info_text_1_Bz2 = count_information_in_file(text_1_Bz2, name1_txt + 'text1_in_bz2_encoded')
info_text_1_Bz2_size = os.path.getsize(name_text_1_Bz2_Enc)

print(name1_txt + ' orig_q: %f orig_s: %f enc_q: %f enc_s: %f bz2+enc_q: %f bz2+enc_s: %f' % (info_text_1_binary_size, info_text_1_Enc, info_text_1_Enc_size, info_text_1_Bz2, info_text_1_Bz2_size))
#===============================================================================================================================================================================================================

info_text_2_binary_s = os.path.getsize(text_2)

info_text_2_Enc = count_information_in_file(text_2_Enc, name2_txt + 'encoded')
info_text_2_Enc_s = os.path.getsize(name_text_2_Enc)

info_text_2_Bz2 = count_information_in_file(text_2_Bz2, name2_txt + ' bz2 encoded')
info_text_2_Bz2_s = os.path.getsize(name_text_2_Bz2_Enc)

print(name2_txt + ' orig_q: %f orig_s: %f enc_q: %f enc_s: %f bz2+enc_q: %f bz2+enc_s: %f' % (info_text_2_binary_s, info_text_2_Enc, info_text_2_Enc_s, info_text_2_Bz2, info_text_2_Bz2_s))
#===============================================================================================================================================================================================================

info_text_3_binary_s = os.path.getsize(text_3)

info_text_3_Enc = count_information_in_file(text_3_Enc, name3_txt + ' encoded')
info_text_3_Enc_s = os.path.getsize(name_text_3_Enc)

info_text_3_Bz2 = count_information_in_file(text_3_Bz2, name3_txt + ' bz2 encoded')
info_text_3_Bz2_s = os.path.getsize(name_text_3_Bz2_Enc)

print(name3_txt + ' orig_q: %f orig_s: %f enc_q: %f enc_s: %f bz2+enc_q: %f bz2+enc_s: %f' % (info_text_3_binary_s, info_text_3_Enc, info_text_3_Enc_s, info_text_3_Bz2, info_text_3_Bz2_s))
#===============================================================================================================================================================================================================


def base_64_encoding(data):
    text_binary_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
    
    bit_str = ''
    base64_str = ''
    div24_symb = ''
    
    for byte in data:
        bin_byte = bin(byte).lstrip("0b")
        bin_byte = bin_byte.zfill(8)
        bit_str += bin_byte
    
    while len(bit_str) % 24 != 0:
        div24_symb = '='
        bit_str += '0'

    groups = [bit_str[x:x+6] for x in range(0,len(bit_str),6)]
    
    for group in groups:
        base64_str += text_binary_alphabet[int(group, 2)]

    base64_str += div24_symb

    return base64_str