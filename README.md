# Request-Topic-Classification  

Решение команды `Deviаnts` задачи "Обработка обращений граждан" от [Промобота](https://promo-bot.ru/) в рамках Хакатона [Цифровой прорыв](https://hacks-ai.ru).

Решение задачи классификации обращений по темам, которое ускорит время обработки.

Мы автоматизируем процесс обработки неформальных обращений граждан, валидируем обращения на предмет наличия в них конкретных жалоб.
К каждому обращению мы выделяем тему, группу тем и исполнителя.

Для классификации обращений по темам используется `ruBert-base`, выделение именованных сущностей для определения исполнителя происходит с помощью Natasha. Были обучены 2 модели `ruber-tiny2`для определения исполнителя и валидации.

Интерфейс решения представлен в виде чат-бота в Telegram.

Уникальность:
Высокая точность и быстродействие, низкие требования к вычислительным мощностям (решение не использует GPU), предсказание исполнителя.


## Стек решения
`Python`, `Transformers`, `PyTorch`, `Natasha`, `aiogram`.

## [Ссылка на бота](https://t.me/processing_appeals_bot)
Запуск бота в dev-режиме
Перейти в директорию с ботом
```
cd processing_citizens_appeals_tg_bot/
```
Создать файл `config.py` и добавить в него `TOKEN="ВАШ ТОКЕН"` телеграм бота 
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip 
```
```
pip install -r requirements.txt
```
Запустить файл `run.py`


## Файлы 

[`PromoBotSolutionAPI.ipynb `](PromoBotSolutionAPI.ipynb) — хостинг API на Colab (работает на CPU)

[`training_rubert_base_ner.ipynb`](training_rubert_base_ner.ipynb) — обучение ruBert-base на данных с исправленными ошибками и именованными сущностями (лучшая модель на классификацию тем)

[`submit_rubert_base_ner.ipynb`](submit_rubert_base_ner.ipynb) — получение лучшего сабмита

[`processing_citizens_appeals_tg_bot/`](processing_citizens_appeals_tg_bot/) — директория с ботом

[`id2label.json`](id2label.json), [`label2id.json`](label2id.json) — Конвертация классов в числовое представление и наоборот

[`topic2big_topic.json`](topic2big_topic.json) — Сопоставление тем с групой тем

[`Copy_of_training_xlm_base.ipynb`](Copy_of_training_xlm_base.ipynb) — Обучение xlm-roberta-base и ruBert-base на данных с исправленными ошибками

[`main.ipynb`](main.ipynb) — Анализ и предобработка данных, а также незаконченный парсер VK, который планировался для полностью автоматизированного решения

[`toxicity_rubert_tiny.ipynb`](toxicity_rubert_tiny.ipynb) — обучение rubert_tiny2 на текстах и инцидента и [Russian Language Toxic Comments](https://www.kaggle.com/datasets/blackmoon/russian-language-toxic-comments) для определения, валидно ли обращение
