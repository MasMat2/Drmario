class Parent:
    events = 0
    def f(self):
        print(f'f {hex(id(self.events))}')
        # self.events += 11
    def b(self):
        print(f'b {hex(id(self.events))}')
        # self.events += 11

class Child(Parent):
    def __init__(self):
        print(f'i {hex(id(self.events))}')
        # self.events += 11
        self.f()
        self.b()

        print(f'i {hex(id(self.events))}')
        # self.events += 11
        self.f()
        self.b()
