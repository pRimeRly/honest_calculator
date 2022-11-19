msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_list = [msg_10, msg_11, msg_12]
result = 0
response_msg4 = ""
memory = 0
response_msg5 = ""
msg_index: int


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def app():
    global result, response_msg4, memory, response_msg5, msg_index

    def app3():
        print(msg_5)
        global response_msg5
        response_msg5 = input()
        if response_msg5 == "y" or response_msg5 == "Y":
            app()
        elif response_msg5 == "n" or response_msg5 == "N":
            quit()
        else:
            print(msg_5)
            app3()

    def app2():
        global response_msg4, memory, msg_index
        print(msg_4)
        response_msg4 = input()
        if response_msg4 == "y" or response_msg4 == "Y":
            def app4():
                global msg_index, memory
                print(msg_list[msg_index])
                answer = input()
                if answer == "y" or answer == "Y":
                    if msg_index < 2:
                        msg_index += 1
                        app4()
                    else:
                        memory = result
            if is_one_digit(result):
                msg_index = 0
                app4()
            else:
                memory = result
            app3()
        elif response_msg4 == "n" or response_msg4 == "N":
            app3()
        else:
            app2()

    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    if not str(x).isalpha() and not str(y).isalpha():
        if oper == "+" or oper == "-" or oper == "*" or oper == "/":
            check(v1=float(x), v2=float(y), v3=oper)
            if oper == "+":
                result = float(x) + float(y)
                print(result)
            elif oper == "-":
                result = float(x) - float(y)
                print(result)
            elif oper == "*":
                result = float(x) * float(y)
                print(result)
            elif oper == "/":
                if float(y) != 0:
                    result = float(x) / float(y)
                    print(result)
                else:
                    print(msg_3)
                    app()
            app2()

        else:
            print(msg_2)
            app()
    else:
        print(msg_1)
        app()


app()
