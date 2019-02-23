class Piram:

    pos = [
    [3,3,3],
    [1,-2,2],
    [2,-2,3]
    ]
    # Tell the program how to link each coordinate, this list is created based on pos
    join = [
    [0,1], [1,2], [2,0]
    ]

    faces = {
    (0,1,2): (0, 255, 255),
    }
    faces = [
        (0,1,2)
    ]

    colors = [
        (0, 255, 255)
    ]

class Piram1:

    pos = [
    [-10,0,0],
    [-4,-3,4],
    [-4,4,3]
    ]
    # Tell the program how to link each coordinate, this list is created based on pos
    join = [
    [0,1], [1,2], [2,0]
    ]

    faces = {
    (0,1,2): (255, 0, 255),
    }

    faces = [
        (0,1,2)
    ]

    colors = [
        (0, 255, 255)
    ]

class Cube:

    # Cubes coordinates x, y, z
    pos = [
    [1,-1,1],
    [1,-1,-1],
    [-1,-1,-1],
    [-1,-1,1],
    [1,1,1],
    [1,1,-1],
    [-1,1,-1],
    [-1,1,1]
    ]
    # Tell the program how to link each coordinate, this list is created based on pos
    join = [
    [0,1], [1,2], [2,3], [3,0],
    [4,5], [5,6], [6,7], [7,4],
    [0,4], [1,5], [2,6], [3,7]
    ]

    faces = {
    (0,1,2,3): (0, 255, 255),
    (4,5,6,7): (255, 0, 255),
    (0,1,5,4): (255, 255, 0),
    (1,2,6,5): (0, 255, 0),
    (2,3,7,6): (0, 0, 255),
    (3,0,4,7): (255, 0, 0)
    }
    colors = [
        (0, 255, 255),
        (255, 0, 255),
        (255, 255, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 0, 0),
        (0, 255, 255),
        (255, 0, 255),
        (255, 255, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 0, 0)
    ]

    faces = [
    (0,1,2),
    (4,5,6),
    (0,1,5),
    (1,2,6),
    (2,3,7),
    (3,0,4),
    (0,2,3),
    (4,6,7),
    (0,5,4),
    (1,6,5),
    (2,7,6),
    (3,4,7)
    ]


if __name__ == "__main__":
    pass
