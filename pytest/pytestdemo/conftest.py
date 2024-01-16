import pytest

# without scope = class , setup will run before and after every methods in the class
# with the scope , setup will only run once before the class , run the methods in the class then run whatever after yield
@pytest.fixture(scope="class")
# name can be any name
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul" , "Shetty","rahulshettyacademy.com"]