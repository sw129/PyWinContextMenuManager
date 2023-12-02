import reg

# Определяем ключ реестра для добавления пункта меню Code.exe
key_path = r"Directory\Background\shell"+r"\name"

# Определяем путь к исполняемому файлу приложения
app_path = r"app_path"

# Определяем название пункта меню
menu_name = "menu_name"

#reg.Add(key_path, app_path, menu_name)
#reg.Del(key_path)