import Play


class GoMon:
    def __init__(self, name, element, power):
        # TODO: Implementasikan code anda disini
        self.nama = name
        self.element = element
        self.power = power
        print()

    def getNama(self):
        return self.nama

    def getElement(self):
        return self.element

    def getPower(self):
        return self.power

    def add(self, otherGoMon):
        # TODO: Implementasikan code anda disini
        name = self.nama + otherGoMon.nama
        elemen = self.element if self.power >= otherGoMon.power else otherGoMon.element
        power = int((self.power + otherGoMon.power)+((self.power + otherGoMon.power)/2) if self.element == otherGoMon.element else (self.power+otherGoMon.power)/2)
        return GoMon(name, elemen, power)

    def __str__(self):
        # TODO: Implementasikan code anda disini
        string = "===========GoMon===========\n"
        string += "nama     : %smon\n" %self.nama.capitalize()
        string += "elemen   : %s\n" %self.element
        string += "kekuatan : %s\n" %self.power
        return string


war = GoMon("war", "api", 1000)
sup = GoMon("sup", "api", 500)
leo = GoMon("leo", "api", 700)
goma = GoMon("goma", "air", 6000)
grey = GoMon("grey", "air", 400)
lada = GoMon("lada", "tumbuhan", 8500)
ku = GoMon("ku", "tumbuhan", 10)
pal = GoMon("pal", "tumbuhan", 11500)
rai = GoMon("rai", "api", 500)
te = GoMon("te", "api", 700)
mo = GoMon("mo", "air", 500)
lost = GoMon("lost", "air", 1000)

print("GoMon Start")
print(war)
print(sup)
print(leo)
print(goma)
print(grey)
print(lada)
print(ku)
print(pal)
print(rai)
print(te)
print(mo)
print(lost)
print()

newmon1 = war.add(grey)
newmon2 = sup.add(mo)
newmon3 = te.add(mo)
newmon4 = sup.add(lost)
newmon5 = lada.add(ku)
newmon6 = sup.add(lada)
newmon7 = war.add(te)
newmon8 = lost.add(grey)
newmon9 = pal.add(sup)
newmon10 = grey.add(ku)

print()
print("GoMon join")
print(newmon1)
print(newmon2)
print(newmon3)
print(newmon4)
print(newmon5)
print(newmon6)
print(newmon7)
print(newmon8)
print(newmon9)
print(newmon10)

Play.greaterThan(war, lost)     # Outputnya : False
Play.greaterThan(sup, lada)     # Outputnya : True
Play.greaterThan(leo, te)       # Outputnya : False
Play.lowerThan(goma, grey)      # Outputnya : False
Play.lowerThan(grey, lost)      # Outputnya : True
Play.lowerThan(lada, war)       # Outputnya : True
Play.equals(ku, mo)             # Outputnya : False
Play.equals(pal, sup)           # Outputnya : False
Play.equals(rai, sup)           # Outputnya : True
Play.greaterThan(te, war)       # Outputnya : False
Play.lowerThan(mo, mo)          # Outputnya : False
Play.greaterThan(lost, leo)     # Outputnya : True
