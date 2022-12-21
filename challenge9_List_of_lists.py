"""Define a function, enrollment_stats(), that takes, as an input, a list of
lists where each individual list contains three elements: (a) the name
of a university, (b) the total number of enrolled students, and (c) the
annual tuition fees.

enrollment_stats() should return two lists: the first containing all of
the student enrollment values and the second containing all of the
tuition fees.

Next, define a mean() and a median() function. Both functions should
take a single list as an argument and return the mean and median of
the values in each list.

Using universities, enrollment_stats(), mean(), and median(), calculate
the total number of students, the total tuition, the mean and median
of the number of students, and the mean and median tuition values.
"""

universities = [["California Institute of Technology", 2175, 37704], ["Harvard", 19627, 39849],
                ["Massachusetts Institute of Technology", 10566, 40732], ["Princeton", 7802, 37000],
                ["Rice", 5879, 35551], ["Stanford", 19535, 40569], ["Yale", 11701, 40500]

]

def enrollment_stats(alist):
    list1 = []
    list2 = []
    for i in universities:
        list1.append(i[1])
        list2.append(i[2])
    return list1, list2

students, tuition = (enrollment_stats(universities))



def mean (alist):
    return sum(alist)/len(alist)

def median(alist):
    n = len(alist)
    alist.sort()
    if n % 2 == 0:
        median1 = alist[n//2]
        median2 = alist[n//2 -1]
        median =(median1 + median2)/ 2
    
    else:
        median = alist[n//2]
        return median

print(f"Total students: {sum(students):,}")
print(f"Total tuition: ${sum(tuition):,}")



print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: $ {median(students):,}")


print(f"Tuition mean: $ {mean(tuition):,.2f}")
print(f"Tuition median: $ {median(tuition):,}")
