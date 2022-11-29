import qrcode
from uuid import uuid4


NAMED_CLUES = {
    (0, 0): 'The code you need is in this grid',
    (0, 2): 'This is the left side',
    (1, 0): 'The grid is zero-indexed, like all things should be, like floor numbering',
    (1, 3): 'The Y coordinate is your birthday’s month, MOD 9',
    (2, 2): '<SOLUTION>',
    (3, 1): 'The X coordinate is your birthday’s day, MOD 9',
    (4, 0): 'Say no to pineapple',
    (5, 1): 'The title isn’t part of the grid',
    (5, 3): 'Tough luck',
    (4, 2): 'Coordinates here work like on a GUI app',
    (6, 3): 'This is the right side'
}

OTHER_QRS = {
    'good_luck.png': 'Good luck with your quest! You might find some clues and learn some important life things by scanning through a few items :)',
    'happy_birthday.png': 'Happy birthday Bjørnardo! <3 Fede & Daniele',
    'we_got_you_a_gift.png': 'We got you a yummy gift, but you will have to work for it!',
    'coffee.png': 'It might take some time to get through, so we got you some "coffee" for the journey!',
    'gift_card.png': 'Here is the code for your gift:',
    'gift_card_code.png': 'https://www.amoi.no?redeem_gift_voucher=<UH-OH>',
    'gift_card_quest.png': 'Oh but it\'s incomplete? Guess you\'d better hurry and find the rest of the code!',
}


def render_qr(text: str, x: int, y: int):
    img = qrcode.make(text)
    img.save(f"output/{x}_{y}_qr.png")


def render_extra(text: str, filename: str):
    img = qrcode.make(text)
    img.save(f"output/extras/{filename}")


if __name__ == '__main__':
    for x in range(7):
        for y in range(4):
            if txt := NAMED_CLUES.get((x, y)):
                render_qr(txt, x, y)
            else:
                render_qr(str(uuid4()), x, y)

    for k, v in OTHER_QRS.items():
        render_extra(v, k)
