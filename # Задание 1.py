email = input("Введите электронную почту: ")

# 1. Находим позицию символа @ в строке
at_position = email.find("@")

if at_position != -1:
    # 2. Находим длину строки
    email_length = len(email)
    
    # 3. Вырежем подстроку от символа @ до конца строки
    domain = email[at_position + 1 : email_length]
    
    print("Домен почты:", domain)
else:
    print("Ошибка: в тексте нет символа @")
