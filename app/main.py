from pprint import pp
import json
from typing import Dict

valid_fruits = ["apple", "banana", "pineapple"]

fruitname = str
fruitcount = int


def handler(event: Dict[fruitname, fruitcount], _):
    # yes, intentionally broken logic.
    pp(event)
    top_fruits = []
    for fruit_name, fruit_count in event.items():
        if fruit_name in valid_fruits:
            top_fruits.append(fruit_count)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'topFruit': top_fruits[-1]
        })
    }
