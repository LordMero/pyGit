#!/usr/bin/env python3 

import npyscreen as npy
import pygit 


class MainForm(npy.Form):
    def afterEditing(self):
        #when we press ok in the form this method is called and the focus 
        #for the next form is set to none, i.e. it quits.
        self.parentApp.setNextForm(None)

    def create(self):
        #self.date = self.add(npy.TitleDateCombo, name="Date")
        self.main = self.add(npy.SelectOne, max_height=4, value=[0,], values=["Make new Repository", "Delete Repository", "Clone Repository"])
        print(self.main.get_selected_objects())


class pygitf(npy.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name = "TEST")
    pass 



if __name__ == "__main__":
    app = pygitf()
    app.run()








