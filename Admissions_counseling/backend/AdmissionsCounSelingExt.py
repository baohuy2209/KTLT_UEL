from sympy.multipledispatch.utils import reverse_dict
from sympy.physics.units import liter

from Admissions_counseling.model.Student import Student
from Admissions_counseling.ui.AdmissionsCounSelingWindow import Ui_MainWindow



class AdmissionsCounSellingExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlots()
    def setupSignalAndSlots(self):
        self.pushButtonProposal.clicked.connect(self.proposal)

    def reverse_dict(self, my_dict):
        return {value: key for key, value in my_dict.items()}
    def proposal(self):
        fullname = self.lineEditFullname.text()
        address = self.lineEditAddress.text()
        school = self.lineEditSchool.text()
        email = self.lineEditEmail.text()
        phone = self.lineEditPhone.text()
        if self.radioButtonMale.isChecked():
            gender = "male"
        elif self.radioButtonFemale.isChecked():
            gender = "female"
        else:
            gender = None
        math = float(self.lineEditMath.text())
        literature = float(self.lineEditLiterature.text())
        physics = float(self.lineEditPhysics.text())
        chemistry = float(self.lineEditChemistry.text())
        biology = float(self.lineEditBiology.text())
        geography = float(self.lineEditGeography.text())
        english = float(self.lineEditEnglish.text())
        history = float(self.lineEditHistory.text())
        student = Student(fullname, address, school, email, phone, gender, math, literature, physics, chemistry, biology, geography, english, history)
        group_a = math*2 + physics + chemistry
        group_a1 = math*2 + physics + english
        group_b = math*2 + chemistry + biology
        group_c = literature*2 + history + geography
        group_d = literature*2 + math + english
        self.lineEditGroupA.setText(str(group_a))
        self.lineEditGroupB.setText(str(group_b))
        self.lineEditGroupA1.setText(str(group_a1))
        self.lineEditGroupC.setText(str(group_c))
        self.lineEditGroupD.setText(str(group_d))
        my_dictionary = {
            "Group a": group_a,
            "Group a1": group_a1,
            "Group b": group_b,
            "Group c": group_c,
            "Group d": group_d
        }
        max = 0
        for value in my_dictionary.values():
            if value > max:
                max = value
        reversed_dict = self.reverse_dict(my_dictionary)
        best_group = reversed_dict[max]
        proposal_text = f"{student.fullname} has the best score at {best_group} with {max}"
        self.textEditProposal.append(proposal_text)
    def show(self):
        self.MainWindow.show()