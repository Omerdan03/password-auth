from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

import argparse

import PySimpleGUI as sg

ACTIVATION_BTN_TEXT = {False: "Start Input",
                       True: "Finish Input"}

def get_args():
    def str2bool(input_value):
        if input_value.lower() == 'true':
            return True
        elif input_value.lower() == 'false':
            return False
        else:
            raise argparse.ArgumentTypeError('Debug arg must be True or False.')
    parser = argparse.ArgumentParser(
        prog='car_gui',
        formatter_class=argparse.RawTextHelpFormatter,
        description="Runs robotic car GUI.")

    parser.add_argument('-debug', metavar='debug', default=False, type=str2bool,
                        help='option for running the GUI in debug mode. (default=False)')
    parser.add_argument('-file', metavar='file_name', default="keylog.txt", type=str,
                        help='The output file. (default=keylog.txt)')
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    logging.basicConfig(filename=args.file, level=logging.DEBUG,
                        format=" %(asctime)s - %(message)s")

    input_active = False
    start_input = None
    end_input = None
    window = sg.Window(title='Password Authenticator',
                       layout=[[sg.Text('Input Password: '), sg.Input(None, key='input_field', disabled=not input_active)],
                               [sg.Button(ACTIVATION_BTN_TEXT[input_active], key='activation_button'),
                                sg.Button('Submit password', key='submit_button', disabled=input_active), sg.Button('Quit')]],
                       margins=(400, 300))
    while True:
        event, values = window.read(timeout=50)

        if event == "activation_button":
            if input_active:
                end_input = datetime.now()
            else:
                window['input_field'].update('')
                start_input = datetime.now()
            input_active = not input_active

            window['activation_button'].update(ACTIVATION_BTN_TEXT[input_active])
            window['input_field'].update(disabled=not input_active)
            window['submit_button'].update(disabled=input_active)

        if event == "submit_button":
            if not values['input_field']:
                print("No input")
            else:
                print(f"start: {start_input.strftime('%H:%M:%S')}")
                print(f"end: {end_input.strftime('%H:%M:%S')}")
                print(values['input_field'])

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        window.refresh()

    window.close()

if __name__ == '__main__':
    main()