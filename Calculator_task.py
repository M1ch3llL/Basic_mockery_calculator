msg_ = ["Enter an equation\n", 'Do you even know what numbers are? Stay focused!',
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...", "Do you want to store the result? (y / n): ",
        "Do you want to continue calculations? (y / n): ", " ... lazy", " ... very lazy", " ... very, very lazy",
        "You are", "Are you sure? It is only one digit! (y / n): ",
        "Don't be silly! It's just one number! Add to the memory? (y / n): ",
        "Last chance! Do you really want to embarrass yourself? (y / n): "]

memory = 0.0
answer = 0


def is_one_digit(v):
    if (-10 < float(v) < 10 and float(v).is_integer()) is True:
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2) is True:
        msg = msg + msg_[6]
    if (float(v1) == 1.0 or float(v2) == 1.0) and v3 == '*':
        msg = msg + msg_[7]
    if (float(v1) == 0.0 or float(v2) == 0.0) and v3 in ['+', '-', '*']:
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


def really_store(value):
    global memory
    if is_one_digit(value) is True:
        answer_2 = 'a'
        while answer_2 not in ['y', 'n']:
            msg_index = 10
            answer_2 = input(msg_[msg_index])
            while answer_2.lower().strip() == 'y':
                msg_index += 1
                answer_2 = input(msg_[msg_index])
                if msg_index >= 12 and answer_2.strip().lower() == 'y':
                    answer_2 = 'n'
                    memory = value
    else:
        memory = value


while True:
    calc = input(msg_[0]).strip()
    x, oper, y = calc.split()

    try:
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        else:
            float(x) and float(y)
    except ValueError:
        print(msg_[1])
        continue

    if oper in ['+', '-', '*', '/']:
        check(x, y, oper)
        if oper == '+':
            result = float(x) + float(y)
            print(result)
        elif oper == '-':
            result = float(x) - float(y)
            print(result)
        elif oper == '*':
            result = float(x) * float(y)
            print(result)
        elif oper == '/':
            try:
                result = float(x) / float(y)
                print(result)
            except ZeroDivisionError:
                print(msg_[3])
                continue

        while answer not in ['y', 'n']:
            answer = input(msg_[4]).strip().lower()
            if answer == 'y':
                really_store(result)
                answer = 0
                break
            elif answer == 'n':
                answer = 0
                break

        while answer not in ['y', 'n']:
            answer = input(msg_[5]).strip().lower()
            if answer == 'y':
                answer = 0
                break
            elif answer == 'n':
                answer = 0
                exit()

    else:
        print(msg_[2])