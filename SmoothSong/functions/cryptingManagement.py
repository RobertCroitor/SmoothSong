# STRING XOR
def xor_two_str(str1, str2):
    a_list = [chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2)]
    return a_list

    # CRYPTING FUNCTIONS
    # ENCRYPT PASSWORD


def encrypt(password):
    firstKey = "?E(H+KbPeShVmYq3t6w9z$C&F)J@NcQfTjWnZr4u7x!A%D*G-KaPdSgUkXp2s5v8"
    secondKey = "mZq4t7w!z%C&F)J@NcRfUjXn2r5u8x/A?D(G-KaPdSgVkYp3s6v9y$B&E)H@MbQe"
    encPassFirst = "".join(xor_two_str(password, firstKey))
    encPassSecond = "".join(xor_two_str(encPassFirst, secondKey))
    return encPassSecond

    # DECRYPT PASSWORD


def decrypt(encPass):
    firstKey = "?E(H+KbPeShVmYq3t6w9z$C&F)J@NcQfTjWnZr4u7x!A%D*G-KaPdSgUkXp2s5v8"
    secondKey = "mZq4t7w!z%C&F)J@NcRfUjXn2r5u8x/A?D(G-KaPdSgVkYp3s6v9y$B&E)H@MbQe"
    decPassSecond = "".join(xor_two_str(encPass, secondKey))
    decPassFirst = "".join(xor_two_str(decPassSecond, firstKey))
    return decPassFirst

    # GENERATE A UUID FOR THE USER BASED ON IT'S USERNAME


def generateUuid(username):
    uuidKey = "4125442A472D4B6150645367566B5970"
    uuid = "".join(xor_two_str(username, uuidKey))
    return uuid

# CRYPTING FUNCTIONS END
