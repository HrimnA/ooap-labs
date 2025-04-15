class GeoNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class GeoTreeDFSIterator:
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        current = self.stack.pop()
        self.stack.extend(reversed(current.children))
        return current

def main():
    country = GeoNode("Україна")

    oblast1 = GeoNode("Київська область")
    rayon1 = GeoNode("Броварський район")
    town1 = GeoNode("Бровари")
    street1 = GeoNode("вул. Київська")
    street2 = GeoNode("вул. Гетьманська")

    town1.add_child(street1)
    town1.add_child(street2)
    rayon1.add_child(town1)
    oblast1.add_child(rayon1)

    oblast2 = GeoNode("Львівська область")
    rayon2 = GeoNode("Дрогобицький район")
    town2 = GeoNode("Трускавець")
    street3 = GeoNode("вул. Шевченка")

    town2.add_child(street3)
    rayon2.add_child(town2)
    oblast2.add_child(rayon2)

    country.add_child(oblast1)
    country.add_child(oblast2)

    print("Обхід дерева в глибину:")
    iterator = GeoTreeDFSIterator(country)
    for node in iterator:
        print(node.name)

if __name__ == "__main__":
    main()
