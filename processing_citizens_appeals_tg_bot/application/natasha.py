from natasha import Doc, NewsEmbedding, NewsNERTagger, MorphVocab, Segmenter

emb = NewsEmbedding()
ner_tagger = NewsNERTagger(emb)
morph_vocab = MorphVocab()
segmenter = Segmenter()


def get_ners(text):
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_ner(ner_tagger)
    for span in doc.spans:
        span.normalize(morph_vocab)
    ner_dict = {}
    for span in doc.spans:
        if span.normal not in ner_dict.get(span.type, []):
            ner_dict[span.type] = ner_dict.get(span.type, []) + [span.normal]
    return ner_dict


def get_ru_ner_labels(text):
    if text == 'PER':
        return 'Персона'
    elif text == 'LOC':
        return 'Локация'
    elif text == 'ORG':
        return 'Организация'
    else:
        return 'Неопознанная сущность'


def get_ners_pretty(text):
    ners = get_ners(text)
    result = ''
    for key, value in ners.items():
        result += f'{get_ru_ner_labels(key)}: {", ".join(value)}\n'
    return result
