import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    x=0
    if len(seqs) == 0:
        return np.empty((0, 0), dtype=int)
    if max_len is None:
        max_len = max((len(seq) for seq in seqs), default=0)
    padded=[]
    
    for seq in seqs:
        if len(seq) < max_len:
            seq = seq + [pad_value] * (max_len - len(seq))
        else:
            seq = seq[:max_len]
        padded.append(seq)
    return np.array(padded, dtype=int)
            
        
  