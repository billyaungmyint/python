# any pytest file should start with test_
# pytest method names should start with test
# any code should be wrapped in method only
# fixtures are used as a setup and tear down methods for test cases - conftest file to generalise fixture
# and make it available to all test cases
# -k stands for method name execution - 
# -s logs in output
# -v stands for info metadata or verbose
# -m stands for mark - @pytest.mark.<name-to-mark>
# commandline options
# py.test -v -s 
# py.test test_demo2.py -v -s - file name
# py.test -k CreditCard -v -s - CreditCard is part of the name of the method
# py.test -m <name-to-mark> -v -s - name of the mark


import pytest



@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

def test_SecondGreetCreditCard():
    print("Good Morning")
