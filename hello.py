print('Hello,sparta')
a = 3
print(a)
b=a
print(b)
a=a+1
print(a)
print(b)
num = a*b
print(num)

name='유현다'
print(name)
number='72'
print(number)
print(number + str(a))
print(int(number)+a)
is_true = True
print(is_true)

a_list=[]
a_list.append(1)
a_list.append([2,3])
print(a_list)

a_dict= {'name':'유현다', 'age':22}
print(a_dict)
a_dict['level']=1
print(a_dict)

b_list=[]
b_list.append({'name':'유현다','age':22})
print(b_list)
b_list.append(1)
print(b_list)
b_list.append({'level':1})
print(b_list)
#b_list=None
if b_list is not None:
    print(b_list)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

#result=is_even(20)
#print(result)
print(is_even(15))

def is_adult(age):
    if age>20:
        print("진짜 성인입니다.")
    elif age == 20:
        print("갓 스물입니다")
    else:
        print("아직 성인은 아닙니다.")

is_adult(22)
is_adult(20)
is_adult(16)

def check_age(age):
    if age >120:
        print("와우")
    elif age >80:
        print("곧 한 세기를 사실 거예요")
    else:
        print("80까지 화이팅")

check_age(123)
check_age(92)
check_age(17)

fruits=['apple','pear','strawberry','banana']
for fruit in fruits: #fruit은 임의로 지어준 이름
    print(fruit)    #하나씩 꺼내어 출력

fruits=['apple','pear','strawberry','banana','pear','strawberry','banana','apple','apple']
def count_fruits(name):
    count = 0
    for fruit in fruits:
        if fruit == name:
            count +=1
    return count

pear_count = count_fruits('pear')
print(pear_count)

apple_count = count_fruits('apple')
print(apple_count)


#harry_potter =[{'wizard':'Harry','age':12},{'wizard':'Dumbledore','age':65},{'wizard':'McGonagall','age':72}]
#def calculate_age(name,harry_potter):
    #for wizard in wizards:
        #if wizard['name'] == name:
            #return wizard['age']
    #return "Name does not exist"

#print(calculate_age('Harry'),harry_potter)




