import unittest
import pymock
import FizzBuzz
import TestFizzBuzzStubbed
"""
Q5. Write the psuedocode for the test_repport method, such that it uses PyMock
    mock objects to test the report method of FizzBuzz. [5 pts]
"""
class TestFizzBuzzMocked(pymock.PyMockTestCase):
        
    def setUp(self):
        super(TestFizzBuzzMocked, self).setUp()
        self.fb = FizzBuzz.FizzBuzz()
        print "setUp TestFizzBuzzMocked"

    def tearDown(self):
        super(TestFizzBuzzMocked, self).tearDown()
        self.fb = None

        def test_report(self):
        #Create mock
        fileHandlerWrapperMock = self.mock()
        #Set expectations
        self.expectAndReturn()
        numbers = ['1','2','3','4']
        fileHandlerWrapperMock.write(numbers)
        fileHandlerWrapperMock.close()
        #Replay
        self.replay()
        #call api
        self.fb.record(numbers,fileHandlerWrapperMock)
        #verify
        self.verify()

if __name__ == "__main__":
    unittest.main()
