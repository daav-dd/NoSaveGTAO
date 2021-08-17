import os
from pynput import keyboard


def on_activate_f9():
    os.popen('netsh advfirewall firewall add rule name="gta5nosave" dir=out action=block remoteip="192.81.241.171"')

def on_activate_f10():
    os.popen('netsh advfirewall firewall delete rule name="gta5nosave"')

def on_activate_f11():
    os.popen('''
    set PROGRAM=path\to\executable
    netsh advfirewall firewall add rule name="gta5netcut" dir=in action=block profile=any program="%PROGRAM%"
    netsh advfirewall firewall add rule name="gta5netcut" dir=out action=block profile=any program="%PROGRAM%"
    ''')

def on_activate_f12():
    os.popen('netsh advfirewall firewall delete rule name="gta5netcut"')
    
hotkeys = keyboard.GlobalHotKeys({
        '<ctrl>+<f9>': on_activate_f9,
        '<ctrl>+<f10>': on_activate_f10,
        '<ctrl>+<f11>': on_activate_f11,
        '<ctrl>+<f12>': on_activate_f12,})

hotkeys.start()
