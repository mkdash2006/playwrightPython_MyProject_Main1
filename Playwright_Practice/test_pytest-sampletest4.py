
import pytest

@pytest.mark.preprod
@ pytest.mark.order(2)
#@pytest.mark.dependency(name="test_m2")
@pytest.mark.dependency(dependency=["test_m2"])
def test_m1():
    print("I am in m1")

@pytest.mark.preprod
@ pytest.mark.order(1)
def test_m2():
    print("I am in m2")
