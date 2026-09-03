
import pytest
# General fumction approach
# def sum1():
#     a=2
#     b=3
#     assert a+b==5

# def sum2():
#     a=6
#     b=7
#     assert a+b==13

# pytest parametrize approach

@pytest.mark.smoke2
@pytest.mark.parametrize("a,b,c",[(2,3,5),(5,6,12),(2,5,7)])      # To pass value to test case
def test_sum(a,b,c):
    assert a+b == c



