import kanren
from kanren.facts import Relation, facts
from kanren.core import var, run, conde


def get_saudara(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))


if __name__ == '__main__':
    parent = Relation()
    facts(parent, ("Slamet", "Amin"),
          ("Slamet", "Anang"),
          ("Amin", "Badu"),
          ("Amin", "Budi"),
          ("Anang", "Didi"),
          ("Anang", "Dadi"))
    x = var()
    child = "Amin"
    ayah = run(1, x, parent(x, child))
    print("\nNama ayah " + child + ": ")
    for item in ayah:
        print(item)

    grandfather = run(0, x, get_saudara(x, "Dadi"))
    siapa = "Dadi"
    grandfather = [x for x in grandfather if x != siapa]
    print("\nNama Kakeknya " + siapa + " adalah : ")
    for item in grandfather:
        print(item)

    uncle = run(0, x, get_saudara(x, "Budi"))
    siapa = "Budi"
    uncle = [x for x in uncle if x != siapa]
    print("\nNama Paman " + siapa + " : ")
    for item in uncle:
        print(item)


child = run(0, x, get_saudara(x, "Anang"))
objek = "Anang"
child = [x for x in child if x != objek]
print("\nNama Paman " + objek + " : ")
for item in child:
    print(item)
