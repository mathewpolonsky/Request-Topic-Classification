import json

big_topic_path = 'files/topic2big_topiс_stars.json'

with open(big_topic_path, 'r', encoding='UTF-8') as file:
    json_dict = json.load(file)

def get_id_to_label():
    id2label_path = 'files/id2label.json'
    with open(id2label_path, 'r', encoding='UTF-8') as file:
        id2label = json.load(file)
        return id2label

async def get_big_topic(topic: str) -> str:
    return json_dict[topic]
