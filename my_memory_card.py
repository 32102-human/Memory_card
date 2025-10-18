
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QRadioButton, QGroupBox)
from PyQt5.QtCore import QTimer

class Question:
    def __init__(self, question: str, answers: list, correct_answer_index: int):
        self.question = question
        self.answers = answers
        self.correct_answer_index = correct_answer_index

class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memory Card - Старт')
        self.setGeometry(100, 100, 400, 200)
        self.init_ui()

    def init_ui(self):
        self.start_label = QLabel("Добро пожаловать в викторину!")
        self.start_button = QPushButton('Начать тест')
        self.start_button.clicked.connect(self.start_test)
        layout = QVBoxLayout()
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def start_test(self):
        self.main_window = App()
        self.main_window.show()
        self.close()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memory Card')
        self.setGeometry(100, 100, 400, 300)
        self.questions = [
            Question("Государственный язык Бразилии?", ["Португальский", "Английский", "Испанский", "Бразильский"], 0),
            Question("Какой национальности не существует?", ["Энцы", "Чулымцы", "Смурфы", "Алеуты"], 2),
            Question("Какой океан самый большой?", ["Атлантический", "Индийский", "Тихий", "Северный"], 2),
            Question("Сколько континентов на Земле?", ["5", "6", "7", "8"], 2),
            Question("Какой элемент имеет химический символ O?", ["Золото", "Кислород", "Углерод", "Азот"], 1),
            Question("Где находится Эйфелева башня?", ["Лондон", "Париж", "Рим", "Мадрид"], 1),
            Question("Кто написал 'Войну и мир'?", ["Тургенев", "Достоевский", "Толстой", "Чехов"], 2),
            Question("Какой планеты нет в нашей солнечной системе?", ["Земля", "Марс", "Юпитер", "Планета X"], 3),
            Question("Столица Японии?", ["Пекин", "Сеул", "Токио", "Бангкок"], 2),
            Question("Кто автор 'Гарри Поттера'?", ["Толкин", "Роулинг", "Кинг", "Маркес"], 1),
            Question("Какой газ преобладает в атмосфере Земли?", ["Кислород", "Азот", "Углекислый газ", "Водород"], 1),
            Question("Кто открыл закон всемирного тяготения?", ["Эйнштейн", "Ньютон", "Галилей", "Кеплер"], 1),
            Question("Какой язык программирования самый популярный в 2023 году?", ["Python", "Java", "C++", "JavaScript"], 0),
            Question("Сколько планет в Солнечной системе?", ["7", "8", "9", "10"], 1),
            Question("Кто написал 'Мастер и Маргарита'?", ["Достоевский", "Булгаков", "Толстой", "Чехов"], 1),
            Question("Какой год считается годом основания Рима?", ["753 до н.э.", "476 н.э.", "1066 н.э.", "1492 н.э."], 0),
            Question("Какой металл является самым легким?", ["Алюминий", "Литий", "Железо", "Золото"], 1),
            Question("Кто написал '1984'?", ["Оруэлл", "Хаксли", "Брэдбери", "Толкин"], 0),
            Question("Какой город является столицей Австралии?", ["Сидней", "Мельбурн", "Канберра", "Брисбен"], 2),
            Question("Кто изобрел телефон?", ["Эдисон", "Белл", "Тесла", "Маркони"], 1),
            Question("Какой цвет является символом мира?", ["Красный", "Зелёный", "Синий", "Белый"], 3),
            Question("Сколько стран в Европе?", ["34", "48", "50", "60"], 2),
            Question("Кто был первым человеком на Луне?", ["Гарриман", "Кармейн", "Нил Армстронг", "Юрий Гагарин"], 2),
            Question("Какой язык является официальным в Китае?", ["Кантонский", "Мандарин", "Шанхайский", "Тайваньский"], 1),
            Question("Кто написал 'Руслан и Людмила'?", ["Тургенев", "Пушкин", "Толстой", "Тихонов"], 1),
            Question("Столица Италии?", ["Рим", "Флоренция", "Милан", "Венеция"], 0),
            Question("Сколько дней в феврале високосного года?", ["28", "29", "30", "31"], 1),
            Question("Какой океан отделяет Америку от Европы?", ["Тихий", "Индийский", "Атлантический", "Северный"], 2),
            Question("Кто написал 'Песнь о Хайавате'?", ["Лонгенус", "Лонгфелло", "Диккенс", "Мелвилл"], 1),
            Question("Какой самый длинный день в году?", ["21 декабря", "21 марта", "22 июня", "23 сентября"], 2),
            Question("Какой химический элемент имеет атомный номер 1?", ["Гелий", "Водород", "Литий", "Кислород"], 1),
            Question("Чем занимается астроном?", ["Изучает Землю", "Изучает высшую математику", "Изучает звезды", "Изучает микробы"], 2),
            Question("Когда началась Вторая мировая война?", ["1935", "1939", "1941", "1945"], 1),
            Question("Какой орган отвечает за дыхание?", ["Сердце", "Легкие", "Печень", "Почки"], 1),
            Question("Какой фрукт является символом Нью-Йорка?", ["Яблоко", "Банан", "Груша", "Апельсин"], 0),
            Question("Сколько континентов на Земле?", ["5", "6", "7", "8"], 2),
            Question("Каковой закон называется закон Архимеда?", ["Гидростатический", "Динамический", "Термодинамический", "Кинетический"], 0),
            Question("Какой газ используется в освещении?", ["Кислород", "Водород", "Гелий", "Неон"], 3),
            Question("Что будет если кофе сделать с молоком?", ["Эспрессо", "Капучино", "Латте", "Американо"], 2),
            Question("Какой нынешний президент США?", ["Трамп", "Обама", "Байден", "Клинтон"], 2),
            Question("Какой элемент с символом Fe?", ["Фтор", "Железо", "Неон", "Фосфор"], 1),
            Question("Какой вид спорта самый популярный в мире?", ["Баскетбол", "Футбол", "Теннис", "Хоккей"], 1),
            Question("Как зовут героя 'Властелина колец'?", ["Гэндальф", "Фродо", "Сэм", "Арагорн"], 1),
            Question("Какой зверь является символом Австралии?", ["Кенгуру", "Утконос", "Коала", "Эму"], 0),
            Question("Какая страна известна своим шоколадом?", ["Франция", "Швейцария", "Бельгия", "Италия"], 2),
            Question("Кто является основателем Facebook?", ["Джек Дорси", "Зукерберг", "Билл Гейтс", "Ларри Пейдж"], 1),
            Question("Какой океан самый глубокий?", ["Атлантический", "Индийский", "Тихий", "Северный"], 2),
            Question("Сколько дней в году?", ["365", "366", "364", "360"], 0),
            Question("Кто был известным физиком-теоретиком?", ["Ньютон", "Галилей", "Эйнштейн", "Кеплер"], 2),
            Question("Какой праздник отмечается 31 декабря?", ["Новый год", "Рождество", "День независимости", "День святого Валентина"], 0),
            Question("Кто был первым президентом США?", ["Джордж Вашингтон", "Авраам Линкольн", "Томас Джефферсон", "Джон Адамс"], 0),
            Question("Какой научный закон объясняет движение тел?", ["Закон Ома", "Закон всемирного тяготения", "Закон Гукка", "Закон сохранения энергии"], 1),
            Question("Кто написал 'Убить пересмешника'?", ["Харпер Ли", "Фрэнсис Скотт", "О'Генри", "Стефан Цвейг"], 0),
            Question("Какой космический объект является центром нашей Солнечной системы?", ["Земля", "Луна", "Солнце", "Марс"], 2),
            Question("Какой фрукт содержит много витамина C?", ["Яблоко", "Банан", "Апельсин", "Клубника"], 2),
            Question("Кто был известным русским поэтом?", ["Пушкин", "Чехов", "Гоголь", "Лермонтов"], 0),
            Question("Какой элемент в таблице Менделеева обозначается буквой O?", ["Кислород", "Золото", "Серебро", "Фтор"], 0),
            Question("В каком году побывала на Луне первая женщина?", ["1969", "1971", "1974", "1976"], 1),
            Question("Как называют ученого, изучающего поведение животных?", ["Биолог", "Этолог", "Зоолог", "Эколог"], 1),
            Question("Как называется процесс превращения водяного пара в жидкость?", ["Конденсация", "Выпаривание", "Сублимация", "Осаждение"], 0),
            Question("Кто был известным режиссером, снявшим 'Титаник'?", ["Стивен Спилберг", "Джеймс Кэмерон", "Джордж Лукас", "Квентин Тарантино"], 1),
            Question("Как называется столица Республики Корея?", ["Сеул", "Пекин", "Токио", "Тайбэй"], 0),
            Question("Какой праздник отмечается 14 февраля?", ["День святого Валентина", "День независимости", "Новый год", "Рождество"], 0),
            Question("Кто является автором 'Каталонских рассказов'?", ["Хорхе Луис Борхес", "Ромуло Гальегос", "Габриэль Гарсия Маркес", "Пабло Неруда"], 1),
            Question("Кто написал 'Собачье сердце'?", ["Михаил Булгаков", "Антон Чехов", "Фёдор Достоевский", "Лев Толстой"], 0),
            Question("Какой химический элемент обозначается буквой Na?", ["Натрий", "Кальций", "Силиций", "Магний"], 0),
            Question("Какой праздник отмечается 7 ноября?", ["День славянской письменности", "День Конституции", "День народного единства", "Октябрьская революция"], 3),
            Question("Кто был известным физиком-экспериментатором?", ["Макс Планк", "Ньютон", "Эйнштейн", "Гейзенберг"], 0),
            Question("Какой цвет обычно ассоциируется со скорбью?", ["Синий", "Чёрный", "Красный", "Зелёный"], 1)
        ]
        self.current_question_index = -1
        self.score = 0
        self.total_questions = 0
        self.used_questions = []
        self.init_ui()

    def init_ui(self):
        self.question_label = QLabel()
        self.radio_group = QGroupBox("Варианты ответов")
        self.radio_buttons = [QRadioButton() for _ in range(4)]
        radio_layout = QVBoxLayout()
        for rb in self.radio_buttons:
            radio_layout.addWidget(rb)
        self.radio_group.setLayout(radio_layout)
        self.answer_button = QPushButton('Ответить')
        self.answer_button.clicked.connect(self.click_ok)
        self.finish_button = QPushButton('Завершить тест')
        self.finish_button.clicked.connect(self.finish_test)
        self.result_label = QLabel()
        self.result_label.hide()
        self.final_result_label = QLabel()
        self.restart_button = QPushButton('Начать заново')
        self.restart_button.clicked.connect(self.restart_test)
        self.final_result_label.hide()
        self.restart_button.hide()
        self.timer_label = QLabel()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_out)
        self.time_left = 30
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.question_label)
        main_layout.addWidget(self.radio_group)
        main_layout.addWidget(self.answer_button)
        main_layout.addWidget(self.finish_button)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.final_result_label)
        main_layout.addWidget(self.restart_button)
        self.setLayout(main_layout)
        self.next_question()

    def next_question(self):
        if len(self.questions) > 0:
            self.current_question_index = random.randint(0, len(self.questions) - 1)
            question = self.questions.pop(self.current_question_index)
            self.used_questions.append(question)
            self.ask(question)
            self.start_timer()
        else:
            self.finish_test()

    def ask(self, question: Question):
        self.question_label.setText(question.question)
        for i in range(len(question.answers)):
            self.radio_buttons[i].setText(question.answers[i])
            self.radio_buttons[i].setChecked(False)
            self.radio_buttons[i].setEnabled(True)
            self.radio_buttons[i].setStyleSheet("")
        self.result_label.hide()
        self.answer_button.setText("Ответить")
        self.total_questions += 1

    def click_ok(self):
        if self.answer_button.text() == "Ответить":
            self.check_answer()
        else:
            self.next_question()

    def check_answer(self):
        selected_answer = None
        for i in range(len(self.radio_buttons)):
            if self.radio_buttons[i].isChecked():
                selected_answer = i
                break

        if selected_answer is None:
            self.result_label.setText("Пожалуйста, выберите ответ.")
            self.result_label.show()
            return

        correct_answer = self.used_questions[-1].correct_answer_index
        if selected_answer == correct_answer:
            self.show_correct("Правильно")
            self.score += 1
        else:
            self.show_correct("Неправильно")

        for i in range(len(self.radio_buttons)):
            if i == correct_answer:
                self.radio_buttons[i].setStyleSheet("color: green;")
            elif i == selected_answer:
                self.radio_buttons[i].setStyleSheet("color: red;")
            else:
                self.radio_buttons[i].setStyleSheet("")

        for rb in self.radio_buttons:
            rb.setEnabled(False)

    def show_correct(self, result):
        self.result_label.setText(result)
        self.result_label.show()
        self.answer_button.setText("Следующий вопрос")
        if self.total_questions >= len(self.used_questions):
            self.finish_button.setEnabled(True)

    def finish_test(self):
        self.timer.stop()
        percentage = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0
        percentage_rounded = round(percentage, 2)
        total_results = "Тест завершен! Верные ответы: " + str(self.score) + \
                      ", Всего вопросов: " + str(self.total_questions) + \
                      ", Рейтинг: " + str(percentage_rounded) + "%."
        self.question_label.hide()
        self.radio_group.hide()
        self.answer_button.hide()
        self.finish_button.hide()
        self.result_label.hide()
        self.final_result_label.setText(total_results)
        self.final_result_label.show()
        self.restart_button.show()
        if self.score >= self.total_questions / 2:
            self.setStyleSheet("background-color: green;")
        else:
            self.setStyleSheet("background-color: red;")

        print(total_results)

    def restart_test(self):
        self.timer.stop()
        self.score = 0
        self.total_questions = 0
        self.setStyleSheet("")
        self.question_label.show()
        self.radio_group.show()
        self.answer_button.show()
        self.finish_button.show()
        self.final_result_label.hide()
        self.restart_button.hide()
        self.questions = self.used_questions.copy()
        self.used_questions = []
        self.next_question()

    def start_timer(self):
        self.time_left = 30
        self.timer_label.setText(f"Осталось времени: {self.time_left} сек.")
        self.timer.start(1000)

    def time_out(self):
        self.time_left -= 1
        self.timer_label.setText(f"Осталось времени: {self.time_left} сек.")
        if self.time_left <= 0:
            self.timer.stop()
            self.show_correct("Время вышло!")
            self.next_question()

if __name__ == '__main__':
    app = QApplication([])
    start_window = StartWindow()
    start_window.show()
    app.exec_()