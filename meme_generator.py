from typing import List
from PIL import Image, ImageDraw, ImageFont

def get_meme(template_name: str, text_list: List[str]) -> Image:
    if template_name not in templates:
        print('Неизвестный шаблон')

        return
    image_path = f'templates/{template_name}.jpg'

    img = Image.open(image_path)

    draw = ImageDraw.Draw(img)

    font_path = 'C:/Users/user/vscode/memegenerator/arial.ttf'

    for i, text in enumerate(text_list):
        print(i, text)
        x = templates[template_name]['positions'][i]['x']
        y = templates[template_name]['positions'][i]['y']
        wrap = templates[template_name]['positions'][i]['wrap']
        font_size = templates[template_name]['positions'][i]['font_size']
        font = ImageFont.truetype(font=font_path, size=font_size)
        part = text
        while len(part) > 0:
            if len(part) >= wrap:
                if part[wrap-1] == " ":
                    part = part[:wrap]
                elif part[wrap] == " ":
                    part = part[:wrap]
                elif part[wrap-2] == " ":
                    part = part[:wrap-1]
                else:
                    part = part[:wrap] + '-'
            draw.text((x, y), part, font=font, fill='#5178a3')
            y += 40
            part = text[wrap:]
            text = text[wrap:]

    return img

templates = {
    'frog': {
        'positions': [{
            'x': 0,
            'y': 0,
            'wrap': 16,
            'font_size': 36,
        }],
    },
    'drake': {
        'positions': [{
            'x': 333,
            'y': 35,
            'wrap': 16,
            'font_size': 36,
        }, {
            'x': 333,
            'y': 339,
            'wrap': 13,
            'font_size': 36,
            }],
    },
    'but': {
        'positions':[ {
            'x': 62,
            'y': 54,
            'wrap': 13,
            'font_size': 24,
        }, {
            'x': 80,
            'y': 217,
            'wrap': 12,
            'font_size': 24,
            }]
    },
    'sad': {
        'positions': [{
            'x': 530,
            'y': 115,
            'wrap': 11,
            'font_size': 36,
        }],
    },
    'head': {
        'positions': [{
            'x': 483,
            'y': 360,
            'wrap': 14,
            'font_size': 36,
        }],
    },
    'perfect': {
        'positions': [{
            'x': 300,
            'y': 170,
            'wrap': 15,
            'font_size': 36,
        }],
    },
    'agree': {
        'positions': [{
            'x': 560,
            'y': 170,
            'wrap': 17,
            'font_size': 42,
        }],
    },
}

text=['я кстати работаю в фсб', 'не волнуйся я тоже']

get_meme(template_name='but', text_list=text).save('test.jpg')