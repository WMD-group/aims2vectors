#! /usr/bin/env python

"""Get lattice vector in a, b, c, alpha, beta, gamma format from input geometry"""

import numpy as np
import sys

# Allow file to be given as input argument

if len(sys.argv) == 1:
    input_file='geometry.in'
else:
    input_file = sys.argv[1]

# Import data columns from FHI-aims input file
lattice_matrix = np.genfromtxt(input_file,comments='#',usecols=(1,2,3))
# Truncate to top 3 rows
lattice_matrix = lattice_matrix[0:3,:]

# Get lattice vector magnitudes (a, b, c) according to Pythagoras' theorem
(a, b, c) = np.sqrt(np.sum(np.square(lattice_matrix),1))

# Calculate angles between vectors using relation
# A.B = |A||B|cos(theta)
gamma = np.arccos(lattice_matrix[0,:].dot(lattice_matrix[1,:]) \
                    / (np.linalg.norm(lattice_matrix[0,:]) * \
                           np.linalg.norm(lattice_matrix[1,:]) \
                      )
                )

alpha = np.arccos(lattice_matrix[1,:].dot(lattice_matrix[2,:]) \
                    / (np.linalg.norm(lattice_matrix[1,:]) * \
                           np.linalg.norm(lattice_matrix[2,:]) \
                      )
                )

beta = np.arccos(lattice_matrix[2,:].dot(lattice_matrix[0,:]) \
                    / (np.linalg.norm(lattice_matrix[2,:]) * \
                           np.linalg.norm(lattice_matrix[0,:]) \
                      )
                )


# Convert to degrees
(alpha, beta, gamma) = np.array([alpha, beta, gamma]).dot(180/np.pi)

print '    a    b      c    alpha  beta   gamma'
print '{0:6.3f} {1:6.3f} {2:6.3f} {3:6.2f} {4:6.2f} {5:6.2f}'.format(\
          a,    b,    c,    alpha, beta, gamma)

