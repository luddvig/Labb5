from bintreeFile import Bintree
from LinkedQFile import LinkedQ

gamla = Bintree()       # Initierar träd för gamla ord
svenska = Bintree()     # Initierar träd för svenska ordlistan
q = LinkedQ()           # Initierar länkad lista för att iterera över barn

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
    """Klass för noder i träd. Har ord som data samt pekare för förälder"""
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent


def writechain(slutnod):
    """Rekursiv funktion för att skriva ut väg från startord (rot i träd) till slutord (barn på lägre nivå)"""
    if slutnod.parent == None:
        print(slutnod.word)         # Basfall för roten
    else:
        writechain(slutnod.parent)  # Kallar rekursivt på funktionen
        print(slutnod.word)         # Skriver ut när skapad stack-frame har exekverats


def makechildren(startord, slutord, q):
    """Funktion för bredden-först-sökning. Kontrollerar om det finns en väg till slutord från givet startord"""
    if startord.word == slutord:
        print("Du har angett samma ord för start och slut.")    # Om användaren anger samma start och slut
        return True
    gamla.put(startord.word)                                    # Startordet placeras i trädet för gamla ord
    startord_lista = list(startord.word)
    bokstaver = "abcdefghijklmnopqrstuvwxyzåäö"
    for bokstav_position in range(len(startord_lista)):
        for bokstaven in bokstaver:
            startord_lista[bokstav_position] = bokstaven
            nytt_ord = "".join(startord_lista)
            if nytt_ord in svenska and nytt_ord not in gamla:   # Om nya ordet finns i svenska och inte använts.
                ny_nod = ParentNode(nytt_ord)                   # Skapar ny nod för nya ordet
                ny_nod.parent = startord                        # Anstätter startnoden som förälder
                if nytt_ord == slutord:                         # Om slutordet hittas
                    print("Finns denna väg till " + slutord + ": ", end="\n")
                    writechain(ny_nod)                          # Kallar på writechain för att skriva ut väg
                    return True                                 # Returnerar True för att stoppa loop i huvudprogram
                else:                                           # Om nya svenska ordet inte var slutordet
                    gamla.put(nytt_ord)                         # Lägger in ordet i trädet för gamla ord
                    q.enqueue(ny_nod)                           # Lägger in nya noden sist i kön
        startord_lista = list(startord.word)
    if q.isEmpty():
        print("Finns ej väg till " + slutord)   # Om kön är tom har ordet inte hittats. Skrivet ut till användare.


# Huvudprogram. Tar input från användaren, kallar på makechildren, itererar tills ord hittats eller inte.
angivna_ord = ta_input(svenska)
starten = ParentNode(angivna_ord[0])            # Skapar startnod
slutord = angivna_ord[1]
q.enqueue(starten)                              # Lägger startnod först i kön
while not q.isEmpty():
    nod = q.dequeue()                           # Hämtar noden först i kön
    barn = makechildren(nod, slutord, q)        # Kallar på makechildren()
    if barn is True:                            # Stannar loop om väg till slutord hittas
        break





