## NAME: QIYUAN ZHU
## DATE: 12/06/2023
## EMAIL ID: zhu.qiyu@northeastern.edu
from datetime import datetime

# Define the Appointment class
class Appointment:
    """Represents an appointment with date, start and end time, and purpose."""

    def __init__(self, date, start_time, end_time, purpose):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.purpose = purpose
