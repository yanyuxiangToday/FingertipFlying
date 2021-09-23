from _thread import start_new_thread

import rumps
from pynput import keyboard

key_count = 0


class KeyAction:
    def __init__(self):
        self.key_dict = {}

    @property
    def key_count(self):
        global key_count
        key_count = 0
        for _, value in self.key_dict.items():
            key_count += value
        return key_count

    def on_press(self, key):
        pass

    def on_release(self, key):
        global key_count
        key_count += 1
        if key in self.key_dict:
            self.key_dict[key] += 1
        else:
            self.key_dict[key] = 0


class FingertipFlying(rumps.App):
    def __init__(self):
        self.config = {
            'app_name': 'FingertipFlying',
            'about': 'About',
            'about_title': 'About FingertipFlying'
        }
        super(FingertipFlying, self).__init__(self.config['app_name'])
        start_new_thread(self.thread_count, ())
        self.about_button = rumps.MenuItem(title=self.config['about'], callback=self.on_about)
        self.menu = [self.about_button]

    @rumps.timer(1)
    def on_tick(self, sender):
        global key_count
        self.title = 'FingertipFlying: ' + str(key_count)

    def on_about(self, sender):
        rumps.alert(self.config['about_title'],
                    ('Keep typing, create anything you want.\n\n'
                     'Contact YanYuxiang: yanyuxiangtoday@163.com\n'
                     'Contact YangShu: yangshu1109@gmail.com\n'),
                    ok='Thanks!')

    @staticmethod
    def thread_count():
        ka = KeyAction()
        with keyboard.Listener(on_press=ka.on_press, on_release=ka.on_release) as listener:
            listener.join()


if __name__ == '__main__':
    FingertipFlying().run()
