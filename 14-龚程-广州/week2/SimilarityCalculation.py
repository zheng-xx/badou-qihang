import numpy as np


def cosine(vec_1, vec_2):
    if vec_1.size != vec_2.size:
        raise Exception("The size of vec_1 and vec_2 need to be the same.")
    else:
        dot_product = float(np.sum(vec_1 * vec_2))
        norm_product = np.linalg.norm(vec_1) * np.linalg.norm(vec_2)
        cosine_similarity = dot_product / norm_product
        return cosine_similarity
