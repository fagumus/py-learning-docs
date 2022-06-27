print("Pizza siparişi ekranına hoş geldiniz!")
size = input("Pizza boyutu? K, O, ya da B ")
add_mushroom = input("Mantar ister misiniz? E ya da H ")
extra_cheese = input("Ekstra peynir ister misiniz? E ya da H ")

bill = 0

if size == 'K':
    bill += 15
    if add_mushroom == 'E':
        bill += 2
elif size == 'O':
    bill += 20
    if add_mushroom == 'E':
        bill += 3
elif size == 'B':
    bill += 25
    if add_mushroom == 'E':
        bill += 3
else:
    print("Sipariş oluşturamadık, geçersiz pizza boyutu seçtiniz.")

if bill != 0:
    if extra_cheese == 'E':
        bill += 1
    choice_text = f"Seçiminiz: boyut = {size} mantar = {add_mushroom} peynir = {extra_cheese}"
    print(choice_text)
    print("Fatura: %d TL" % bill)

