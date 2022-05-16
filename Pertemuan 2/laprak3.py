from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero
from kanren import vars
ukuran = Relation()
warna = Relation()
gelap = Relation()
tingkah = Relation()
facts(ukuran, ("beruang", "besar"),
      ("gajah", "besar"),
      ("kucing", "kecil"))
facts(warna, ("beruang", "cokelat"),
      ("kucing", "hitam"),
      ("gajah", "kelabu"))

fact(gelap, "hitam")
fact(gelap, "cokelat")
x = var()
besar = run(0, x, ukuran(x, "besar"))
print("hewan berukuran besar                          : ", besar)
z = var()
kecil = run(0, z, ukuran(z, "kecil"),
            warna(z, "hitam"))
print("Hewan berukuran kecil dan hitam                : ", kecil)
a = var()
dua = run(0, a, ukuran(a, "besar"),
          warna(a, "cokelat"))
print("Hewan berukuran besar dan berwarna cokelat     : ", dua)
tiga = run(0, z, warna(z, "cokelat" or "hitam"))
print("Hewan berwarna gelap                           : ", tiga)
empat = run(0, z, warna(z, "cokelat"),
            ukuran(z, "besar"))
print("Hewan berwarna cokelat dan besar              : ", empat)
