from List_exercise_1.Essay.ui.EssayMainWindow import Ui_MainWindow


class EssayMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonCountWords.clicked.connect(self.count_words)
        self.pushButtonCountSequences.clicked.connect(self.count_sequences)
        self.pushButtonCountParagraphs.clicked.connect(self.count_paragraphs)
        self.pushButtonCountCom.clicked.connect(self.count_com)
    def count_com(self):
        essay = self.textEditEssay.toPlainText()
        number_com = essay.count('cơm')
        self.lineEditComs.setText(str(number_com))
    def count_paragraphs(self):
        essay = self.textEditEssay.toPlainText()
        print(essay)
        number_paragraphs = essay.count('\n') + 1
        self.lineEditParagraphs.setText(str(number_paragraphs))
    def count_words(self):
        essay = self.textEditEssay.toPlainText()
        list_words = essay.split()
        self.lineEdiWords.setText(str(len(list_words)))
    def count_sequences(self):
        essay = self.textEditEssay.toPlainText()
        list_words = essay.split(".")
        self.lineEditSequences.setText(str(len(list_words)))
    def show(self):
        self.MainWindow.show()
