
# class Figure():
#     def __init__(self, surface, figure):
#         # Cubes coordinates x, y, z
#         self.pos = figure.pos
#         # Tell the program how to link each coordinate, this list is created based on self.pos
#         self.join = figure.join
#         self.faces = figure.faces
#         self.colors = figure.colors
#
#     def rot_algor(self, x, y, angle):
#         cos = math.cos(angle)
#         sin = math.sin(angle)
#         axis_1 = (cos*x - sin*y)
#         axis_2 = (cos*y + sin*x)
#
#         return axis_1, axis_2
#
#     def get_xyz(self):
#         # Create a list with the x,y and z values of each vertice
#         points = []
#         anglex = 2*Physics.counterx*math.pi/self.speed
#         angley = 2*self.countery*math.pi/self.speed
#         anglez = 2*self.counterz*math.pi/self.speed
#
#         for i in self.pos:
#             x,y,z = i
#             x, z = self.rot_algor(x, z, angley)
#             y, z = self.rot_algor(y, z, anglex)
#             x, y = self.rot_algor(x, y, anglez)
#
#             x = cam[0] + 50*x
#             y = cam[1] + 50*y
#             z = cam[2] + 50*z
#
#             points.append((x, y, z))
#         return points
#
#     def get_xy(self, x, y, z):
#         planex = self.width + 400*(x)/(z+1000)
#         planey = self.height + 400*(y)/(z+1000)
#         return (planex, planey)
#
#     def get_2d(self, cord_3d):
#         points = []
#         for cord in cord_3d:
#             x, y = get_xy(cord[0], cord[1], cord[2])
#             points.append((x,y))
#         return points
#
#     def update(self):
#         self.cord_3d = self.get_xyz()
#         self.cord_2d = self.get_2d(self.cord_3d)
#
#     def draw_polygons(self):
#         depths = []
#         for face in self.faces:
#             depths.append([sum([self.cord_3d[point][cor]**2  for point in face for cor in range(3)])])
#         return depths
#
# class Animation():
#
#     def __init__(self, surface, *args):
#         self.surface = surface
#         self.figures = args
#
#     def update_all(self):
#         move_cam()
#         for figure in self.figures:
#             figure.update()
#
#     def draw_all(self):
#         face_color = []
#         depths = []
#         face_list = []
#         for figure in self.figures:
#             for i in range(len(figure.faces)):
#                 face_list.append([figure.cord_2d[point] for point in figure.faces[i]])
#                 face_color.append(figure.colors[i])
#                 depths.append([sum([figure.cord_3d[point][2]**3  for point in figure.faces[i]])])
#         ordered = depths[:]
#         ordered.sort()
#         ordered.reverse()
#         for i in ordered:
#             p = depths.index(i)
#             pygame.draw.polygon(self.surface, face_color[p], face_list[p])
#
