from PIL import Image

cards = {"день рождения": "cards/dr.jpg", "новый год": "cards/newy.jpg","1 сентября": "cards/1st.jpg"}
print("День рождения, Новый год, 1 сентября")
holiday = input("Введите название праздника: ").lower()

if holiday in cards:
    card = Image.open(cards[holiday])
    card.show()
else:
    print("Открытки нет")