from main import es_par

def test_es_par():
    assert es_par(2) == True
    assert es_par(3) == False
    assert es_par(0)==True