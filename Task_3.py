from PIL import Image, ImageDraw, ImageFont

cards = {"день рождения": "cards/dr.jpg", "новый год": "cards/newy.jpg","1 сентября": "cards/1st.jpg"}
print("День рождения, Новый год, 1 сентября")

holiday = input("Введите праздник: ").lower()
name = input("Введите имя: ")

if holiday in cards:
    filename = cards[holiday]
    card = Image.open(filename)
    draw = ImageDraw.Draw(card)
    font = ImageFont.truetype("arial.ttf", 50)
    message = f"{name}, поздравляю!"

    if holiday == "день рождения":
        day = "dr"
        position = (110, 540)
        color = (0, 0, 0)
    elif holiday == "новый год":
        day = "newy"
        position = (300, 900)
        color = (255, 70, 0)
    else:
        day = "1st"
        position = (325, 900)
        color = (255, 0, 0)

    draw.text(position, message, font=font, fill=color, stroke_width=2, stroke_fill=(255, 255, 255))
    card.show()

    card.save(f"new_cards/{name}_{day}.png")
else:
    print("error")