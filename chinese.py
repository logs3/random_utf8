import random

def random_chinese(length):
    random_unicodes = [chr(random.randrange(0x4E00, 0x9FBF)) for _ in range(0, length)] 
    return u"".join(random_unicodes)
