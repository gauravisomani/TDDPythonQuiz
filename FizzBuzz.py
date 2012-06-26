"""
Q1. Why is the report method untestable ? [2 pts]
Ans:
- report() method is instantiating collaborators like write,close,etc.
- have external dependency.

Q2. How will you change the api of the report method to make it more testable ? [2 pts]
Ans:
    def report(self, numbers,fileHandler):

"""
class FizzBuzz(object):
    def report(self, numbers,fileHandler=open):

        report_file = fileHandler('c:/temp/fizzbuzz_report.txt', 'w')

        for number in numbers:
            msg = str(number) + " "
            fizzbuzz_found = False
            if number % 3 == 0:
                msg += "fizz "
                fizzbuzz_found = True
            if number % 5 == 0:
                msg += "buzz "
                fizzbuzz_found = True

            if fizzbuzz_found:
                report_file.write(msg + "\n")

        report_file.close()

if "__main__" == __name__:
    fb = FizzBuzz()
    fb.report(range(100))