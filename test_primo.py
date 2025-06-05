from primos import es_primo

def test_es_primo():
    # Casos verdaderos
    assert es_primo(2) is True
    assert es_primo(3) is True
    assert es_primo(5) is True
    assert es_primo(7) is True
    assert es_primo(13) is True

    # Casos falsos
    assert es_primo(1) is False
    assert es_primo(4) is False
    assert es_primo(6) is False
    assert es_primo(9) is False
    assert es_primo(0) is False