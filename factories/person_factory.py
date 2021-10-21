class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "%d: %s"%(self.id, self.name)

class PersonFactory:
    def __init__(self):
        self.person_id = 0

    def create_person(self, name):
        p = Person(self.person_id, name)
        self.person_id += 1
        return p

def main():
    pf = PersonFactory()
    people = [ pf.create_person(name) for name in ["alfa", "bravo", "charlie"] ]
    for p in people:
        print(p)

if __name__ == '__main__':
    main()