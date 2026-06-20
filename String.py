email = input("Введите электронную почту: ")
at_position = email.find("@")

if at_position != -1:
    email_length = len(email)
    domain = email[at_position + 1 : email_length]
    print("Домен почты:", domain)
else:
    print("Ошибка: в тексте нет символа @")
