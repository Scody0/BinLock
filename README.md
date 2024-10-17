# BinLock - File Encryption/Decryption

### Version: v0.0.1 beta
### Developed by: Scody

Description:
BinLock is a simple file encryption and decryption tool that uses binary code. It allows users to secure their files with a customizable encryption key. The encryption method is based on the XOR operation between the file data and the key.

Features:
- Encrypt and decrypt files easily.
- User-friendly graphical interface.
- Custom encryption key for enhanced security.

Installation:
1. Make sure you have Python 3.x installed on your machine.
2. Install the required libraries if they are not already installed. You can use pip to install Tkinter, which is included with Python installations by default.

```bash
pip install tk
```

3. Download the BinLock.py file from the repository.

How to Use:
1. Run the BinLock.py file.
2. Enter your encryption key in the designated field.
3. Choose one of the following options:
   - Encrypt File: Select the file you want to encrypt. After choosing the file, specify the output file name to save the encrypted data.
   - Decrypt File: Select the encrypted file you want to decrypt. Specify the output file name to save the decrypted data.
4. Click the corresponding button to execute the action.

How It Works:
- The program reads the input file as binary data.
- It encodes the provided key into bytes.
- The XOR operation is applied between the file data and the key bytes.
- The resulting encrypted or decrypted data is saved to the specified output file.

License:
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Scody0/BinLock/blob/main/LICENSE.md) file for details.

-------------------------
# BinLock - Шифрование/дешифрование файлов

### Версия: v0.0.1 beta
### Разработчик: Scody

Описание:
BinLock — это простой инструмент для шифрования и дешифрования файлов с использованием двоичного кода. Программа позволяет пользователям защитить свои файлы с помощью настраиваемого ключа шифрования. Метод шифрования основан на операции XOR между данными файла и ключом.

Особенности:
- Легкое шифрование и дешифрование файлов.
- Удобный графический интерфейс.
- Настраиваемый ключ шифрования для повышения безопасности.

Установка:
1. Убедитесь, что у вас установлена версия Python 3.x.
2. Установите необходимые библиотеки, если они не установлены. Вы можете использовать pip для установки Tkinter, который включен в стандартную установку Python.

```bash
pip install tk
```

3. Скачайте файл BinLock.py из репозитория.

Как использовать:
1. Запустите файл BinLock.py.
2. Введите ключ шифрования в указанное поле.
3. Выберите один из следующих вариантов:
   - Шифровать файл: Выберите файл для шифрования. После выбора файла укажите имя файла для сохранения зашифрованных данных.
   - Дешифровать файл: Выберите зашифрованный файл для расшифровки. Укажите имя файла для сохранения расшифрованных данных.
4. Нажмите соответствующую кнопку для выполнения действия.

Как это работает:
- Программа считывает входной файл в виде двоичных данных.
- Кодирует указанный ключ в байты.
- Операция XOR применяется между данными файла и байтами ключа.
- Результирующие зашифрованные или расшифрованные данные сохраняются в указанный выходной файл.

Лицензия:
Этот проект лицензирован на условиях лицензии MIT — см. файл [LICENSE](https://github.com/Scody0/BinLock/blob/main/LICENSE.md) для получения дополнительной информации.
