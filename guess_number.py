# class BacteriaProducer:
#     maximum_bacteria_now = 0
#     # Допишите инициализатор класса 
#     def __init__(self, max_bacteria):
#         self.bacteria_count = 0  # Изначально количество бактерий равно 0
#         self.max_bacteria = max_bacteria  # Максимально возможное количество бактерий

#     def create_new(self):
#         if self.bacteria_count < self.max_bacteria:
#             self.bacteria_count += 1  # Увеличиваем счетчик бактерий на 1
#             print(f'Добавлена одна бактерия. Количество бактерий в популяции: {self.bacteria_count}')
#         else:
#             print('Нет места под новую бактерию')
#     # Допишите метод
#     def remove_one(self):
#         if self.bacteria_count > 0:
#             self.bacteria_count -= 1  # Уменьшаем счетчик бактерий на 1
#             print(f'Одна бактерия удалена. Количество бактерий в популяции: {self.bacteria_count}')
#         else:
#             print('В популяции нет бактерий, удалять нечего')

# # Пример запуска для самопроверки
# bacteria_producer = BacteriaProducer(max_bacteria=3)
# bacteria_producer.remove_one()
# bacteria_producer.create_new()
# bacteria_producer.create_new()
# bacteria_producer.create_new()
# bacteria_producer.create_new()
# bacteria_producer.remove_one()





# class MushroomsCollector:
#     def __init__(self):
#         self.mushrooms = []  # Изначально корзина пуста

#     def is_poisonous(self, mushroom_name):
#         # Пример проверки на ядовитость
#         poisonous_mushrooms = ['мухомор', 'поганка']  # Список ядовитых грибов
#         return mushroom_name.lower() in poisonous_mushrooms

#     def add_mushroom(self, mushroom_name):
#         if self.is_poisonous(mushroom_name):
#             print('Нельзя добавить ядовитый гриб')
#         else:
#             self.mushrooms.append(mushroom_name)  # Добавляем гриб в корзину
#             print(f'Гриб {mushroom_name} добавлен в корзину')

#     def __str__(self):
#         return ', '.join(self.mushrooms) 
# # Пример запуска для самопроверки
# collector_1 = MushroomsCollector()
# collector_1.add_mushroom('Мухомор')
# collector_1.add_mushroom('Подосиновик')
# collector_1.add_mushroom('Белый')
# print(collector_1)

# collector_2 = MushroomsCollector()
# collector_2.add_mushroom('Лисичка')
# print(collector_1)
# print(collector_2)



# class CipherMaster:
#     alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     def cipher(self, original_text, shift):
#         result = []
#         for letter in original_text:
#             position = self.alphabet.find(letter.lower())
#             if position == -1:
#                 result.append(letter)
#             else:
#                 result.append(self.alphabet[(position + shift) % len(self.alphabet)])
#         return ''.join(result)
#     def decipher(self, cipher_text, shift):
#         result = []
#         for letter in cipher_text:
#             position = self.alphabet.find(letter.lower())
#             if position == -1:
#                 result.append(letter)
#             else:
#                 result.append(self.alphabet[(position - shift) % len(self.alphabet)])
#         return ''.join(result)
# cipher_master = CipherMaster()
# print(cipher_master.cipher(
#     original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
#     shift=2
# ))
# print(cipher_master.decipher(
#     cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
#     shift=-3
# ))



class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def process_text(self, text, shift, is_encrypt):
        result = []
        for letter in text:
            position = self.alphabet.find(letter.lower())
            if position == -1:
                result.append(letter)  # Если символ не в алфавите, добавляем его без изменений
            else:
                if is_encrypt:
                    new_position = (position + shift) % len(self.alphabet)  # Шифрование
                else:
                    new_position = (position - shift) % len(self.alphabet)  # Дешифрование
                result.append(self.alphabet[new_position])  # Добавляем зашифрованный или расшифрованный символ
        return ''.join(result)

# Проверка
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
