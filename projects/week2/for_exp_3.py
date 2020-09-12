import random
import string

school = []

def create_school (class_number):
    new_school = []
    used_class_name = set()
    while len(new_school) < class_number:
        class_name = str(random.randint(1, 11)) + random.choice(string.ascii_letters).upper()
        class_scores = []
        class_cnt_people = random.randint(10, 30)
        for j in range(class_cnt_people):
            class_scores.append(random.randint(2, 5))
        new_class = {}
        new_class['school_class'] = class_name
        new_class['scores'] = class_scores
        if class_name not in used_class_name:
            new_school.append(new_class)
            used_class_name.add(class_name) 
    return new_school        


school = list(create_school(20))

school_scores_sum = 0
school_people_cnt = 0
for i in school:
    print(i['school_class'], end=' avg:')
    print(sum(i['scores']) / len(i['scores']))
    school_scores_sum += sum(i['scores'])
    school_people_cnt += len(i['scores'])
print (f'avg school score: {school_scores_sum / school_people_cnt}')