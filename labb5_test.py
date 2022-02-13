from bintreeFile import Bintree
from LinkedQFile import LinkedQ

gamla = Bintree()       # Initierar träd för gamla ord
svenska = Bintree()     # Initierar träd för svenska ordlistan
q = LinkedQ()           # Initierar länkad lista

# Lägger in svenska ord i svenska trädet
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet


# funktion för att få ord från användaren
def ta_input(ordlista):
    orden = list()
    start = input("Ange startord: ")
    while start not in ordlista:        # Måste ange ord i svenska trädet
        start = input(start + " finns inte i ordlistan. Ange ett startord från ordlistan: ")
    orden.append(start)
    slut = input("Ange slutord: ")
    while slut not in ordlista:         # Måste ange ord i svenska trädet
        slut = input(slut + " finns inte i ordlistan. Ange ett slutord från ordlistan: ")
    orden.append(slut)
    return orden                        # returnerar lista med startord och slutord


class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent


def writechain(slutnod):
    if slutnod.parent == None:
        print(slutnod.word)
    else:
        writechain(slutnod.parent)
        print(slutnod.word)


def makechildren(startord, slutord, q):
    """Funktion för bredden-först-sökning. Kontrollerar om det finns en väg till slutord från givet startord"""
    gamla.put(startord.word)
    startord_lista = list(startord.word)
    bokstaver = "abcdefghijklmnopqrstuvwxyzåäö"
    for bokstav_position in range(len(startord_lista)):
        for bokstaven in bokstaver:
            startord_lista[bokstav_position] = bokstaven
            nytt_ord = "".join(startord_lista)
            if nytt_ord in svenska and nytt_ord not in gamla:
                ny_nod = ParentNode(nytt_ord)
                ny_nod.parent = startord
                if nytt_ord == slutord:
                    print("Finns denna väg till " + slutord + ": ", end="\n")
                    writechain(ny_nod)
                    return True
                else:
                    gamla.put(nytt_ord)
                    q.enqueue(ny_nod)
        startord_lista = list(startord.word)
    if q.isEmpty():
        print("Finns ej väg till " + slutord)   # Om kön är tom har ordet inte hittats. Skrivet ut till användare.


# Huvudprogram. Tar input från användaren, kallar på makechildren, itererar tills ord hittats eller inte.
angivna_ord = ta_input(svenska)
starten = ParentNode(angivna_ord[0])
slutord = angivna_ord[1]
q.enqueue(starten)
while not q.isEmpty():
    nod = q.dequeue()
    barn = makechildren(nod, slutord, q)
    if barn is True:
        break




