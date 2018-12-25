def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode('utf8-8')
    else:
        return bytes_or_str


# for python2
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        return unicode_or_str.decode('utf-8')
    else:
        return unicode_or_str


# for python2
def to_str2(unicode_or_str):
    if isinstance(unicode_or_str, unicode='utf-8'):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default

    return found
