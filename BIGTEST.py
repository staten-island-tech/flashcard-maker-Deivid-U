courses = {"Python Programming": {"fee": 150, "seats": 0, "category": "Technology"}, "Machine Learning": {"fee": 200, "seats": 3, "category": "Technology"}, "Business Strategy": {"fee": 100, "seats": 5, "category": "Business"}, "Marketing 101": {"fee": 120, "seats": 2, "category": "Business"}, "Cybersecurity": {"fee": 180, "seats": 4, "category": "Technology"}}

student_enrollment = ["Python Programming", "Business Strategy", "Marketing 101"]
student_fee_raw = 0
scholarship = 0
final_fee = 0

for course in student_enrollment:
    for i, value in courses.items():
        if course == i:
            if value["seats"] == 0:
                rejected_course_alternatives = {}
                for alternative, properties in courses.items():
                    if course != alternative and properties["category"] == value["category"]:
                        rejected_course_alternatives[course] = (value["category"])
            elif value["seats"] > 0:
                if value["category"] == "Technology":
                    scholarship += 20

if len(student_enrollment) >= 3:
    discount = 0.95

print()
    

