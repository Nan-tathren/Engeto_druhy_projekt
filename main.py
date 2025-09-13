import random

def uvod():
    print("""
        Hi there!
        -----------------------------------------------
        I've generated a random 4 digit number for you.
        Let's play a bulls and cows game.
        -----------------------------------------------
        Enter a number:
        -----------------------------------------------
        """
        )

def vytvor_tajne_cislo():
    cisla = []
    while len(cisla) < 4:
        number = random.randint(0, 9)
        if len(cisla) and number == 0:
            continue
        
        if number not in cisla:
            cisla.append(number)
        
    return "".join(str(d) for d in cisla)    
    
    
def validuj_tip():
    while True:
        tip = input('Enter a number: ')

        if len(tip) == 4 and tip.isdigit() and tip[0] != '0' and len(set(tip)) == len(tip):
            return tip
        else:
            print('You need to enter 4 original digits that do not start with a zero!')


def vyhodnoceni_bulls_cows(tajne_cislo, tip):
    bulls = 0
    cows = 0
    
    for i in range(len(tajne_cislo)):
        if tajne_cislo[i] == tip[i]:
            bulls += 1

    for i in range(len(tip)):
        if tip[i] in tajne_cislo and tip[i] != tajne_cislo[i]:
            cows += 1

    return bulls, cows


def vypis_vysledek(bulls: int, cows: int) -> None:
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_text}, {cows} {cow_text}")

def main():
    """hlavni smycka hry"""
    uvod()
    tajne_cislo = vytvor_tajne_cislo()
    while True:
        tip = validuj_tip()
        bulls, cows = vyhodnoceni_bulls_cows(tajne_cislo, tip)
        vypis_vysledek(bulls, cows)
        if bulls == 4:
            print('congratz')
            break

if __name__ == "__main__":
    main()
