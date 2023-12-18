from typing import List
from PIL import Image, ImageDraw, ImageFont

def get_meme(template_name: str, text_list: List[str]) -> Image:
    if template_name not in templates:
        print('Неизвестный шаблон')

        return
    image_path = f'templates/{template_name}.jpg'

    img = Image.open(image_path)

    draw = ImageDraw.Draw(img)

    font_path = 'C:/Users/user/vscode/memegenerator/arial (1).ttf'

    font = ImageFont.truetype(font=font_path, size=36)

    for i, text in enumerate(text_list):
        print(i, text)
        x = templates[template_name]['positions'][i]['x']
        y = templates[template_name]['positions'][i]['y']
        wrap = templates[template_name]['positions'][i]['wrap']


        while len(text) > 0:
            draw.text((x, y), text[:wrap], font=font, fill='#5178a3')
            y += 40
            print(text)
            text = text[wrap:]

    return img

templates = {
    'frog': {
        'positions': [{
            'x': 0,
            'y': 0,
            'wrap': 13,
            'font_size': 36
        }],
    },
    'drake': {
        'positions':[ {
            'x': 333,
            'y': 35,
            'wrap': 13,
            'font_size': 36
        }, {
            'x':333,
            'y':339,
            'wrap': 13,
            'font_size': 36
            }],
    },
    'but': {
        'positions':[ {
            'x': 92,
            'y': 84,
            'wrap': 13,
            'font_size': 36
        }, {
            'x':80,
            'y':217,
            'wrap': 13,
            'font_size': 36
            }]
    },
    'sad': {
        'positions': [{
            'x': 530,
            'y': 115,
            'wrap': 13,
            'font_size': 36
        }],
    },
    'head': {
        'positions': [{
            'x': 483,
            'y': 440,
            'wrap': 13,
            'font_size': 36
        }],
    },
    'perfect': {
        'positions': [{
            'x': 300,
            'y': 170,
            'wrap': 13,
            'font_size': 36
        }],
    },
    'agree': {
        'positions': [{
            'x': 560,
            'y': 170,
            'wrap': 13,
            'font_size': 36
        }],
    },
}

text=['higofdhkjkjdcsagergegergegrqwgk', 'ssds']




get_meme(template_name='drake', text_list=text).save('test1.jpg')


