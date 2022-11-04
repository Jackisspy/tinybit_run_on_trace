basic.forever(function () {
    basic.showString("TINN")
})
basic.forever(function () {
    Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
})
basic.forever(function () {
    if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.White) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.White)) {
        for (let Speed = 0; Speed <= 80; Speed++) {
            Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, Speed)
        }
    } else if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.Black) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.White)) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinLeft, 70)
    } else if (Tinybit.Line_Sensor(Tinybit.enPos.LeftState, Tinybit.enLineState.White) && Tinybit.Line_Sensor(Tinybit.enPos.RightState, Tinybit.enLineState.Black)) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinRight, 70)
    } else {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Stop, 0)
    }
})
