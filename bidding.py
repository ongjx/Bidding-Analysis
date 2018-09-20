import pandas as pd
# from pprint import pprint
df = pd.read_csv('2013-14_T1.csv')

df1 = df[['Term',
         'Session',
         'Course Code',
         'Description',
         'Section',
         'Max Bid',
         'Median Bid',
         'Min Bid',
         'Instructor',
          'School/Department'
        ]]

df1 = df1[df1['Max Bid'] > 0]
df1 = df1.dropna()
school = 'School/Department'

course_code = list(set(df1['Course Code']))
sch = list(set(df1[school]))
d = {}

for course in course_code:
    d[course] = pd.DataFrame(df1[df1['Course Code'] == course])
df_list = list(d)


instructor_list = []
for course in df_list[:]:

    temp = list(set(d[course]['Instructor']))
    for instructor in temp:
        instructor_list.append(instructor)

        # display(d[course].head())


df1[df1['Instructor'] == instructor_list[0]]
bid_price = {}
for instructor in instructor_list:
    a_list = []
    for i in df1[df1['Instructor'] == instructor].mean():
        a_list.append(round(i,3))
        bid_price[instructor] = a_list
    
courses = {}
for course in df_list:
    instruct = {}
    temp = list(set(d[course]['Instructor']))
    for instructor in temp:
        instruct[instructor] = {'Max' : round(df1[df1['Instructor']==instructor].mean()[0],3), 
                                "Median" : round(df1[df1['Instructor']==instructor].mean()[1],3),
                                'Min' : round(df1[df1['Instructor']==instructor].mean()[2],3)
                               }
        courses[course] = instruct
    print(courses[course])

