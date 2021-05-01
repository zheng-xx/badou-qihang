import numpy as np
a = np.random.randint(1,10,(1,3))
b = np.random.randint(1,10,(1,3))
A = np.linalg.norm(a)
B = np.linalg.norm(b)
cos_similar = np.sum(a*b)/(A*B)
print(cos_similar)