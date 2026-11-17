class Exam:
    def __init__(self, exam_id, name, student_count=None, conflicting_exam_ids=None, domain=None):
        self.exam_id = exam_id
        self.name = name

        if student_count is None:
            self.student_count = 0
        else:
            self.student_count = student_count

        if conflicting_exam_ids is None:
            self.conflicting_exam_ids = []
        else:
            self.conflicting_exam_ids = conflicting_exam_ids

        if domain is None:
            self.domain = []
        else:
            self.domain = domain
