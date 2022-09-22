## vk_api-stubs

Стабы для модуля vk_api

100% покрытие типов + автодополнение методов API(так же включает методы для работы с аудио)

## Установка
`pip install vk_api-stubs`

## Зачем?
Стабы нужны для проверки типов в IDE

## Автодополнение
Методы API описаны в объекте `VkApiMethod` чтобы его получить надо вызвать `get_api`
```python
import vk_api

TOKEN = "VK API TOKEN"
vk = vk_api.VkApi(token=token)
api = vk.get_api() # тут объект VkApiMethod
```
![Screenshot](img/1.jpg)
![Screenshot](img/2.jpg)
