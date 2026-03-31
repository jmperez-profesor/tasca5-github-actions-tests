from src.operacions import suma

def test_suma_negatius():
    assert suma(-2, -3) == -5
