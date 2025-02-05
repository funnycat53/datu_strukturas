
class Node:
    def __init__(self, saturs, vecaks=None, mazais=None, lielais=None, limenis = 0):
        self.info = saturs
        self.parent = vecaks
        self.smaller = mazais
        self.bigger = lielais
        self.level = limenis
        return
    
    def read(self):
        print(f"dati: {self.info}, līmenis: {self.level}")
        return
    
class Koks:
    def __init__(self):
        self.sakne = None
        return
    
    def add(self, jaunais):
        if self.sakne is None:
            self.sakne = Node(jaunais, limenis=0)
        else:
            self.add_rekursija(self.sakne, jaunais, level=1)

    def add_rekursija(self, tagadejais: Node, jaunais, level):
        if jaunais > tagadejais.info:
            if tagadejais.bigger is None:
                tagadejais.bigger = Node(jaunais, vecaks=tagadejais, limenis=level)
            else:
                self.add_rekursija(tagadejais.bigger, jaunais, level + 1)
        else:
            if tagadejais.smaller is None:
                tagadejais.smaller = Node(jaunais, vecaks=tagadejais, limenis=level)
            else:
                self.add_rekursija(tagadejais.smaller, jaunais, level + 1)
    
    def read(self):
        if self.sakne == None:
            print("Kokā nav neviena elementa!")
            return
        elements = self.sakne
        self.read_ja_ir(elements)

    def read_ja_ir(self, elements):
        if elements == None:
            return
        elements.read()
        self.read_ja_ir(elements.smaller)
        self.read_ja_ir(elements.bigger)
        return
    
    def sort(self):
        saraksts = []
        self.seciba(self.sakne, saraksts)
        print("Saraksts ar visiem elementiem:", saraksts)
        return saraksts

    def seciba(self, node: Node, saraksts):
        if node is None:
            return
        self.seciba(node.smaller, saraksts)
        saraksts.append(node.info)
        self.seciba(node.bigger, saraksts)
    def read_mazakais(self, mazakais):
        if mazakais.smaller:
            self.read_mazakais(mazakais.smaller)
        mazakais.read()
        if mazakais.bigger:
            self.read_mazakais(mazakais.bigger)

    def search(self, meklejamais):
        limenis, vecaks, skaits = self.parbauda_vienu(meklejamais, self.sakne, skaits=0)
        if limenis == -1:
            print(f"Neeksistē elements, tika veiktas {skaits} pārbaudes")
            return
        if limenis == 0:
            print(f"Elements ir koka sakne, tika veiktas {skaits} pārbaudes")
            return
        print(f"Elementa līmenis ir {limenis}, tā vecāks ir {vecaks}, tika veiktas {skaits} pārbaudes")
        return
    
    def parbauda_vienu(self, meklejamais, elements:Node, skaits):
        skaits += 1
        if meklejamais == elements.info:
            vecaks = None
            if elements.parent:
                vecaks = elements.parent.info
            return elements.level, vecaks, skaits
        if elements.smaller and elements.info > meklejamais:
            return self.parbauda_vienu(meklejamais, elements.smaller, skaits)
        if elements.bigger and elements.info < meklejamais:
            return self.parbauda_vienu(meklejamais, elements.bigger, skaits)
        return -1, None, skaits


koks = Koks()
koks.add(8)
koks.add(4)
koks.add(60)
koks.add(12)
koks.add(7)
koks.add(33)
koks.add(2)
koks.add(128)
koks.sort()
koks.search(60)
