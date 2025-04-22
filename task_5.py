class TestCase:

    def __init__(self):
        self.steps = {}
        self.result = None

    # метод, который добавляет в словарь steps шаг тест-кейса
    def set_step(self, step_number, step_text):
        if 'Шаги' not in self.steps:
            self.steps['Шаги'] = {}
        self.steps['Шаги'][step_number] = step_text

    # метод, который удаляет шаг из steps по ключу step_number
    def delete_step(self, step_number):
        self.steps['Шаги'].pop(step_number)

    # метод, который устанавливает ожидаемый результат
    def set_result(self, result):
        self.steps['Ожидаемый результат'] = result
    
    # метод, который выводит на экран информацию о составе тест-кейса
    def get_test_case(self):
        print(self.steps)


test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()


test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()