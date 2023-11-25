import torch
from transformers import AutoTokenizer

from .load_json_files import get_id_to_label

model = torch.load("files/rubert.pt", map_location=torch.device('cpu'))
model.eval()
checkpoint = "cointegrated/rubert-tiny2"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
id2label = get_id_to_label()


async def classificate_text(text_to_classificate: str) -> str:
    tokens = tokenizer(text_to_classificate, truncation="longest_first", padding="max_length", max_length=512)
    tokens = {key: torch.tensor(val).long() for key, val in tokens.items()}
    for key in tokens:
        tokens[key] = tokens[key].unsqueeze(0)
    pred = model(**tokens)
    return id2label[str(pred["logits"].argmax().item())]
