class Date(object):
    def get_date(self):
        return "2018-12-09"

class Time(Date):
    def get_time(self):
        return '23:21:00'


dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_time())
print(tm.get_date())

