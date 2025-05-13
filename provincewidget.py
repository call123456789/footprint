from PyQt5.QtWidgets import QWidget, QPushButton
from citybutton import CityButton

class ProvinceWidget(QWidget):
    def __init__(self, parent=None, provincename="", pre=None):
        super().__init__(parent)
        self.resize(1200, 686)
        self.cities = [] 
        self.provincename = provincename
        self.pre = pre

        # 添加右侧按钮组（竖排）
        button_width = 150
        button_height = 50
        spacing = 20
        x = 1200 - button_width - 20  # 右侧边距20px

        # 返回按钮
        self.btn_return = QPushButton("返回", self)
        self.btn_return.setFixedSize(button_width, button_height)        
        self.btn_return.clicked.connect(self.onReturnClicked)
        self.btn_return.move(x, 10)

        # 随机去哪儿按钮
        self.btn_random = QPushButton("随机去哪儿", self)
        self.btn_random.setFixedSize(button_width, button_height)
        self.btn_random.clicked.connect(self.onRandomClicked)
        self.btn_random.move(x, 10 + button_height + spacing)

        # 知识问答按钮
        self.btn_quiz = QPushButton("知识问答", self)
        self.btn_quiz.setFixedSize(button_width, button_height) 
        self.btn_quiz.clicked.connect(self.onQuizClicked)
        self.btn_quiz.move(x, 10 + 2*(button_height + spacing))

        # 加载城市按钮逻辑
        with open(f"resources/{provincename}.txt", 'r', encoding='utf-8') as file:
            content = file.read()
        city_list = content.split()
        for item in city_list:
            button = CityButton(self, f"{provincename}{item}")
            self.cities.append(button)
            button.show()

    # 保留原有返回逻辑
    def onReturnClicked(self):
        self.hide()
        if self.pre:
            self.pre.show()

    # 随机去哪儿功能（示例占位）
    def onRandomClicked(self):
        print("随机去哪儿")

    # 知识问答功能（示例占位）
    def onQuizClicked(self):
        print("知识问答")