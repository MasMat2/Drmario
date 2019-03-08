import random

abc = 'abcdefghijklmnopqrstuvwxyz1234567890,./[]'
cor = ()


def get_3d():
    t = ()
    for i in range(3):
        t += int(random.random()*10)
    return t

def face_vertex():
    face_tuple = ()
    for face in range(3):
        face_vertex = []
        for index in range(3):
            face_vertex.append(tuple(random.randint(0,10)))
        face_tuple += tuple(face_vertex),
    return face_tuple

face = []
for i in range(3):
    face.append((face_vertex()),)

print(face)
