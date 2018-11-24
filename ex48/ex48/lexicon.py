directions = ['north','south','east','west','down','up','left','right','back']
verbs = ['go','stop','kill','eat']
stops = ['the','in','of','from','at','it']
nouns = ['door','bear','princess','cabinet']
numbers = []
def scan(words):
    #stuff = input('> ')
    words = words.split()
    print(words)
    results = []
    if len(words) > 0:
        for w in words:
            if directions.count(w):
                results.append(('direction',w))
            elif verbs.count(w):
                results.append(('verb',w))
            elif stops.count(w):
                results.append(('stop',w))
            elif nouns.count(w):
                results.append(('noun',w))
            else:
                r = convert_num(w)
                if r is None:
                    results.append(('error',w))
                else:
                    results.append(('number',r))
        

    return results


def convert_num(num):
    try:
        return int(num)
    except ValueError:
        return None

