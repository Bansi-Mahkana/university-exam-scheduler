from src.models import Student
from src.models import Exam
from src.models import Room
from src.models import Date
from src.models import TimeSlot
from datetime import date, time


# students
stu_1 = Student("S1", ["E1", "E2"])
stu_2 = Student("S2", ["E1", "E3"])
stu_3 = Student("S3", ["E2"])
stu_4 = Student("S4", ["E3"])

students = [stu_1, stu_2, stu_3, stu_4]

# exams
exam_1 = Exam("E1", "Mathematics")
exam_2 = Exam("E2", "Physics")
exam_3 = Exam("E3", "Chemistry")

exams = [exam_1, exam_2, exam_3]

# rooms
room_1 = Room("R1", 30)
room_2 = Room("R2", 50)

rooms = [room_1, room_2]

# dates
date_1 = Date("D1", date(2026, 12, 1))
date_2 = Date("D2", date(2026, 12, 2))

dates = [date_1, date_2]

# time_slots
slot_1 = TimeSlot("T1", time(8, 0), time(10, 0))
slot_2 = TimeSlot("T2", time(14, 0), time(16, 0))

time_slots = [slot_1, slot_2]

# testing
print("No. of Exams: ", len(exams))
print("No. of Students: ", len(students))
print("No. of Time-slots: ", len(time_slots))
print("No. of Dates: ", len(dates))
print("No. of Rooms: ", len(rooms))