# on suppose que le fichier existe
def read_set(filename):
    """
    crée un ensemble des mots-lignes trouvés dans le fichier
    """
    # on crée un ensemble vide
    result = set()

    # on parcourt le fichier
    with open(filename) as feed:
        for line in feed:
            # avec strip() on enlève la fin de ligne,
            # et les espaces au début et à la fin
            result.add(line.strip())
    return result

# on peut aussi utiliser une compréhension d'ensemble
def read_set_bis(filename):
    with open(filename) as feed:
        return {line.strip() for line in feed}



# ici aussi on suppose que les fichiers existent
def search_in_set(filename_reference, filename):
    """
    cherche les mots-lignes de filename parmi ceux
    qui sont presents dans filename_reference
    """

    # on tire profit de la fonction précédente
    reference_set = read_set(filename_reference)

    # on crée une liste vide
    result = []
    with open(filename) as feed:
        for line in feed:
            token = line.strip()
            # remarquez ici les doubles parenthèses
            # pour passer le tuple en argument
            result.append((token, token in reference_set))

    return result



def search_in_set_bis(filename_reference, filename):

    # on tire profit de la fonction précédente
    reference_set = read_set(filename_reference)

    # c'est un plus clair avec une compréhension
    # mais moins efficace car on calcule strip() deux fois
    with open(filename) as feed:
        return [(line.strip(), line.strip() in reference_set)
                for line in feed]
