#tytułu, ilości stron, autora, data wydania, właściciel
class ksiazka:
    def __init__(self, tytuł, ilosc_stron, autor, data_wydania, właściciel):
        self.tytuł = tytuł
        self.ilosc_stron = ilosc_stron
        self.autor = autor
        self.data_wydania = data_wydania
        self.właściciel = właściciel

    def NowyWłaściciel (self, nowyWłaściciel):
        self.właściciel = nowyWłaściciel

poczatek ="k"
lista_książek =[]
i = 1
która = int(input("ile książek chcesz wpisać: "))
while(i<=która):
    print("Wpisz informacje o książce")
    tytuł = input("Tytuł: ")
    ilosc_stron = int(input("Ilość stron: "))
    autor = input("Autor: ")
    data_wydania = input("Data wydania: ")
    właściciel = input("Właściciel: ")
    książka = poczatek + str(i)
    książka = ksiazka(tytuł,ilosc_stron,autor,data_wydania, właściciel)
    lista_książek.append(książka)
    i+=1

co = input("Czego chcesz się dowiedzieć? ")
match co:
    case "tytuł":
        for k in lista_książek: print(k.tytuł)
    case "ilość stron":
        for k in lista_książek: print(k.ilosc_stron)
    case "autor":
        for k in lista_książek: print(k.autor)
    case "data wydania" : 
        for k in lista_książek: print(k.data_wydania)
    case "właściciel":
        for k in lista_książek: print(k.właściciel)








