
import pytest
# General Approach using method ###################

# @pytest.mark.smoke1
# def test_f1():
#     print("Precondition")
#     print("Test step1")
#     print("Postcondition")
# @pytest.mark.smoke1
# def test_f2():
#     print("Precondition")
#     print("Test step2")
#     print("Postcondition")
# @pytest.mark.smoke1
# def test_f3():
#     print("Precondition")
#     print("Test step3")
#     print("Postcondition")

# Using Function() for repeatative functionality ##############################
# def precondition():
#     print("TC Precondition")

# def postcondition():
#     print("TC Postcondition")
    
# @pytest.mark.smoke1
# def test_f1():
#     precondition()
#     print("Test step1")
#     postcondition()
# @pytest.mark.smoke1
# def test_f2():
#     precondition()
#     print("Test step2")
#     postcondition()
# @pytest.mark.smoke1
# def test_f3():
#     precondition()
#     print("Test step3")
#     postcondition()

# Now Using playwright 'fixture' method for the repeatative functionality 
# Post conditions (if any) - use 'yield' once
# Here fixture defined and executed in all test cases
# @pytest.fixture()
# def precondition():
#     print("TC Precondition")
#     yield
#     print("TC Postcondition")
    
# @pytest.mark.smoke1
# def test_f1(precondition):
#     print("Test step1")
    
# @pytest.mark.smoke1
# def test_f2(precondition):
#     print("Test step2")
    
# @pytest.mark.smoke1
# def test_f3(precondition):
#     print("Test step3")

# Here fixture defined and executed in all test cases
# @pytest.fixture(autouse=True)     # Bydefault @pytest.fixture(autouse=True, scope="function")  
#                                   # So no need to define scope="functoion" with fixture
# def precondition():
#     print("TC Precondition")
#     yield
#     print("TC Postcondition")
    
@pytest.mark.smoke1
def test_f1():
    print("Test step1")
    
@pytest.mark.smoke1
def test_f2():
    print("Test step2")
    
@pytest.mark.smoke1
def test_f3():
    print("Test step3")

# Fixture defined but executed once not in all test cases. Before all TC/After All the TC.  Start/End of TC
# @pytest.fixture(autouse=True, scope="session")
# def precondition():
#     print("Precondition Before All Tests")
#     yield
#     print("Postcondition After All Tests")
# @pytest.mark.smoke1  
# def test_f1():
#     print("Test Case 1")
    
# @pytest.mark.smoke1  
# def test_f2():
#     print("Test Case 2")
    
# @pytest.mark.smoke1   
# def test_f3():
#     print("Test Case 3")

# Fixture - yield also return value in each test case
# @pytest.fixture(autouse=True, scope="session")
# def precondition():
#     print("Precondition Before All Tests")
#     yield
#     print("Postcondition After All Tests")

# @pytest.fixture(autouse=True)
# def prevalue1():
#     print("fixture value:")
#     yield ": data from fixture"

# @pytest.mark.smoke1  
# def test_f1(prevalue1):
#     print("Test Case1", prevalue1)

# @pytest.mark.smoke1  
# def test_f2(prevalue1):
#     print("Test Case2", prevalue1)
    
# @pytest.mark.smoke1   
# def test_f3(prevalue1):
#     print("Test Case3", prevalue1)
    
    