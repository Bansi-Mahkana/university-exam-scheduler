class Student:
    def __init__(self, student_id, enrolled_exam_ids=None):
        self.student_id = student_id
        if enrolled_exam_ids is None:
            self.enrolled_exam_ids = []
        else:
            self.enrolled_exam_ids = enrolled_exam_ids
