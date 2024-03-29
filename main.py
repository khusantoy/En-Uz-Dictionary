import os.path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget
)

from core import Core

class MainButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(300, 80)
        self.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: Arial;
                font-weight: bold;
                color: #fff;
                background-color: #113946;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #335566;
            } 
        """)

class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedHeight(50)
        self.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: Arial;
                font-weight: bold;
                color: #fff;
                background-color: #113946;
                border-radius: 10px;
            }           
            QPushButton:hover {
                background-color: #335566;
            }
        """)

class Input(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(50)
        self.setStyleSheet("""
            font-size: 20px;
            font-family: Arial;
            font-weight: bold;
            border: 2px solid #000;
            border-radius: 10px;
        """)

class WelcomeWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Welcome")
        self.setFixedSize(500, 700)
        self.setStyleSheet("""
            background-color: #FFF2D8;
        """)

        self.h_box = QHBoxLayout()
        self.v_box = QVBoxLayout()

        self.add_btn = MainButton("Add New Word")
        self.list_btn = MainButton("List Of Words")
        self.search_btn = MainButton("Search Word")
        self.exit_btn = MainButton("Exit")

        self.v_box.addStretch()
        self.v_box.addWidget(self.add_btn)
        self.v_box.addWidget(self.list_btn)
        self.v_box.addWidget(self.search_btn)
        self.v_box.addWidget(self.exit_btn)
        self.v_box.addStretch()

        self.h_box.addLayout(self.v_box)

        self.setLayout(self.h_box)

        self.add_btn.clicked.connect(self.add_win)
        self.list_btn.clicked.connect(self.list_win)
        self.search_btn.clicked.connect(self.search_win)
        self.exit_btn.clicked.connect(self.exit)

        self.show()

    def add_win(self):
        self.close()
        self.win = AddWindow()

    def list_win(self):
        self.close()
        self.win = WordsWindow()

    def search_win(self):
        self.close()
        self.win = SearchWindow()

    def exit(self):
        self.close()

class AddWindow(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.core = Core()
        self.setWindowTitle("Add new words")
        self.setFixedSize(500, 700)
        self.setStyleSheet("""
            background-color: #FFF2D8;
        """)

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()

        self.v_box = QVBoxLayout()

        self.en_input = Input()
        self.en_input.setPlaceholderText("English")
        self.uz_input = Input()
        self.uz_input.setPlaceholderText("Uzbek")
        self.add_btn = Button("Add")
        self.menu_btn = Button("Menu")
        self.list_btn = Button("List of words")
        self.search_btn = Button("Search")

        self.h_box1.addWidget(self.en_input)
        self.h_box2.addWidget(self.uz_input)
        self.h_box3.addWidget(self.add_btn)
        self.h_box4.addWidget(self.menu_btn)
        self.h_box4.addWidget(self.list_btn)
        self.h_box4.addWidget(self.search_btn)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addStretch()

        self.v_box.addLayout(self.h_box4)

        self.setLayout(self.v_box)

        self.show()

        self.menu_btn.clicked.connect(self.menu)
        self.list_btn.clicked.connect(self.words)
        self.search_btn.clicked.connect(self.search)

        self.add_btn.clicked.connect(self.add_word)

    def add_word(self):
        uz = self.uz_input.text().lower()
        en = self.en_input.text().lower()

        if uz and en:
            self.core.write_data({"en": en, "uz":uz})
            self.uz_input.clear()
            self.en_input.clear()

    def menu(self):
        self.close()
        self.win = WelcomeWindow()

    def words(self):
        self.close()
        self.win = WordsWindow()

    def search(self):
        self.close()
        self.win = SearchWindow()

class WordsWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.core = Core()            
        self.setWindowTitle("List of words")
        self.setFixedSize(500, 700)
        self.setStyleSheet("""
            background-color: #FFF2D8;
        """)

        self.english = QLabel(self)
        self.english.setText("English")
        self.english.setStyleSheet("""
            font-size: 24px;
            font-family: Arial;
            font-weight: bold;
        """)
        self.uzbek = QLabel(self)
        self.uzbek.setText("Uzbek")
        self.uzbek.setStyleSheet("""
            font-size: 24px;
            font-family: Arial;
            font-weight: bold;
        """)

        self.en_list = QListWidget(self)
        self.en_list.setStyleSheet("""
            font-size: 18px;
            font-family: Arial;
            background-color: #EAD7BB;
            border: 2px solid #113946;
        """)
        self.uz_list = QListWidget(self)
        self.uz_list.setStyleSheet("""
            font-size: 18px;
            font-family: Arial;
            background-color: #EAD7BB;
            border: 2px solid #113946;
        """)

        # self.file = open("words.txt", "r")
        # self.words = self.file.readlines()
        # self.count = 1
        # for word in self.words:
        #     word = word[:-1]
        #     word = word.split(' ')
        #     self.en_list.addItem(f'{self.count}.{word[0]}')
        #     self.uz_list.addItem(f'{self.count}.{word[1]}')
        #     self.count +=1 

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()

        self.v_box = QVBoxLayout()

        self.h_box1.addWidget(self.english)
        self.h_box1.addWidget(self.uzbek)

        self.h_box2.addWidget(self.en_list) 
        self.h_box2.addWidget(self.uz_list)

        self.delete_btn = QPushButton(self)
        self.delete_btn.setText("Delete")
        self.delete_btn.setFixedHeight(50)
        self.delete_btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: Arial;
                font-weight: bold;
                color: #fff;
                background-color: #DC3545;
                border-radius: 10px;
            }           
            QPushButton:hover {
                background-color: #EC586F;
            }
        """)
        

        self.menu_btn = Button("Menu")
        self.add_btn = Button("Add New Word")
        self.search_btn = Button("Search")
        
        self.h_box3.addWidget(self.menu_btn)
        self.h_box3.addWidget(self.add_btn)
        self.h_box3.addWidget(self.search_btn)
        self.h_box4.addWidget(self.delete_btn)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box3)

        self.setLayout(self.v_box)

        self.scroll_bar1 = self.en_list.verticalScrollBar()
        self.scroll_bar2 = self.uz_list.verticalScrollBar()

        self.scroll_bar1.valueChanged.connect(self.scrollBarValueChanged1)
        self.scroll_bar2.valueChanged.connect(self.scrollBarValueChanged2)

        self.show()
        self.show_all_words()

        self.menu_btn.clicked.connect(self.menu)
        self.add_btn.clicked.connect(self.add)
        self.search_btn.clicked.connect(self.search)
        self.delete_btn.clicked.connect(self.delete_word)

    def delete_word(self):
        def is_file_empty(file_path):
            return os.path.getsize(file_path) == 0

        file_path = 'words.txt'

        if is_file_empty(file_path):
            print("Deletion error")
        else:
            self.index = self.en_list.currentRow()
            with open('words.txt', 'r') as f:
                lines = f.readlines()
                lines.pop(self.index)

            with open('words.txt', 'w') as f:
                f.writelines(lines)
            self.close()
            self.win = WordsWindow()

    def menu(self):
        self.close()
        self.win = WelcomeWindow()

    def add(self):
        self.close()
        self.win = AddWindow()

    def search(self):
        self.close()
        self.win = SearchWindow()

    def scrollBarValueChanged1(self, value):
        self.scroll_bar2 = self.uz_list.verticalScrollBar()
        self.scroll_bar2.setValue(value)

    def scrollBarValueChanged2(self, value):
        self.scroll_bar1 = self.en_list.verticalScrollBar()
        self.scroll_bar1.setValue(value)

    def show_all_words(self):
        words = self.core.get_all_words()
        for word in words:
            en = word.get('en').capitalize()
            uz = word.get('uz').capitalize()
            self.en_list.addItem(en)
            self.uz_list.addItem(uz)

class SearchWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.core = Core()
        self.setWindowTitle("Search words")
        self.setFixedSize(500, 700)
        self.setStyleSheet("""
            background-color: #FFF2D8;
        """)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Search Dictionary")
        self.input.setFixedSize(350, 50)
        self.input.setStyleSheet("""
            font-size: 20px;
            font-family: Arial;
            font-weight: bold;
            border: 2px solid #000;
            border-radius: 10px;
        """)
        self.search_btn = Button("Search")
        self.result = QListWidget(self)
        self.result.setStyleSheet("""
            font-size: 18px;
            font-family: Arial;
            background-color: #EAD7BB;
            border-radius: 10px;
            border: 2px solid #113946;
        """)

        self.menu_btn = Button("Menu")
        self.add_btn = Button("Add new word")
        self.list_btn = Button("List of words")

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()

        self.v_box = QVBoxLayout()
        
        self.h_box1.addWidget(self.input)
        self.h_box1.addWidget(self.search_btn)
        self.h_box2.addWidget(self.result)
        
        self.h_box3.addWidget(self.menu_btn)
        self.h_box3.addWidget(self.add_btn)
        self.h_box3.addWidget(self.list_btn)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)

        self.setLayout(self.v_box)

        self.show()

        self.menu_btn.clicked.connect(self.menu)
        self.add_btn.clicked.connect(self.add)
        self.list_btn.clicked.connect(self.words)
        self.search_btn.clicked.connect(self.search)

    def menu(self):
        self.close()
        self.win = WelcomeWindow()

    def add(self):
        self.close()
        self.win = AddWindow()

    def words(self):
        self.close()
        self.win = WordsWindow()

    def search(self):
        search_word = self.input.text().lower()
        print(search_word)
        self.__clear()
        if search_word:
            words = self.core.get_word(search_word)
            if words == 0:
                self.result.addItem("Topilmadi")
            else:
                en, uz = words
                self.result.addItem(f"{en} {uz}")

    def __clear(self):
        self.input.clear()
        self.result.clear()

app = QApplication([])
welcome = WelcomeWindow()
# add = AddWindow()
# words = WordsWindow()
# search = SearchWindow()
app.exec_()