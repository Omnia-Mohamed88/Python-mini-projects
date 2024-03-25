import random
import time
operators = ["+","-","*"]
min_operand = 3
max_operand = 12
total_problems = 10
def generate_problem():
    left_operand = random.randint(min_operand,max_operand)
    right_operand = random.randint(min_operand,max_operand)
    operator = random.choice(operators)
    expration = str(left_operand) + " " + operator + " " + str(right_operand)
    answer = eval(expration)
    return expration , answer
wrong =0
input("press enter to start!")
print("-------------------------------")
start_time = time.time()
for i in range(total_problems):
    expr , answer = generate_problem()
    while True :
        guess = input("problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong+=1
end_time = time.time()
total_time = round(end_time - start_time, 2)
print("---------------------------------")
print("nice work! you finshed in ," ,total_time ,"secounds!")