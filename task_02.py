# TODO Найдите количество книг, которое можно разместить на дискете
disk_capacity = 1.44 * 1024 * 1024 #Объем дискеты в байтах
number_of_pages = 100
number_of_lines = 50
number_of_symbol = 25
symbol_size = 4
book_size = number_of_pages * number_of_lines * number_of_symbol * symbol_size
books = disk_capacity // book_size
print("Количество книг, помещающихся на дискету:", int(books))
