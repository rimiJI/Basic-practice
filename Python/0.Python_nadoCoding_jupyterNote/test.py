# import numpy as np
# liar_data= [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
# print(liar_data)
# print(type(liar_data))
# # ---------------------------어레이로 전환
# liar_array=np.array(liar_data)
# print(liar_array)
# print(type(liar_array))
# #------------------------0인얘들만 모라라
# liar_num=liar_array[liar_array==0]
# print(liar_num)
# #--------------------size = 갯수
# print(liar_num.size)





# char: h new char: k
# char: e new char: h
# char: l new char: o
# char: l new char: o
# char: o new char: r
# char:   new char: c
# char: w new char: z
# char: o new char: r
# char: r new char: u
# char: l new char: o
# char: d new char: g

# print(np.array([[1,2,3],[4.5,'5','6']],dtype=np.string).nbytes)

text = 'Hello Zaira'
shift = 3

def caeser():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)
