def xor_two_str(str1, str2):
    a_list = [chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2)]
    return a_list


def generateUuid(uuid):
    uuidKey = "4125442A472D4B6150645367566B5970"
    uuid = "".join(xor_two_str(uuid, uuidKey))
    return uuid
