from collections import namedtuple

# Create a class Vector3D
# Fields x and y are required. z has a default value of 0
Vector3D = namedtuple(typename="Vector3D", field_names=["x", "y", "z"], defaults=(0,))

if __name__ == "__main__":
    v = Vector3D(1, 1)
    v.x  # value of x
    v[1]  # value of y
    [x for x in v]  # namedtuples are iterables
