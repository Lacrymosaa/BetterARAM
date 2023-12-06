import sys
import emoji
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QSpacerItem, QSizePolicy
from BetterRandom import CharacterGetter


class CharacterGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.character_getter = CharacterGetter()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        teams_layout = QHBoxLayout()

        for team, border_color in [('Left', 'blue'), ('Right', 'red')]:
            team_layout = QVBoxLayout()

            for role in ['Tank', 'Fighter', 'Mage', 'Carry', 'Support']:
                role_layout = QHBoxLayout()

                label = QLabel(role + ":")
                label.setFixedSize(40, 20)
                role_layout.addWidget(label)

                text_box = QLineEdit()
                text_box.setReadOnly(True)
                text_box.setStyleSheet(f"border: 1px solid {border_color}; height: 25px")
                role_layout.addWidget(text_box)

                button = QPushButton(emoji.emojize(':game_die:'))
                button.clicked.connect(lambda _, r=role, t=team, tb=text_box: self.sort_character(r, t, tb))
                button_style = "background-color: transparent; border: 3px groove lightgray; padding: 2px;"
                button.setStyleSheet(button_style)
                button.pressed.connect(lambda b=button: self.darken_button(b))
                button.released.connect(lambda b=button: self.restore_button(b))
                role_layout.addWidget(button)

                team_layout.addLayout(role_layout)

            teams_layout.addLayout(team_layout)

            if team == 'Left':
                spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                teams_layout.addItem(spacer_item)

        start_button = QPushButton('Iniciar')
        start_button.clicked.connect(self.start_all)
        start_button.setStyleSheet("background-color: transparent; border: 3px groove lightgray; padding: 5px; width: 60px;")
        start_button.pressed.connect(lambda b=start_button: self.darken_button(b))
        start_button.released.connect(lambda b=start_button: self.restore_button(b))
        layout.addLayout(teams_layout)
        layout.addWidget(start_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Better Random All Mid')
        self.setWindowIcon(QIcon('aram.png'))
        self.show()

    def sort_character(self, role, team, text_box):
        character = self.character_getter.get_character(role)
        text_box.setText(character)

    def start_all(self):
        for widget in self.findChildren(QPushButton):
            if widget.text() == emoji.emojize(':game_die:'):
                widget.click()
    
    def darken_button(self, button):
        if button.text() == 'Iniciar':
            button.setStyleSheet("background-color: lightgray; border: 3px groove lightgray; padding: 5px; width: 60px;")
        else:
            button.setStyleSheet("background-color: lightgray; border: 3px groove lightgray; padding: 2px;")

    def restore_button(self, button):
        if button.text() == 'Iniciar':
            button.setStyleSheet("background-color: transparent; border: 3px groove lightgray; padding: 5px; width: 60px;")
        else:
            button.setStyleSheet("background-color: transparent; border: 3px groove lightgray; padding: 2px;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CharacterGUI()
    sys.exit(app.exec_())
