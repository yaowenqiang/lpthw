from time import gmtime, strftime
class LogFile():

    def __init__(self, logfile=''):
        self.logfile = logfile

    def write(self,message):
        timestr = strftime("%a, %d %b %Y %H:%M:%S",gmtime())
        message = timestr + ' ' + message + "\n"
        fh = open(self.logfile, 'a')
        fh.write(message)
        fh.close()
    

class DelimFile():

    def __init__(self, logfile='', delimitter=''):
        self.logfile = logfile
        self.delimitter = delimitter

    def write(self,message):
        timestr = strftime("%a, %d %b %Y %H:%M:%S",gmtime())
        writestr = ''

        for i in message[0:-1]:
            print(i)
            writestr += str(i) + self.delimitter

        writestr +=  str(message[-1])  + "\n"

        #writestr = timestr + ' ' + writestr + "\n"

        fh = open(self.logfile, 'a')
        fh.write(writestr)
        fh.close()

log1 = LogFile('log.txt')
log1.write('this is a log message')
log1.write('this is another log message')

c = DelimFile('test.csv', ',')
c.write(['a','b','c','d'])
c.write([1,2,3,4])
