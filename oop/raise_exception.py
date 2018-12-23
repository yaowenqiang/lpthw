def make_delim_line(list_to_join, delim):
    try:
        formatted_line = delim.join(list_to_join)
    except TypeError:
        raise TypeError("make_delim_line(): arg 1 must be a list or tuple")
    return formatted_line

fline1 = make_delim_line('abc', ',')
print(fline1)
#fline2 = make_delim_line([1, 2, 3], ',')
#print(fline2)


mydict = {'a':1,'b':2}
try:
    print(5/0)
#except ZeroDivisionError , e:
except Exception as e:
    #print(e.message)
    print(e.args)
    print(str(e))
