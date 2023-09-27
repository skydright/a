#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QButtonGroup, QLabel, QRadioButton, QPushButton, QHBoxLayout, QVBoxLayout
from random import shuffle , randint
def show_result():
    group_box.hide()
    ans_groupbox.show()
    main_btn.setText('Следующий вопрос:')

def show_queetion():
    group_box.show()
    ans_groupbox.hide()
    main_btn.setText('Ответить')
    RadiGroupBox.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadiGroupBox.setExclusive(True)

def start_test():
    if main_btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        main_win.score +=1
        
        show_correct('Правильно!')
        
        
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():    
            show_correct('Неверно!')
    print('Всего вопросов:', main_win.count)
    print('Верные:', main_win.score)
    print('Рейтинг:', main_win.score / main_win.count * 100)

def next_question():
    print('Всего вопросов:', main_win.count)
    print('Верные:', main_win.score)
    main_win.count +=1
    cur_question = randint(0, len(questions_list)-1)
    q1 = questions_list[cur_question]
    ask(q1)


class Question():
    def __init__ (self, question, r_answer, w_answer1, w_answer2, w_answer3):
        self.question = question
        self.r_answer = r_answer
        self.w_answer1 = w_answer1
        self.w_answer2 = w_answer2
        self.w_answer3 = w_answer3

def ask(qt: Question):
    shuffle(answers)
    answers[0].setText(qt.r_answer)
    answers[1].setText(qt.w_answer1)
    answers[2].setText(qt.w_answer2)
    answers[3].setText(qt.w_answer3)
    w.setText(qt.question)
    correct_answer.setText(qt.r_answer)
    show_queetion()


app = QApplication([])
main_win = QWidget()
main_win.count = 1
main_win.score = 0

main_win.setWindowTitle('Memory card')

w = QLabel('Какой национальности не существует?')
group_box = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

answers = [rbtn_1 ,rbtn_2, rbtn_3, rbtn_4]

RadiGroupBox = QButtonGroup()
RadiGroupBox.addButton(rbtn_1)
RadiGroupBox.addButton(rbtn_2)
RadiGroupBox.addButton(rbtn_3)
RadiGroupBox.addButton(rbtn_4)

RadiGroupBox.setExclusive(False)
rbtn_1.setChecked(False)
rbtn_2.setChecked(False)
rbtn_3.setChecked(False)
rbtn_4.setChecked(False)
RadiGroupBox.setExclusive(True)

h_layout1 = QHBoxLayout()
v_layout1 = QVBoxLayout()
v_layout2 = QVBoxLayout()

v_layout1.addWidget(rbtn_1)
v_layout1.addWidget(rbtn_3)

v_layout2.addWidget(rbtn_2)
v_layout2.addWidget(rbtn_4)

h_layout1.addLayout(v_layout1)
h_layout1.addLayout(v_layout2)

group_box.setLayout(h_layout1)


ans_groupbox = QGroupBox('Результат теста')
result = QLabel('Правильно/неправильно')
correct_answer = QLabel('Верный ответ')

res_layout = QVBoxLayout()
res_layout.addWidget( result, alignment=(Qt.AlignLeft | Qt.AlignTop))
res_layout.addWidget(correct_answer, alignment=Qt.AlignHCenter, stretch=2)
ans_groupbox.setLayout(res_layout)

main_btn = QPushButton('Ответить')
main_btn.clicked.connect(start_test)
main_layout = QVBoxLayout()

main_h_layout1 = QHBoxLayout()
main_h_layout2 = QHBoxLayout()
main_h_layout3 = QHBoxLayout()

main_h_layout1.addWidget(w)
main_h_layout2.addWidget(group_box)
main_h_layout2.addWidget(ans_groupbox)


ans_groupbox.hide()


main_h_layout3.addStretch(1)
main_h_layout3.addWidget(main_btn, stretch=2) 
main_h_layout3.addStretch(1)

main_layout.addLayout(main_h_layout1, stretch=2)
main_layout.addLayout(main_h_layout2, stretch=8)
main_layout.addStretch(1)
main_layout.addLayout(main_h_layout3, stretch=1)
main_layout.addStretch(1)
main_layout.setSpacing(5)

main_win.setLayout(main_layout)
questions_list = []
questions_list.append(
    Question('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чулымцы','Алеуты')
)
questions_list.append(
    Question('Как дела?', 'Нормально', 'Пойдёт', 'Плохо', 'Ужасно')
)



main_win.show()
app.exec_()
