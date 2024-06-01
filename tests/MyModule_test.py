from MyPackage.MyModule import SquareFcn
import pytest

@pytest.mark.parametrize("Input", [int(-5), -3.4, 0, 0.2, 3, 4.4])
def test_Square_positives(Input):
    assert SquareFcn(Input) == Input*Input
    assert SquareFcn(Input) == Input**2

@pytest.mark.skip(reason="Input checking not yet implementet!")
@pytest.mark.parametrize("Input", [True, "hello", [3,2]])
def test_Square_negatives(Input):
    with pytest.raises(ValueError):
        SquareFcn(Input)

# def test_Square_OnArray