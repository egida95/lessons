# import random 

# while True:
    
#     user_action = input('Сделайте выбор-камень,ножницы или бумага>>> ')
#     possible_actions = ['ножницы', 'камень', 'бумага']
#     computer_action = random.choice(possible_actions)
#     print(f'Вы выбрали {user_action},программа выбрала{computer_action}.\n')

#     if user_action == computer_action:
#         print(f"Оба пользователя выбрали {user_action}. Ничья!!")
#     elif user_action == "камень":
#         if computer_action == "ножницы":
#             print("Камень бьет ножницы! Вы победили!")
#         else:
#             print("Бумага оборачивает камень! Вы проиграли.")
    
#     elif user_action == "бумага":
#         if computer_action == "камень":
#             print("Бумага оборачивает камень! Вы победили!")
#         else:
#             print("Ножницы режут бумагу! Вы проиграли.")
    
#     elif user_action == "ножницы":
#         if computer_action == "бумага":
#             print("Ножницы режут бумагу! Вы победили!")
#         else:
#             print("Камень бьет ножницы! Вы проиграли.")
            
#     play_again = "" 
#     play_again = input("Сыграем еще? (д/н): ") 
#     if play_again.lower() != "д": 
#         break
    
    