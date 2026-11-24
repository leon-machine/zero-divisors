import numpy as np
class Elim:
    def __init__(self, ncol, P):
        self.B = np.zeros((0, ncol)); self.piv = []; self.ncol = ncol; self.P = P
    def add(self, M):
        P = self.P
        M = np.mod(M, P).astype(np.float64)
        if self.piv:
            M = np.mod(M - np.mod(M[:, self.piv] @ self.B, P), P)
        new = []; newpiv = []
        for row in M:
            row = row.copy()
            for q, r in zip(newpiv, new):
                if row[q] != 0:
                    row = np.mod(row - row[q] * r, P)
            nzs = np.nonzero(row)[0]
            if len(nzs) == 0:
                continue
            q = int(nzs[0]); inv = pow(int(row[q]), P - 2, P)
            row = np.mod(row * inv, P)
            for k in range(len(new)):
                if new[k][q] != 0:
                    new[k] = np.mod(new[k] - new[k][q] * row, P)
            new.append(row); newpiv.append(q)
        if not new:
            return 0
        Mn = np.array(new)
        if self.piv:
            self.B = np.mod(self.B - np.mod(self.B[:, newpiv] @ Mn, P), P)
        self.B = np.vstack([self.B, Mn]); self.piv += newpiv
        return len(new)
    def rank(self):
        return len(self.piv)

