import sublime
import sublime_plugin
import subprocess
import os
import errno
import threading
import time

# from Queue import Queue, Empty


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


class AngularCommand(sublime_plugin.WindowCommand):
    """
    This plugin will take a file path for where the folder should be located
    and the folder name
    """
    def run(self):
        # sublime.error_message("haha shits broke son")
        user_path = os.path.expanduser("~")
        if len(self.window.folders()) == 0:
            self.window.show_input_panel("Application Name:", user_path+"/", self.on_done, None, None)
        else:
            self.run_yo(self.window.folders()[0])

    def on_done(self, user_input):
        if os.path.isdir(user_input) is False:
            print("Creating dir")
            mkdir_p(user_input)
            os.chmod(user_input, 0777)
        self.run_yo(user_input)

    def run_yo(self, path):
        thread = AngularAppGenerator(path)
        thread.daemon = True
        thread.start()
        # print(os.getcwd())


class AngularAppGenerator(threading.Thread):
    def __init__(self, path):
        self.path = path
        threading.Thread.__init__(self)

    def run(self):
        os.chdir(self.path)
        # output = subprocess.Popen(["ls"], stdout=subprocess.PIPE).communicate()[0]
        output = subprocess.Popen(["yo", "angular", "--minsafe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # response = output.stdout.read()
        print(output.communicate(input="Y\n"))
        """
        Okay heres what needs to happen here
        While the program is running:
            We need to wait on a response from the yo angular command
            Then we need to response accordingly
        """
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
        file_path = self.path + "/app/"
        files = []
        print(self.cmd[1])
        if self.cmd[1] == "angular:route":
            files.append(file_path + "views/{0}.html".format(self.cmd[2]))
            files.append(file_path + "scripts/controllers/{0}.js".format(self.cmd[2]))
        elif self.cmd[1] == "angular:controller":
            files.append(file_path + "scripts/controllers/{0}.js".format(self.cmd[2]))
        elif self.cmd[1] == "angular:service":
            files.append(file_path + "scripts/services/{0}.js".format(self.cmd[2]))
        elif self.cmd[1] == "angular:directive":
            files.append(file_path + "scripts/directives/{0}.js".format(self.cmd[2]))
        elif self.cmd[1] == "angular:filter":
            files.append(file_path + "scripts/filters/{0}.js".format(self.cmd[2]))

        for f in files:
            sublime.windows()[0].open_file(f)
        print("Angular Task Should Have Run")


class AngularRoute(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Route Name:", "", self.on_done, None, None)

    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:route", text, "--minsafe"])
        thread.start()


class AngularController(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Controller Name:", "", self.on_done, None, None)

    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:controller", text, "--minsafe"])
        thread.start()


class AngularDirective(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Directive Name:", "", self.on_done, None, None)

    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:directive", text, "--minsafe"])
        thread.start()


class AngularFilter(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Filter Name:", "", self.on_done, None, None)

    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:filter", text, "--minsafe"])
        thread.start()


class AngularService(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Service Name:", "", self.on_done, None, None)

    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:service", text, "--minsafe"])
        thread.start()


class AngularView(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("View Name:", "", self.on_done, None, None)

    def on_done(self, text):
        thread = ThreadedTaskRunner(self.window.folders()[0], ["yo", "angular:view", text, "--minsafe"])
        thread.start()
