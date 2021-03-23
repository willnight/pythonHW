from random import choice
# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?  - да
# Сможете ли вы сделать аргументы именованными? - да

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num, can_repeat=True):
    """
      Generates random jokes from 3 lists - 1 word from each list

      :param int num: jokes repeats
      :param bool can_repeat: can words repeats
      :return: list of jokes
    """

    jokes = []
    if can_repeat:
        for i in range(0, num):
            jokes.append(' '.join([choice(nouns), choice(adverbs), choice(adjectives)]))
        return jokes
    else:
        for i in range(0, num):
            if len(nouns) > 0 and len(adverbs) > 0 and len(adjectives) > 0:
                noun, adverb, adjective = choice(nouns), choice(adverbs), choice(adjectives)
                jokes.append(' '.join([noun, adverb, adjective]))
                nouns.remove(noun)
                adverbs.remove(adverb)
                adjectives.remove(adjective)
        return jokes


print(get_jokes(7))
print(get_jokes(6, can_repeat=False))