def int_to_char(n):
    """
    traduit un entier entre 1 et 26
    en un caractère entre 'A' et 'Z'
    """
    # si index était compris entre 0 et 25, on pourrait obtenir
    # la lettre comme étant chr(ord('A') + index)
    # on fait donc un changement de variable n -> n-1
    # de plus on va rendre le résultat cyclique modulo 26
    # pour pouvoir l'utiliser sur des nombres quelconques

    return chr(ord('A') + (n - 1) % 26)


def spreadsheet(index):
    """
    transforme un numéro de colonne en nom alphabétique
    dans l'ordre lexicographique
    1 -> A; 26 -> Z; 27 -> AA; 28 -> AB; etc..
    """
    # index peut être supérieur à 26
    # en remarquant que la dernière lettre s'incrémente à chaque fois
    # qu'index augmente, et repasse à 'A' de manière cyclique,
    # on voit qu'on peut utiliser notre version cyclique de `int_to_char`
    # pour calculer la lettre la plus à droite dans le résultat.
    # et pour les autres lettres, il suffit de recommencer sur le quotient

    result = int_to_char(index)
    while index > 26:
        index = (index - 1) // 26
        result = int_to_char(index) + result
    return result



def spreadsheet_bis(index):
    """
    Accessoirement on peut vérifier que la variable index fournie
    est bien un entier supérieur à 0.
    """
    if not isinstance(index, int):
        raise TypeError("index must be an integer !")
    elif index < 1:
        raise ValueError("index must be positive !")

    result = chr(ord('A') + (index - 1) % 26)
    while index > 26:
        index = (index - 1) // 26
        result = chr(ord('A') + (index - 1) % 26) + result
    return result
