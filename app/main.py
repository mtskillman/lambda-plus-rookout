from pprint import pp
import json
from typing import Dict
from rook.serverless import serverless_rook

valid_fruits = ["apple", "banana", "pineapple"]

fruitname = str
fruitcount = int


@serverless_rook
def handler(event: Dict[fruitname, fruitcount], _):
    # yes, intentionally broken logic.
    pp(event)
    top_fruits = []
    for fruit_name, fruit_count in event.items():
        if fruit_name in valid_fruits:
            print(f'fruit name {fruit_name} found in valid fruits')
            top_fruits.append(fruit_count)
    print('top fruits: ', top_fruits)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'topFruit': top_fruits[-1]
        })
    }
