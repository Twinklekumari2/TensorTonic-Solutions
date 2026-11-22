import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    x = np.array(a)
    y = np.array(b)
    ans = float(np.sum(x*y))

    a_norm = np.linalg.norm(x)
    b_norm = np.linalg.norm(y)

    if a_norm == 0 or b_norm == 0 :
        return 0.0

    return float(ans/(a_norm*b_norm))
    
    pass