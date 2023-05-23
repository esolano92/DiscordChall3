height = int(input("Choose a height for the tree!"))

def drawtree(height):
    tree ="#"
    centerAlign = 21
    if height == 0:
        tree = '" "'
        print(tree.center(centerAlign, " "))
    else:
        print(tree.center(centerAlign, " "))
        for number in range(1, height):
            tree += "##"
            print(tree.center(centerAlign, " "))
drawtree(height)
