import funcao_binomial

def test_binomial():
    assert funcao_binomial.binomial(5, 3) == 10
    
def test_binomial():
    assert funcao_binomial.binomial(10, 1) == 10
    
def test_binomial():
    assert funcao_binomial.binomial(6, 2) == 15
    
def test_binomial():
    assert funcao_binomial.binomial(5, 0) == 1