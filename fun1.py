'''
def add_number():
    c = 0
    for number in range(1, 100 + 1):
        print(number)
        c = c + number
    return c
answer = add_number()
print(answer)
'''
def add_numbers(start, end):
    start = int(input("Choose a starting number"))
    end = int(input("Choose an end point"))
    while(type(start) != int or type(end) != int):
        print("Please try again")
        add_numbers(start , end)
    ls_num = list(range(start,end+1))
    str_sum = sum(ls_num)
    return str_sum
test1 = add_numbers(1,2)
print(test1)
