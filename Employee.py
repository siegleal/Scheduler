class myDateTime:
    _month = 0
    _day = 0

    def __init__(self, month,day):
        self._month = month
        self._day = day

    def month(self):
        return self._month
    
    def day(self):
        return self._day

    def isAfter(self,other):
        if (isinstance(other,myDateTime)):
            if (other.month() > self._month):
                return true
            elif (other.month() < self._month):
                return false
            else:
                return (other.day() > self._day)

class Employee:
    
    _firstName = "first"
    _lastName = "last"
    _permanentDays = set()
    _age = 16
    _requestedDays = set()

    def __init__(self,fname,lname,age,pdays):
        self._firstName = fname
        self._lastName = lname
        self._age = age
        self._permanentDays = pdays
    
    def setFirstName(self,name):
        self._firstName = name
        
    def getFirstName(self):
        return self._firstName

    def setLastName(self,name):
        self._lastName = name
        
    def getLastName(self):
        return self._lastName
        
    def getFullName(self):
        return self._firstName + " " + self._lastName

    def getFormattedName(self):
        return self._lastName + ", " + self._firstName

    def setPermanentDaysOff(self,days):
        self._permanentDays = days
        
    def getPermDaysOff(self):
        return self._permanentDays

    def setAge(self,age):
        self._age = age

    def is18(self):
        return (self._age >= 18)

    def addReqDay(self,day):
        self._requestedDays |= day

    def getReqDays(self):
        return self._requestedDays

