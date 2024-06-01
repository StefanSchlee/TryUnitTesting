from MyPackage.MyModule import SquareFcn
import pytest

def test_Square():
    assert(SquareFcn(3) == 9)
    print("Test succeded!")