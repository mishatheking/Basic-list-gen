#List generator 

num=int(input("enter number of students :" ))
stu_list={}
no_of_stu=num+1
g=0 #students index in stu_list
for stu_no in range(1,no_of_stu):
    """i can decide to push the input function down to the equation of stu_liat[stu_no]"""
    stu_name=input(f"enter nō {stu_no} student's name :" )
    stu_list[stu_no]=stu_name
    g+=1
for x in stu_list:
    print(f"{x} : {stu_list[x]}")
print(f"This class has a total of {num} students")
