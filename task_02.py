# TODO Напишите функцию find_common_participants
def find_common_participants(first_str, second_str, separator=','):
    first_str = first_str.split(separator)
    second_str = second_str.split(separator)
    general_list = []
    for index_1 in range(len(first_str)):
        for index_2 in range(len(second_str)):
            if first_str[index_1] == second_str[index_2]:
                general_list.append(first_str[index_1])
    general_list.sort()
    return general_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Проверьте работу функции с разделителем отличным от запятой
