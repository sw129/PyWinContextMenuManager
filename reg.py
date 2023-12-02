# Импортируем модуль для работы с реестром
import winreg

def Add(key_path, app_path, menu_name):
    # Открываем ключ реестра для записи
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)

    # Устанавливаем название пункта меню
    winreg.SetValue(key, "", winreg.REG_SZ, menu_name)

    # Устанавливаем иконку приложения
    winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, app_path)

    # Создаем подключ для команды запуска приложения
    subkey = winreg.CreateKey(key, "command")

    # Устанавливаем команду запуска приложения с параметром %V
    winreg.SetValue(subkey, "", winreg.REG_SZ, f'"{app_path}" "%V"')

    # Закрываем ключи реестра
    subkey.Close()
    key.Close()

def Del(key_path):
    # Открываем ключ реестра для записи
    key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path, 0, winreg.KEY_WRITE)

    # Удаляем подключ для команды запуска приложения
    winreg.DeleteKey(key, "command")

    # Закрываем ключ реестра
    key.Close()

    # Удаляем ключ реестра для пункта меню
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, key_path)
