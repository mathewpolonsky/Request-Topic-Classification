def get_formated_text(classification_dict):
    topic = classification_dict.get("Тема")
    big_topic = classification_dict.get("Группа тем")
    ner = classification_dict.get("Ners")
    validation = classification_dict.get("Валидации")
    contractor = classification_dict.get("Исполнитель")
    if not ner:
        ner = "Не найдено\n"
    text = f'''
*Обработка завершена!*

*Валидация:*
{validation}

*Тема*:
{topic}

*Группа тем:*
{big_topic}

*Локации и организации*:
{ner}
*Исполнитель:*
{contractor}
'''
    return text
