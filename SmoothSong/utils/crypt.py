def xor_two_str(str1, str2):
    a_list = [chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2)]
    return a_list


def encrypt(password):
    firstKey = "?E(H+KbPeShVmYq3t6w9z$C&F)J@NcQfTjWnZr4u7x!A%D*G-KaPdSgUkXp2s5v8"
    secondKey = "mZq4t7w!z%C&F)J@NcRfUjXn2r5u8x/A?D(G-KaPdSgVkYp3s6v9y$B&E)H@MbQe"
    encPassFirst = "".join(xor_two_str(password, firstKey))
    encPassSecond = "".join(xor_two_str(encPassFirst, secondKey))

    return encPassSecond


def decrypt(encPass):
    firstKey = "?E(H+KbPeShVmYq3t6w9z$C&F)J@NcQfTjWnZr4u7x!A%D*G-KaPdSgUkXp2s5v8"
    secondKey = "mZq4t7w!z%C&F)J@NcRfUjXn2r5u8x/A?D(G-KaPdSgVkYp3s6v9y$B&E)H@MbQe"
    decPassSecond = "".join(xor_two_str(encPass, secondKey))
    decPassFirst = "".join(xor_two_str(decPassSecond, firstKey))
    return decPassFirst
