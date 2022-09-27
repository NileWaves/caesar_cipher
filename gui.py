from msilib.schema import Icon
import PySimpleGUI as sg
from caesar_cipher import *

sg.theme("LightBrown2")

layout = [
    [
        sg.Sizer(240, 2),
        sg.Text("Rotate by"),
        sg.Input(key="SHIFT", size=(2, 1)),
        sg.Text("letter(s)"),
        sg.Sizer(400, 2),
        sg.Text("Counter-rotate by"),
        sg.Input(key="REVERSE", size=(2, 1)),
        sg.Text("letter(s)"),
    ],
    [
        sg.Text("Plaintext:  "),
        sg.Multiline("Enter plaintext to encrypt...", key="-INPUT-", size=(70, 20)),
        sg.Text("Ciphertext:  "),
        sg.Multiline("Enter ciphertext to decrypt...", key="-INPUT2-", size=(70, 20)),
    ],
    [sg.Sizer(290, 2), sg.Ok("Encrypt"), sg.Sizer(540, 2), sg.Ok("Decrypt")],
    [
        sg.Text("Ciphertext: "),
        sg.Output(key="-OUTPUT-", size=(70, 20)),
        sg.Text("Plaintext:  "),
        sg.Output(key="-OUTPUT2-", size=(70, 20)),
    ],
]

window = sg.Window(
    "Caesar Cipher",
    layout,
    grab_anywhere=True,
    size=(1280, 720),
    icon="caesar_cipher.ico",
)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Encrypt":
        # Before a user types in the input boxes
        # values["SHIFT"] == NONE, which cannot be typecast
        try:
            shift1 = int(values["SHIFT"])
        except ValueError:
            shift1 = 0

        plaintext = values["-INPUT-"]
        ciphertext = encrypt(shift1, plaintext)
        window["-OUTPUT-"].update(value=ciphertext)

    if event == "Decrypt":
        try:
            shift2 = int(values["REVERSE"])
        except ValueError:
            shift2 = 0
        ciphertext = values["-INPUT2-"]
        plaintext = decrypt(shift2, ciphertext)
        window["-OUTPUT2-"].update(value=plaintext)

window.close()
