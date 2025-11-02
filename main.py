def on_button_pressed_a():
    radio.send_number(1)
    basic.show_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(3)
    basic.show_number(3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(2)
    basic.show_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P14, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P15, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_NONE)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P15) == 0:
        radio.send_number(0)
        basic.show_number(0)
    elif pins.digital_read_pin(DigitalPin.P13) == 0:
        radio.send_number(1)
        basic.show_number(1)
    elif pins.digital_read_pin(DigitalPin.P16) == 0:
        radio.send_number(2)
        basic.show_number(2)
    elif pins.digital_read_pin(DigitalPin.P14) == 0:
        radio.send_number(3)
        basic.show_number(3)
    elif pins.analog_read_pin(AnalogReadWritePin.P2) > 550 and (pins.analog_read_pin(AnalogReadWritePin.P1) > 400 and pins.analog_read_pin(AnalogReadWritePin.P1) < 600):
        radio.send_number(4)
        basic.show_number(4)
    elif pins.analog_read_pin(AnalogReadWritePin.P2) < 450 and (pins.analog_read_pin(AnalogReadWritePin.P1) > 400 and pins.analog_read_pin(AnalogReadWritePin.P1) < 600):
        radio.send_number(5)
        basic.show_number(5)
    elif pins.analog_read_pin(AnalogReadWritePin.P1) < 450 and (pins.analog_read_pin(AnalogReadWritePin.P2) > 400 and pins.analog_read_pin(AnalogReadWritePin.P2) < 600):
        radio.send_number(6)
        basic.show_number(6)
    elif pins.analog_read_pin(AnalogReadWritePin.P1) > 550 and (pins.analog_read_pin(AnalogReadWritePin.P2) > 400 and pins.analog_read_pin(AnalogReadWritePin.P2) < 600):
        radio.send_number(7)
        basic.show_number(7)
    else:
        radio.send_number(8)
        basic.show_number(8)
basic.forever(on_forever)
