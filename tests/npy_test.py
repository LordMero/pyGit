#!/usr/bin/env python3 

import npyscreen as npy

class pygitF(npy.Form):
    def create(self):
        self.date = self.add(npy.TitleDateCombo, name='Date')


def func(*args):
    F = pygitF(name="pygit")
    F.edit()
    pass

if __name__ == "__main__":
    npy.wrapper_basic(func)
