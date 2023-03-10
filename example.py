import numpy as np
from ecn_robotics.math import ech_red
from ecn_robotics.display import print_matrix

m = np.array([[1, 3, 0, 5],
              [0, 0, 0, 0],
              [0, 0, 1, 7]
              ], dtype=float)

RE = ech_red(m)

print_matrix(RE,
             name="RE matrix",
             xaxis=["C1", "Anotheronemaybe", "mx3", "x4", "l1"],
             yaxis=[str(i) for i in range(1, 6)]
             )
