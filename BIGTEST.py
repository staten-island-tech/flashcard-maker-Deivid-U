






























courses = {"Python Programming": {"fee": 150, "seats": 0, "category": "Technology"}, "Machine Learning": {"fee": 200, "seats": 3, "category": "Technology"}, "Business Strategy": {"fee": 100, "seats": 5, "category": "Business"}, "Marketing 101": {"fee": 120, "seats": 2, "category": "Business"}, "Cybersecurity": {"fee": 180, "seats": 4, "category": "Technology"}}

student_enrollment = ["Python Programming", "Business Strategy", "Marketing 101"]
student_fee_raw = 0
scholarship = False
discount = False
final_fee = 0
rejected_course_alternatives = {}

for course in student_enrollment:
    for i, value in courses.items():
        if course == i:
            if value["category"] == "Technology":
                    scholarship = True
            if value["seats"] == 0:
                alternatives_list = []
                for alternative, properties in courses.items():
                    if course != alternative and properties["category"] == value["category"]:
                        alternatives_list.append(alternative)
                        rejected_course_alternatives[course] = alternatives_list
            elif value["seats"] > 0:
                student_fee_raw += value["fee"]
                

if len(student_enrollment) >= 3:
    discount = True

for course in rejected_course_alternatives:
    print(f'{course} is unavailable, try {rejected_course_alternatives[course]} instead')

final_fee = student_fee_raw

if discount == True:
    print("applying 5% discount for enrolling in 3 or more courses")
    final_fee *= 0.95

if scholarship == True:
    print("applying 20$ scholarship for enrolling in a technology course")
    final_fee -= 20

print(f"Total enrollment cost before discounts: ${student_fee_raw}")

print(f"Total enrollment cost after discounts: ${final_fee}")
