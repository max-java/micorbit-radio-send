input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
    basic.showNumber(1)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(3)
    basic.showNumber(3)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
    basic.showNumber(2)
})
radio.setGroup(1)
pins.setPull(DigitalPin.P13, PinPullMode.PullNone)
pins.setPull(DigitalPin.P14, PinPullMode.PullNone)
pins.setPull(DigitalPin.P15, PinPullMode.PullNone)
pins.setPull(DigitalPin.P16, PinPullMode.PullNone)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P15) == 0) {
        radio.sendNumber(0)
        basic.showNumber(0)
    } else if (pins.digitalReadPin(DigitalPin.P13) == 0) {
        radio.sendNumber(1)
        basic.showNumber(1)
    } else if (pins.digitalReadPin(DigitalPin.P16) == 0) {
        radio.sendNumber(2)
        basic.showNumber(2)
    } else if (pins.digitalReadPin(DigitalPin.P14) == 0) {
        radio.sendNumber(3)
        basic.showNumber(3)
    } else if (pins.analogReadPin(AnalogReadWritePin.P2) > 550 && (pins.analogReadPin(AnalogReadWritePin.P1) > 400 && pins.analogReadPin(AnalogReadWritePin.P1) < 600)) {
        radio.sendNumber(4)
        basic.showNumber(4)
    } else if (pins.analogReadPin(AnalogReadWritePin.P2) < 450 && (pins.analogReadPin(AnalogReadWritePin.P1) > 400 && pins.analogReadPin(AnalogReadWritePin.P1) < 600)) {
        radio.sendNumber(5)
        basic.showNumber(5)
    } else if (pins.analogReadPin(AnalogReadWritePin.P1) < 450 && (pins.analogReadPin(AnalogReadWritePin.P2) > 400 && pins.analogReadPin(AnalogReadWritePin.P2) < 600)) {
        radio.sendNumber(6)
        basic.showNumber(6)
    } else if (pins.analogReadPin(AnalogReadWritePin.P1) > 550 && (pins.analogReadPin(AnalogReadWritePin.P2) > 400 && pins.analogReadPin(AnalogReadWritePin.P2) < 600)) {
        radio.sendNumber(7)
        basic.showNumber(7)
    } else {
        radio.sendNumber(8)
        basic.showNumber(8)
    }
})
