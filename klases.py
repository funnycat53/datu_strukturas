class Node:
    def __init__(self, saturs, pirms=None, pec=None):
        self.info = saturs
        self.next = pec
        self.prev = pirms

    def read(self):
        print(self.info)

class List:
    def __init__(self):
        self.sakums = None
        self.skaits = 0
        return

    def add(self, jaunais, index = -1):
        if index == -1 or index >= self.skaits:
            if self.sakums == None:
                self.sakums = Node(jaunais)
            else:
                pedejais = self.sakums
                while pedejais.next:
                    pedejais = pedejais.next
                pedejais.next = Node(jaunais, pirms = pedejais)
        else:
            if index == 0:
                elements = Node(jaunais, pec = self.sakums)
                self.sakums.next.prev = elements
                self.sakums = elements
            else:
                aste = self.sakums
                for i in range(index):
                    aste = aste.next   
                galva = aste.prev
                elements = Node(jaunais, galva, aste)
                galva.next = elements
                aste.prev = elements
        self.skaits += 1
        return

    def read(self):
        if self.sakums == None:
            print("Saraksts ir tukšs!")
        esosais = self.sakums
        while esosais:
            esosais.read()
            esosais = esosais.next
        return

    def pop(self):
        if self.skaits == 0:
            print("Nav ko izdzēst")
            return
        if self.skaits == 1:
            self.sakums = None
            self.skaits = 0
            return
        pirmspedejais = self.sakums
        while pirmspedejais.next.next:
            pirmspedejais = pirmspedejais.next
        pirmspedejais.next = None
        self.skaits -= 1
        return
    
saraksts = List()
saraksts.read()
saraksts.add("free", 1)
saraksts.add("huzz", 2)
saraksts.add("luh", 0)
saraksts.add("calm", 4)
saraksts.add("tēma", 3)
saraksts.add("bruzz", 6)
saraksts.add("tuzz", 5)
saraksts.add(1000000)
saraksts.pop()
saraksts.read()

