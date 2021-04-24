import numpy as np


def cos_sim(vector_a, vector_b):
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim
if __name__ == '__main__':
    vector_a = np.array([1,2,3])
    vector_b = np.array([1,2,3])
    vector_c = np.array([-1,-2,-3])
    print('cos_sim between vector_a and vector_b:',cos_sim(vector_a,vector_b))
    print('cos_sim between vector_b and vector_c:',cos_sim(vector_b,vector_c))