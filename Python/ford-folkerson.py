"""
Ford Fulkerson used to solve the maximum flow problem in a flow graph.
The algorithm iteratively finds an augmenting path which is from source to sink in a residual graph.
The residual graph is one created by subtracting (capacity - current flow) for forward edges + adding backward edge of current flow
The algo then increases the flow along the augmenting path by maximum amount, which is the minimum capacity of edges along that path.
Runs in O(max flow * E)

"""

from collections import defaultdict