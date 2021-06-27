#! /usr/bin/env python3

import npyscreen

# This is a form object
class WizardFormMain(npyscreen.ActionForm, npyscreen.SplitForm, npyscreen.FormWithMenus):
  def create(self):

    self.button = self.add(npyscreen.Button, name="Button") # Make this button go to FORM2
 
    # Since we are inheriting the npyscreen.FormWithMenus class we can use menus, this will add an option to the menu to exit the program
    self.menu = self.new_menu(name="Main Menu", shortcut='^M')
    self.menu.addItem("Exit Program", self.exit, "^X")
  # END DEF
    
  def exit(self):
    self.parentApp.switchForm(None) # causes the app to exit on OK
  # END DEF

  # Save data to conf file and Go back to first form...
  def on_ok(self):
    npyscreen.notify_confirm("OK Pressed, going to FORM2 now.", title="Notice", wrap=True, wide=True, editw=1)
    self.parentApp.setNextForm('FORM2')
  # END DEF

  def on_cancel(self):
    self.parentApp.setNextForm(None) # Also exit's the program
  # END DEF

# END CLASS

# FORM2
class WizardForm2(npyscreen.ActionForm, npyscreen.SplitForm, npyscreen.FormWithMenus):
  def create(self):

    self.name = self.add( npyscreen.TitleText, name="Username: " )
    self.passwd = self.add( npyscreen.TitleText, name="Password: " )

  # Save data to conf file and Go back to first form...
  def on_ok(self):
    npyscreen.notify_confirm("Saved! Going back to main form", title="OK Presed", wrap=True, wide=True, editw=1)
    self.parentApp.setNextForm('MAIN')
  # END DEF

  def on_cancel(self):
    npyscreen.notify_confirm("NOT Saved, going back to main form", title="OK Presed", wrap=True, wide=True, editw=1)
    self.parentApp.setNextForm('MAIN') # Back to main form
  # END DEF
# END CLASS

# This is the Wizards form manager function
class WizardApp(npyscreen.NPSAppManaged):
  def onStart(self):
    self.addForm('MAIN', WizardFormMain, name = "First Form!", lines=20, columns=60, draw_line_at=16 )
    self.addForm('FORM2', WizardForm2, name = "Second Form!", lines=20, columns=60, draw_line_at=16 )
  # END DEF
# END CLASS


if ( __name__ == "__main__"):
  wizard = WizardApp().run()
