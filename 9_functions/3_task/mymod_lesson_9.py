def count_lines(name):
    file = open(name)
    lines = len(file.readlines())
    file.close()
    return print('lines: ' + str(lines))


def count_chars(name):
    file = open(name)
    chars = len(file.read())
    file.close()
    return print('chars: ' + str(chars))


def test(name):
    count_lines(name)
    count_chars(name)
