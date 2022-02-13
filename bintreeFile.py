class TreeNode:
    """Klass för trädnod"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Bintree:
    """Klass för binärt sökträd. Instansvariabel root. Metoder put, contains och write."""
    def __init__(self):
        self.__root = None

    def put(self, newvalue):
        self.__root = putta(self.__root, newvalue)  # Kallar på hjälpfunktion putta, vill addera value.

    def __contains__(self, value):
        return finns(self.__root, value)  # Kallar på hjälpfunktion finns, söker value.

    def write(self):            # Kallar på hjälpfunktion skriv, skriver ut inorder, LPR
        skriv(self.__root)
        print("\n")


def putta(root, value): # Tar in rot för binärt träd samt värde att lägga till
    """Jämför värden från rot nedåt till korrekt plats hittas att placera value, rekursivt"""
    if root == None:
        return TreeNode(value)      # Lägger till nod, basfall
    else:
        if root.value == value:     # Fångar dublett
            return root
        elif root.value > value:
            root.left = putta(root.left, value)     # Går vänster om value mindre än root
        else:
            root.right = putta(root.right, value)   # Går höger om value större än root
    return root


def finns(root, value):   # Tar in rot för binärt träd samt värde att söka efter
    """Binärsök value i trädet, rekursivt"""
    if root == None:
        return False                # Basfall, om ej hittad
    else:
        if value == root.value:     # Returnerar True om värdet hittas
            return True
        elif value < root.value:                # Går vänster om värdet är mindre än roten
            return finns(root.left, value)
        else:
            return finns(root.right, value)     # Går höger om värdet är större än roten


def skriv(root):
    """Går igenom trädet och skriver up i inorder (LPR), rekursivt"""
    if root == None:
        return None             # Basfall
    else:
        skriv(root.left)
        print(root.value)
        skriv(root.right)

