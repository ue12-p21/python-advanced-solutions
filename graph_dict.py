from collections import defaultdict

def graph_dict(filename):
    """
    construit une stucture de données de graphe
    à partir du nom du fichier d'entrée
    """
    # un dictionnaire vide normal
    graph = {}

    with open(filename) as feed:
        for line in feed:
            begin, value, end = line.split()
            # c'est cette partie qu'on économisera
            # dans la deuxième solution avec un defaultdict
            if begin not in graph:
                graph[begin] = []
            # remarquez les doubles parenthèses
            # car on appelle append avec un seul argument
            # qui est un tuple
            graph[begin].append((end, int(value)))
            # si on n'avait écrit qu'un seul niveau de parenthèses
            # graph[begin].append(end, int(value))
            # cela aurait signifié un appel à append avec deux arguments
            # ce qui n'aurait pas du tout fait ce qu'on veut
    return graph


def graph_dict_bis(filename):
    """
    pareil mais en utilisant un defaultdict
    """
    # on déclare le defaultdict de type list
    # de cette façon si une clé manque elle
    # sera initialisée avec un appel à list()
    graph = defaultdict(list)

    with open(filename) as feed:
        for line in feed:
            # on coupe la ligne en trois parties
            begin, value, end = line.split()
            # comme c'est un defaultdict on n'a
            # pas besoin de l'initialiser
            graph[begin].append((end, int(value)))
    return graph
