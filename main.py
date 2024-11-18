# Словарь
books = [
    { "title":"Война и мир", "author": "Лев Толстой", "year": "1850"},
    {"title":"Дом в котором автор", "author": "Мариам Петросян", "year": "1869" },
    {"title":"негр", "author": "никитос", "year": "2009" },
    {"title":"шляпа", "author": "владос", "year": "2008"},
    {"title":"абаюнда", "author": "артем", "year": "2013"},
 ]
 # Перебор всех книг и вывод информации
for i in range(len(books)):
    print(f"          Книга {i + 1}          " )
    print(f"название: {books[i]["title"]} aвтор: {books[i]["author"]} ")
    print(f"          {books[i]['year']}          ")
    print()
 