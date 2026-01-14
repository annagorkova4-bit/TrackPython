# TODO  Напишите функцию count_letters
def count_letters(text_str):
    main_dic = {}
    text_str = text_str.lower()
    for symbol in text_str:
        if  symbol.isalpha():
            if symbol in main_dic:
                main_dic[symbol] += 1
            else:
                main_dic[symbol] = 1
    return main_dic

# TODO Напишите функцию calculate_frequency
def calculate_frequency(main_dic):
    new_main_dic = {}
    sum_symbol=sum(main_dic.values())
    for symbol in main_dic:
        new_main_dic[symbol] = round(main_dic[symbol] / sum_symbol, 2)
    return new_main_dic

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
main_dic=count_letters(main_str)
new_main_dic=calculate_frequency(main_dic)
for key, value in new_main_dic.items():
    print(f"{key}: {value:.2f}")