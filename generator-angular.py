import sublime
import sublime_plugin
import subprocess
import os
import errno
import re
import threading

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise



class AngularCommand(sublime_plugin.WindowCommand):
    """
    This plugin will take a file path for where the folder should be located
    and the folder name
    """
    def run(self):
        user_path = os.path.expanduser("~")
        if len(self.window.folders()) == 0:
            self.window.show_input_panel("Application Name:",user_path+"/",self.on_done, None, None)
        else:
            self.run_yo(self.window.folders()[0])

    def on_done(self, user_input):
        if os.path.isdir(user_input) == False:
            print("Creating dir")
            mkdir_p(user_input)
            os.chmod(user_input, 0777)
        self.run_yo(user_input)

    def run_yo(self, path):
        thread = AngularAppGenerator(path)
        thread.start()
        # print(os.getcwd())


class AngularAppGenerator(threading.Thread):
    def __init__(self, path):
        self.path = path
        threading.Thread.__init__(self)

    def run(self):
        os.chdir(self.path)
        # output = subprocess.Popen(["ls"], stdout=subprocess.PIPE).communicate()[0]
        output = subprocess.Popen(["yo","angular","--minsafe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # response = output.stdout.read()
        print(output.communicate(input="Y\n"))
        # print(output.communicate())
        # output.communicate('Y')
        # print(output.communicate())
        print("thread done")





class ThreadedTaskRunner(threading.Thread):
    def __init__(self, path, cmd):
        self.path = path
        self.cmd = cmd
        threading.Thread.__init__(self)

    def run(self):
        os.chdir(self.path)
        output = subprocess.Popen(self.cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        print(output.communicate()[0])
        print("Angular Task Should Have Run")






class AngularRoute(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Route Name:","", self.on_done, None, None)
    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:route", text, "--minsafe"])
        thread.start()


class AngularController(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Controller Name:","", self.on_done, None, None)
    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:controller", text, "--minsafe"])
        thread.start()


class AngularDirective(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Directive Name:","", self.on_done, None, None)
    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:directive", text, "--minsafe"])
        thread.start()


class AngularFilter(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Filter Name:","", self.on_done, None, None)
    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:filter", text, "--minsafe"])
        thread.start()


class AngularService(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Service Name:","", self.on_done, None, None)
    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:service", text, "--minsafe"])
        thread.start()


class AngularView(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("View Name:","", self.on_done, None, None)
    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:view", text, "--minsafe"])
        thread.start()


