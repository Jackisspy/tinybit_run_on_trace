def on_forever():
    basic.show_string("TINN")
basic.forever(on_forever)

def on_forever2():
    Tinybit.RGB_Car_Big(Tinybit.enColor.GREEN)
basic.forever(on_forever2)

def on_forever3():
    if Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        for Speed in range(81):
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, Speed)
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.BLACK) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.WHITE):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 70)
    elif Tinybit.Line_Sensor(Tinybit.enPos.LEFT_STATE, Tinybit.enLineState.WHITE) and Tinybit.Line_Sensor(Tinybit.enPos.RIGHT_STATE, Tinybit.enLineState.BLACK):
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINRIGHT, 70)
    else:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_STOP, 0)
basic.forever(on_forever3)
