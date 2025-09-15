import random

def uvod():
        """uvodni funkce vysvetlujici jak hrat"""
        print("""
        Hi there!
        -----------------------------------------------
        I've generated a random 4 digit number for you.
        Let's play a bulls and cows game.
        -----------------------------------------------
        Enter a number:
        -----------------------------------------------
        """)

def vytvor_tajne_cislo():
    """funkce vytvarejici tajne cislo"""
    cisla = []
    while len(cisla) < 4:
        number = random.randint(0, 9)
        if not cisla and number == 0:
            continue
        if number not in cisla:
            cisla.append(number)
    return "".join(str(d) for d in cisla)

def validuj_tip():
    """funkce kontrolujici input od uzivatele, nesmi zacinat nulou a vsechny cisla musi byt original"""
    while True:
        tip = input('Enter a number: ')
        if len(tip) == 4 and tip.isdigit() and tip[0] != '0' and len(set(tip)) == len(tip):
            return tip
        else:
            print('You need to enter 4 original digits that do not start with a zero!')

def vyhodnoceni_bulls_cows(tajne_cislo, tip):
    """Vrátí počet bulls (správná číslice i pozice) a cows (správná číslice, špatná pozice)."""
    bulls = cows = 0
    for i, c in enumerate(tip):
        if c == tajne_cislo[i]:
            bulls += 1
        elif c in tajne_cislo:
            cows += 1
    return bulls, cows

def vypis_vysledek(bulls: int, cows: int) -> None:
    """Vypíše výsledek ve formátu 'x bulls, y cows'."""
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_text}, {cows} {cow_text}")

def main():
    """Hlavní smyčka hry."""
    uvod()
    tajne_cislo = vytvor_tajne_cislo()
    pokusy = 0
    while True:
        tip = validuj_tip()
        pokusy += 1
        bulls, cows = vyhodnoceni_bulls_cows(tajne_cislo, tip)
        vypis_vysledek(bulls, cows)
        if bulls == 4:
            print(f'Congratz! You guessed it in {pokusy} attempts.')
            break

if __name__ == "__main__":
    main()
