import random

def random_japanese(length):
    random_unicodes = [chr(random.randrange(0x3041, 0x30ff)) for _ in range(0, length)]
    return u"".join(random_unicodes)