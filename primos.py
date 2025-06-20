def es_primo(n):
    """Devuelve True si n es primo, False en caso contrario."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#comentario para probar