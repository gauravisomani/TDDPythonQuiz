import unittest
import pymock
import FizzBuzz
"""
Q3. What will be printed when we execute 'python FizzBuzzStubbed.py' ? [3 pts]
Ans:

setUpClass FizzBuzzStubbed
setup
test_report
teardown
setup
test_report
teardown
tearDownClass

"""


"""
Q4. Implement MyStub class so that you can send it as a fake object to the
    report method of FizzBuzz object from a test case. [3 pts]
Ans:

"""
class MyStub(object):
    def __init__(self):
        pass
        
    def write(self, number):
        self.numbers.append(number)
    
    def close(self):
        self.closed = True

    def gen_open_stub(my_stub):
        def open(fpath, mode):
            return my_stub
        return open

class TestFizzBuzzStubbed(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        print "setUpClass FizzBuzzStubbed"
        
    def setUp(self):
        super(TestFizzBuzzStubbed, self).setUp()
        self.fb = FizzBuzz.FizzBuzz()
        print "setup"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass"
        
    def tearDown(self):
        super(TestFizzBuzzStubbed, self).tearDown()
        self.fb = None
        print "teardown"

    def test_report(self):
        print "test_report"
        numbers = ['1','2','3','4']
        my_stub = MyStub()
        filehandler = my_stub.gen_open_stub(my_stub)
        self.fb.report(numbers,filehandler)
        
    def test_report_for_empty_list(self):
         print "test_report"
        numbers = []
        my_stub = MyStub()
        filehandler = my_stub.gen_open_stub(my_stub)
        self.fb.report(numbers,filehandler)
        

if __name__ == "__main__":
    unittest.main()
