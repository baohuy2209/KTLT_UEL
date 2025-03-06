import random

from PyQt6.QtWidgets import QMessageBox

from exam.Bai2.ui.RewardWindow import Ui_MainWindow


class RewardWindowExt(Ui_MainWindow):
    def __init__(self):
        self.list_employee = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonCreateLottery.clicked.connect(self.create_lottery)
        self.pushButtonReward.clicked.connect(self.reward)
    def reward(self):
        first_prize = int(self.lineEditFirstPrize.text())
        second_prize_1 = int(self.lineEditSecondPrize_1.text())
        second_prize_2 = int(self.lineEditSecondPrize_2.text())
        second_prizes = [second_prize_1, second_prize_2]
        third_prize_1 = int(self.lineEditThirdPrize_1.text())
        third_prize_2 = int(self.lineEditThirdPrize_2.text())
        third_prize_3 = int(self.lineEditThirdPrize_3.text())
        third_prizes = [third_prize_1, third_prize_2, third_prize_3]
        fourth_prize_1 = int(self.lineEditFourthPrize_1.text())
        fourth_prize_2 = int(self.lineEditFourthPrize_2.text())
        fourth_prize_3 = int(self.lineEditFourthPrize_3.text())
        fourth_prize_4 = int(self.lineEditFourthPrize_4.text())
        fourth_prizes = [fourth_prize_1, fourth_prize_2, fourth_prize_3, fourth_prize_4]
        my_dict = {
            1: [],
            2: [],
            3: [],
            4: []
        }
        temp_flag = [False, False, False, False]
        for emp in self.list_employee:
            if emp.lottery == first_prize and temp_flag[0] == False:
                my_dict[1].append(emp.name)
                temp_flag[1] = True
            for se_prize in second_prizes:
                if se_prize == emp.lottery and len(my_dict[2]) <= 2 and temp_flag[1] == False:
                    my_dict[2].append(emp.name)
                if len(my_dict[2]) == 2:
                    temp_flag[1] = True
            for th_prize in third_prizes:
                if th_prize == emp.lottery and len(my_dict[3]) <= 3 and temp_flag[2] == False:
                    my_dict[3].append(emp.name)
                if len(my_dict[3]) == 3:
                    temp_flag[2] = True
            for fo_prize in fourth_prizes:
                if fo_prize == emp.lottery and len(my_dict[4]) <= 4 and temp_flag[3] == False:
                    my_dict[4].append(emp.name)
                if len(my_dict[4]) == 4:
                    temp_flag[3] = True
        if len(my_dict[1]) == 0:
            first_emp = ""
        else:
            first_emp = my_dict[1][0]
        second_emps = ""
        for i in range(len(my_dict[2])):
            second_emps += my_dict[2][i] + " "
        third_emps = ""
        for i in range(len(my_dict[3])):
            third_emps += my_dict[3][i] + " "
        fourth_emps = ""
        for i in range(len(my_dict[4])):
            fourth_emps += my_dict[4][i] + " "

        result = f"First Prize: {first_emp} \n Second Prizes: {second_emps} \n Third Prizes: {third_emps} \n Fourth Prizes: {fourth_emps}"
        msg = QMessageBox()
        msg.setText(f"{result}")
        msg.setWindowTitle("Announcement")
        msg.exec()
    def create_lottery(self):
        numbers = random.sample(range(1, 100), 10)
        self.lineEditFirstPrize.setText(str(numbers[0]))
        self.lineEditSecondPrize_1.setText(str(numbers[1]))
        self.lineEditSecondPrize_2.setText(str(numbers[2]))
        self.lineEditThirdPrize_1.setText(str(numbers[3]))
        self.lineEditThirdPrize_2.setText(str(numbers[4]))
        self.lineEditThirdPrize_3.setText(str(numbers[5]))
        self.lineEditFourthPrize_1.setText(str(numbers[6]))
        self.lineEditFourthPrize_2.setText(str(numbers[7]))
        self.lineEditFourthPrize_3.setText(str(numbers[8]))
        self.lineEditFourthPrize_4.setText(str(numbers[9]))
    def show(self):
        self.MainWindow.show()