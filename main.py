import argparse

import PySimpleGUI as sg




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
    args = parser.parse_args()
    return args


def main():

    activation_btn_text = {
        False: "Start Input",
        True: "Finish Input"
    }

    args = get_args()

    input_active = False
    window = sg.Window(title='Password Authenticator',
                       layout=[[sg.Text('Input Password: '), sg.Input(None, key='input_field', disabled=not input_active)],
                               [sg.Button(activation_btn_text[input_active], key='activation_button'),
                                sg.Button('Submit password', key='submit_button'), sg.Button('Quit')]],
                       margins=(400, 300))
    while True:
        event, values = window.read(timeout=50)

        if event == "activation_button":
            input_active = not input_active
            window['activation_button'].update(activation_btn_text[input_active])
            window['input_field'].update(disabled=not input_active)

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        window.refresh()

    window.close()

if __name__ == '__main__':
    main()