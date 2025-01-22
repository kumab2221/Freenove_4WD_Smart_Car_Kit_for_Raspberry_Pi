
BuzzerOn_flag = False
called_counter = 0
set_counter = 0
BuzzerOut = 0
Pre_Area = -1

def BuzrCtrl(AreaJdg,DrvCtrlSt):
    global BuzzerOn_flag, called_counter, set_counter,Pre_Area
    called_counter += 1

    if AreaJdg != Pre_Area:
        Pre_Area = AreaJdg
        set_counter = called_counter

    if AreaJdg == 3:  # Area1
        if DrvCtrlSt == 0:
            if called_counter - set_counter >= 50:  
                BuzzerOn_flag = False
            else:
                BuzzerOn_flag = True

        else :  
                BuzzerOn_flag = True
                set_counter = called_counter

    elif AreaJdg == 2:  # Area2: ON:0.2sec OFF:0.4sec
        if BuzzerOn_flag:
            if called_counter - set_counter >= 4:  # 0.4
                BuzzerOn_flag = False
                set_counter = called_counter
        else:
            if called_counter - set_counter >= 2:  # 0.2
                BuzzerOn_flag = True
                set_counter = called_counter

    elif AreaJdg == 1:  # Area3: ON:0.2sec OFF:0.8sec
        if BuzzerOn_flag:
            if called_counter - set_counter >= 8:  # 0.8
                BuzzerOn_flag = False
                print("False")
                set_counter = called_counter
            else:
                BuzzerOn_flag = True
        else:
            if called_counter - set_counter >= 2:  # 0.2
                BuzzerOn_flag = True
                print("True")
                set_counter = called_counter
            else:
                BuzzerOn_flag = False

    elif AreaJdg == 0:  # Area4:
        BuzzerOn_flag = False

    if BuzzerOn_flag:
        BuzzerOut = 1
    else:
        BuzzerOut = 0

    return BuzzerOut
