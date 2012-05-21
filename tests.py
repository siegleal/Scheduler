import unittest
import Employee

class EmployeeTestCase(unittest.TestCase):
    
    e = None

    def setUp(self):
        self.e = Employee.Employee("Test","Name",18,set())
        
    def testFirstName(self):
        self.assertEqual(self.e.getFirstName(),"Test")
        
    def testLastName(self):
        self.assertEqual(self.e.getLastName(),"Name")
        
    def testFullName(self):
        self.assertEqual(self.e.getFullName(),"Test Name")

    def testFormattedName(self):
        self.assertEqual(self.e.getFormattedName(),"Name, Test")

    def testPermantentDaysOff(self):
        self.assertEqual(len(self.e.getPermDaysOff()),0,'Constructor failed')
        self.e.setPermanentDaysOff({'sun','mon'})
        self.assertEqual(self.e.getPermDaysOff(),{'sun','mon'})

    def testIs18(self):
        self.assertTrue(self.e.is18())
        self.e.setAge(17)
        self.assertFalse(self.e.is18())

    def testRequestedDays(self):
        day = Employee.myDateTime(1,1)
        self.e.addReqDay(set(day))
        self.assertEqual(self.e.getReqDays(),set(day))
        


if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
