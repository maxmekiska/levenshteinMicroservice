from Levenshtein import distance, hamming, jaro, ratio


def compute_levenshtein_distance(kwargs):
    dist = distance(**kwargs)
    return dist


def compute_ratio(kwargs):
    rat = ratio(**kwargs)
    return rat


def compute_hamming(kwargs):
    ham = hamming(**kwargs)
    return ham


def compute_jaro(kwargs):
    jar = jaro(**kwargs)
    return jar
