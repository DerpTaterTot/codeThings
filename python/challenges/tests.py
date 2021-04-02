def takeAvg(lst):
    sum = 0
    stringCount = 0
    for a in lst:
        try:
            int(a)
        except:
            stringCount += 1
            continue
        sum += a
    return sum/(len(lst)-stringCount)

def testscores(scores):
    start = []
    final = []
    for a in scores:
        for b in scores[a]:
            start.append(scores[a].get(b))
        final.append(takeAvg(start))
        start.clear()
        print(scores[a]['name'] + ':', final[0])
        print()
        final.clear()

def averageOfTest(scores, subject):
    total = 0
    totalP = 0
    for key in scores:
        if subject in scores[key]:
            total += scores[key][subject]
            totalP += 1

    if totalP == 0:
        return -1
    else:
        return total/totalP

'''
    allScores = []
    for dictionary in scores:
        try:
            allScores.append(scores[dictionary][subject])
        except:
            continue
        
    if len(allScores) == 0:
        return -1
    else:
        return takeAvg(allScores)
'''



def findSubjects(scores):
    values_view = scores.values()
    value_iterator = iter(values_view)
    first_value = next(value_iterator)
    first_key = list(scores.keys())[list(scores.values()).index(first_value)]

    for student in scores:
        for key in scores[student]:
            if key not in scores[first_key]:
                scores[first_key][key] = scores[student][key]

    return scores[first_key]

def findAllSubjects(scores):
    allsub = []
    for student_key in scores:
        for key in scores[student_key]:
            if key == 'name':
                continue 
            if not key in allsub:
                allsub.append(key)
    return allsub

def subjectsAvg(scores):
    listofsubjects = findAllSubjects(scores)
    for key in listofsubjects:
        if key == 'name':
            continue

        avg = averageOfTest(scores, key)
        print(key + ':', avg)

def subjectAvg_once(scores):
    record= {}
    for student_key in scores:
        for key in scores[student_key]:
            if key == 'name':
                continue 
            sc = scores[student_key][key]
            if not key in record:
                record[key]= [sc, 1]
            else:
                record[key][0] += sc
                record[key][1] += 1

    for subj in record:
        print(subj + ':', record[subj][0]/record[subj][1])


'''
            # find the sum of each subject and count, stored to total and count
            for student in scores:
                if key == 'name':
                    total = -1
                    count = 1
                    continue
                if key not in scores[student]:
                    continue
                total += scores[student][key]
                count = count + 1

            if total/count != -1:
                print(key + ':', str(total/count))
            total = 0
            count = 0
            
        exit(0)
'''

def name_and_anverage(dt):
    total=0
    count = 0
    for sub in dt:
        if sub == 'name':
            continue
        total += dt[sub]
        count += 1
    return dt['name'], total/count

def score_report(scores):
    for a in scores:
        name, avg = name_and_anverage(scores[a])
        print(name+' :', avg)
        print()

def score_report2(scores):
    top_avg = -1
    low_avg = 101
    topName = 'NoBody'
    lowName = 'NoBody'
    for a in scores:
        name, avg = name_and_anverage(scores[a])
        if avg > top_avg:
            topName = name
            top_avg = avg
        elif avg < low_avg:
            lowName = name
            low_avg = avg
        else:
            continue
        
    print("The best student,", topName + ", had an average of", str(top_avg))
    print()
    print("The worst student,", lowName + ", had an average of", str(low_avg))

def main():
    score = {'s1': {'name': 'apple', 'math': 95, 'physics': 90, 'history': 85, 'ELA': 92},
         's2': {'name': 'banana', 'math': 91, 'physics': 85, 'history': 93, 'ELA': 93},
         's3': {'name': 'orange', 'math': 85, 'physics': 78, 'history': 83, 'bbq': 68},
         'asd5': {'name': 'danger', 'math': 8, 'physics': 7, 'history': 3.5, 'ELA': 68}
    }

    score_report2(score)
    score_report2({})

if __name__ == "__main__":
    main()
