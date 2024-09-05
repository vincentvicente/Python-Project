## NAME: QIYUAN ZHU
## DATE: 12/06/2023
## EMAIL ID: zhu.qiyu@northeastern.edu
import AppointmentDiary  

class User:
    def __init__(self, username):
        self.username = username
        self.appointment_diary = AppointmentDiary.AppointmentDiary()
