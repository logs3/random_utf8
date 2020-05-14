import random

def random_emoticon(length):
    random_unicodes = [chr(random.randrange(0x1F601, 0x1F64F)) for _ in range(0, length)]
    return u"".join(random_unicodes)
