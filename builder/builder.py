class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.elements = []

    def add_field(self, type, name):
        self.elements.append(
            (type, name)
        )
        return self

    def __str__(self):
        str = ["class %s:"%self.root_name]
        if self.elements:
            str.append("def __init__(self):")
            str.extend("    self.%s = %s"%(el[0],el[1]) for el in self.elements)
        else:
            str.append("  pass")
        return '\n'.join(str)

def main():
    cb = CodeBuilder('Person')\
        .add_field('name',  '""') \
        .add_field('age',  '0')
    print(cb)

if __name__ == '__main__':
    main()