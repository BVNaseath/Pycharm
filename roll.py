from datetime import date
from club import Club

class Roll:
    def __init__(self, members, roll_date):
        self.members = members
        self.date = roll_date

    current_roll = {}

    def create_roll(self, members, x, current_roll):
        for member in members:
            if x == "y":
                current_roll[member] = "Present"
            else:
                current_roll[member] = "Absent"

    def present_list(self, current_roll, members):
        present_people = []
        for key in current_roll:
            if current_roll[key] == "Present":
                present_people.append(current_roll[key])

    def absent_list(self, current_roll, members):
        absent_people = []
        for key in current_roll:
            if current_roll[key] == "Absent":
                absent_people.append((current_roll[key]))
