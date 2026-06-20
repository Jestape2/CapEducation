import random

def get_computer_choice():
    varianty = ["камень", "ножницы", "бумага"]
    return random.choice(varianty)

def determine_winner(vvod_igroka, vvod_kompa):
    if vvod_igroka == vvod_kompa: 
        return "nichya"
    
    if (vvod_igroka == "камень" and vvod_kompa == "ножницы") or \
       (vvod_igroka == "ножницы" and vvod_kompa == "бумага") or \
       (vvod_igroka == "бумага" and vvod_kompa == "камень"):
        return "igrok"
    
    return "komputer"

def main():
    print("Игра до 3 очков.")
    ochki_igroka = 0
    ochki_kompa = 0
    
    while ochki_igroka < 3 and ochki_kompa < 3:
        vvod_polzovatelya = input("\nВаш ход: ").lower().strip()
        peremennaya_kompa = get_computer_choice()
        print(f"Компьютер: {peremennaya_kompa}")
        
        itog_raunda = determine_winner(vvod_polzovatelya, peremennaya_kompa)
        
        if itog_raunda == "igrok": 
            ochki_igroka += 1
        elif itog_raunda == "komputer": 
            ochki_kompa += 1
            
        print(f"Счет: {ochki_igroka} - {ochki_kompa}")
        
    print(f"\nФинальный счет: {ochki_igroka} - {ochki_kompa}")
    if ochki_igroka == 3:
        print("Вы победили!")
    else:
        print("Победил компьютер.")

if __name__ == "__main__":
    main()
