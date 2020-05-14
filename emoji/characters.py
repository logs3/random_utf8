import random

def random_characters(length):
    random_unicodes = [chr(random.randrange(0x24C2, 0x1F251)) for _ in range(0, length)]
    return u"".join(random_unicodes)