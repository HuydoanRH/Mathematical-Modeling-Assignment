from tkinter import *
import tkinter.messagebox
import threading
import random
import time
from pyvis.network import Network
from PetriNet import PetriNet

class qs1a(PetriNet):
    def createWidgets(self):
        #tao canvas ve doi tuong
        self.canvas = Canvas(self.master, bg="white", height="350")
        self.canvas.pack()
        self.canvas.grid(row=0, column=0, columnspan=6, sticky=W + E + N + S, padx=3, pady=3)

        # ve so do trong cau 1#
        # ve Place
        self.canvas.create_oval(70, 50, 140, 120)  # FREE
        self.canvas.create_oval(210, 190, 280, 260)  # BUSY
        self.canvas.create_oval(350, 50, 420, 120)  # DOCU

        widget = Label(self.canvas, text='FREE', bg="white")
        widget.pack()
        self.canvas.create_window(105, 35, window=widget)

        self.label_free = Label(self.canvas, text="0", bg="white")
        self.label_free.pack()
        self.canvas.create_window(105, 85, window=self.label_free)

        widget = Label(self.canvas, text='BUSY', bg="white")
        widget.pack()
        self.canvas.create_window(245, 275, window=widget)

        self.label_busy = Label(self.canvas, text="0", bg="white")
        self.label_busy.pack()
        self.canvas.create_window(245, 225, window=self.label_busy)

        widget = Label(self.canvas, text='DOCU', bg="white")
        widget.pack()
        self.canvas.create_window(385, 35, window=widget)

        self.label_docu = Label(self.canvas, text="0", bg="white")
        self.label_docu.pack()
        self.canvas.create_window(385, 85, window=self.label_docu)
        # ve Transition
        self.canvas.create_rectangle(70, 190, 140, 260, tag="start")  # START
        self.canvas.create_rectangle(210, 50, 280, 120, tag="end")  # END
        self.canvas.create_rectangle(350, 190, 420, 260, tag="change")  # CHANGE

        widget = Label(self.canvas, text='START', bg="white")
        widget.pack()
        self.canvas.create_window(105, 275, window=widget)

        widget = Label(self.canvas, text='END', bg="white")
        widget.pack()
        self.canvas.create_window(245, 35, window=widget)

        widget = Label(self.canvas, text='CHANGE', bg="white")
        widget.pack()
        self.canvas.create_window(385, 275, window=widget)

        # ve mui ten
        self.canvas.create_line(210, 85, 140, 85, arrow=tkinter.LAST)  # END -> FREE
        self.canvas.create_line(350, 85, 280, 85, arrow=tkinter.LAST)  # DOCU -> END
        self.canvas.create_line(140, 225, 210, 225, arrow=tkinter.LAST)  # START -> BUSY
        self.canvas.create_line(280, 225, 350, 225, arrow=tkinter.LAST)  # BUSY -> CHANGE
        self.canvas.create_line(105, 120, 105, 190, arrow=tkinter.LAST)  # FREE -> START
        self.canvas.create_line(385, 190, 385, 120, arrow=tkinter.LAST)  # CHANGE -> DOCU

        # ve chuc nang
        #ve cac o text nhap vao FREE BUSY DOCU
        Label(self.master, text="FREE").grid(row=1, column=0)
        self.input_free = Entry(self.master)
        self.input_free.grid(row=1, column=1)

        Label(self.master, text="BUSY").grid(row=1, column=2)
        self.input_busy = Entry(self.master)
        self.input_busy.grid(row=1, column=3)

        Label(self.master, text="DOCU").grid(row=1, column=4)
        self.input_docu = Entry(self.master)
        self.input_docu.grid(row=1, column=5)

        # ve button Run Stop TS
        self.run_button = Button(self.master, width=16, padx=3, pady=3)
        self.run_button['text'] = "RUN FIRE"
        self.run_button['command'] = self.run_fire
        self.run_button.grid(row=2, column=1, padx=2, pady=2)

        self.stop_button = Button(self.master, width=16, padx=3, pady=3)
        self.stop_button['text'] = "STOP FIRE"
        self.stop_button['command'] = self.stop_fire
        self.stop_button.grid(row=2, column=3, padx=2, pady=2)

        self.ts_button = Button(self.master, width=16, padx=3, pady=3)
        self.ts_button['text'] = "TRANSITION MODE"
        self.ts_button['command'] = self.transition_system
        self.ts_button.grid(row=2, column=5, padx=2, pady=2)

        # tao lable making M
        self.label_marking = Label(self.canvas, text="MARKING M = [" + str(self.free)
                                                     + ".FREE, " + str(self.busy) + ",.BUSY " + str(self.docu) + ".DOCU]"
                                                    , bg="white")
        self.label_marking.pack()
        self.canvas.create_window(245, 10, window=self.label_marking)
    def run_fire(self):
        if (self.input_free.get() == "" and self.input_busy.get() == "" and self.input_docu.get() == ""):
            tkinter.messagebox.showwarning("Error","Please fill parameter before run mode!")
        elif (not (self.input_free.get().isnumeric() and self.input_busy.get().isnumeric()
                 and self.input_docu.get().isnumeric())):
            tkinter.messagebox.showwarning("Error","Please fill parameter >0!")
            print("FAILED\n" + "-" * 30)

        elif (int(self.input_free.get()) > 1 or int(self.input_busy.get()) > 1 or int(self.input_docu.get()) > 1):
            tkinter.messagebox.showwarning("Error","Please fill parameter <1!")
            print("FAILED\n" + "-" * 30)

        else:
            self.isSet = 1
            self.free = self.init_free = int(self.input_free.get())
            self.busy = self.init_busy = int(self.input_busy.get())
            self.docu = self.init_docu = int(self.input_docu.get())

            self.label_free.configure(text=str(self.init_free))
            self.label_busy.configure(text=str(self.init_busy))
            self.label_docu.configure(text=str(self.init_docu))
            self.label_marking.configure(text="MARKING M_0 = [" + str(self.free) + ".free, "
                                              + str(self.busy) + ".busy, " + str(self.docu) + ".docu]")

            print("SUCCESSFUL")
            print("Initial Marking: M0 = [" + str(self.init_free) + ".free, "
                  + str(self.init_busy) + ".busy, " + str(self.init_docu) + ".docu]\n" + "-" * 30)

            if self.flag_auto == 1:
                pass
            else:
                self.flag_auto *= -1
                print("AUTO FIRE MODE ON\n" + "-" * 30)
                if self.flag_auto == 1:
                    self.input_free.configure(state = tkinter.DISABLED)
                    self.input_busy.configure(state = tkinter.DISABLED)
                    self.input_docu.configure(state = tkinter.DISABLED)
                self.thread_auto_fire = threading.Thread(target=self.handle_fire)
                self.thread_auto_fire.start()


    def stop_fire(self):
        if self.flag_auto == -1:
            pass
        else:
            self.flag_auto *= -1
            if self.flag_auto == -1:
                self.input_free.configure(state = tkinter.NORMAL)
                self.input_busy.configure(state = tkinter.NORMAL)
                self.input_docu.configure(state = tkinter.NORMAL)
            print("AUTO FIRE MODE OFF\n" + "-" * 30)
    def transition_system(self):
        if (self.input_free.get() == "" and self.input_busy.get() == "" and self.input_docu.get() == ""):
            tkinter.messagebox.showwarning("Error", "Please fill parameter before run mode!")
        else:
            # FORM MARKING: [x.free, y.busy, z.docu]
            print("TRANSITION SYSTEM")
            self.markings = []
            self.state = 0
            self.transition = 0
            self.graph = Network(directed=True)

            current_marking = [self.init_free, self.init_busy, self.init_docu]
            self.markings.append(current_marking)
            self.state += 1
            self.graph.add_node(0, label=str("[" + str(current_marking[0]) + ", "
                                             + str(current_marking[1]) + ", " + str(current_marking[2]) + "]"))

            self.find_transition_relation(self.markings[0])

            self.graph.show_buttons(filter_='physics')
            self.graph.show('Transition System.html')

            print(str(self.state) + " states")
            print(str(self.transition) + " transitions\n" + "-" * 30)
    def find_transition_relation(self, current_marking):
        near_marking = self.find_near_marking(current_marking)
        for i in range (0, len(near_marking)):
            self.find_transition_relation(near_marking[i])

    def find_near_marking(self, current_marking):
        near = []
        if current_marking[0] > 0 and current_marking[1] == 0:
            self.transition += 1
            marking = [current_marking[0] - 1, current_marking[1] + 1, current_marking[2]]

            node = str("[" + str(marking[0]) + ", " + str(marking[1]) + ", " + str(marking[2]) + "]")

            if not (marking in self.markings):
                self.graph.add_node(len(self.markings), label=node)
                near.append(marking)
                self.markings.append(marking)
                self.state += 1

            self.graph.add_edge(self.markings.index(current_marking), self.markings.index(marking), label="START")

            print("[[" + str(current_marking[0]) + ".FREE, " + str(current_marking[1]) + ".BUSY, "
                  + str(current_marking[2]) + ".DOCU]" + "; ---START---> "
                  + "[" + str(marking[0]) + ".FREE, " + str(marking[1]) + ".BUSY, "
                  + str(marking[2]) + ".DOCU]")

        if current_marking[1] > 0 and current_marking[2] == 0:
            self.transition += 1
            marking = [current_marking[0], current_marking[1] - 1, current_marking[2] + 1]

            node = str("[" + str(marking[0]) + ", " + str(marking[1]) + ", " + str(marking[2]) + "]")

            if not (marking in self.markings):
                self.graph.add_node(len(self.markings), label=node)
                near.append(marking)
                self.markings.append(marking)
                self.state += 1

            self.graph.add_edge(self.markings.index(current_marking), self.markings.index(marking), label="CHANGE")

            print("[[" + str(current_marking[0]) + ".FREE, " + str(current_marking[1]) + ".BUSY, "
                  + str(current_marking[2]) + ".DOCU]" + "; ---CHANGE---> "
                  + "[" + str(marking[0]) + ".FREE, " + str(marking[1]) + ".BUSY, "
                  + str(marking[2]) + ".DOCU]")

        if current_marking[2] > 0 and current_marking[0] == 0:
            self.transition += 1
            marking = [current_marking[0] + 1, current_marking[1], current_marking[2] - 1]

            node = str("[" + str(marking[0]) + ", " + str(marking[1]) + ", " + str(marking[2]) + "]")

            if not (marking in self.markings):
                self.graph.add_node(len(self.markings), label=node)
                near.append(marking)
                self.markings.append(marking)
                self.state += 1

            self.graph.add_edge(self.markings.index(current_marking), self.markings.index(marking), label="END")

            print("[[" + str(current_marking[0]) + ".FREE, " + str(current_marking[1]) + ".BUSY, "
                  + str(current_marking[2]) + ".DOCU]" + "; ---END---> "
                  + "[" + str(marking[0]) + ".FREE, " + str(marking[1]) + ".BUSY, "
                  + str(marking[2]) + ".DOCU]")
        return near

    def handle_fire(self):
        while (self.flag_auto == 1 and self.flag_fire_start != 1 and self.flag_fire_change != 1 and self.flag_fire_end != 1):
            self.check_deadlock()
            self.fire()
            time.sleep(1.35)
    def check_deadlock(self):
        if (self.free == 0 and self.docu == 0 and self.busy == 0):
            print("DEADLOCK")
            self.stop_fire()
    def fire(self):
        if ((self.is_start_enable() and (not self.is_change_enable()) and (not self.is_end_enable())) or
                ((not self.is_start_enable()) and (self.is_change_enable()) and (not self.is_end_enable())) or
                ((not self.is_start_enable()) and (not self.is_change_enable()) and (self.is_end_enable()))):
            if self.is_start_enable():
                self.fire_start()
            elif self.is_change_enable():
                self.fire_change()
            elif self.is_end_enable():
                self.fire_end()

        elif self.is_start_enable() and (self.is_change_enable()) and (not self.is_end_enable()):
            self.fire_start()
            time.sleep(0.5)
            self.fire_change()

        elif self.is_start_enable() and (not self.is_change_enable()) and (self.is_end_enable()):
            self.fire_start()
            time.sleep(0.5)
            self.fire_end()

        elif (not self.is_start_enable()) and (self.is_change_enable()) and (self.is_end_enable()):
            self.fire_end()
            time.sleep(0.5)
            self.fire_change()

        elif self.is_start_enable() and self.is_change_enable() and self.is_end_enable():
            self.fire_start()
            time.sleep(0.5)
            self.fire_change()
            time.sleep(0.5)
            self.fire_end()

    def is_start_enable(self):
        if self.free > 0:
            return True
        else:
            return False

    def is_change_enable(self):
        if self.busy > 0:
            return True
        else:
            return False

    def is_end_enable(self):
        if self.docu > 0:
            return True
        else:
            return False

    def fire_start(self):
        if self.flag_fire_start == -1:
            self.start_dot = self.canvas.create_oval(100, 120, 110, 130, fill="blue")

            self.flag_fire_start *= -1
            self.free -= 1
            self.label_free.configure(text=str(self.free))

        if self.canvas.coords(self.start_dot)[1] != 220.0:
            self.canvas.move(self.start_dot, 0, 5)
        elif self.canvas.coords(self.start_dot)[0] != 200.0:
            self.canvas.move(self.start_dot, 5, 0)

        if self.canvas.coords(self.start_dot)[0] != 200.0:
            self.canvas.after(20, self.fire_start)
        else:
            self.canvas.delete(self.start_dot)

            self.busy += 1
            self.label_busy.configure(text=str(self.busy))
            self.label_marking.configure(text="MARKING M = [" + str(self.free) + ".free, "
                                              + str(self.busy) + ".busy, " + str(self.docu) + ".docu]")
            self.flag_fire_start *= -1

    def fire_end(self):
        if self.flag_fire_end == -1:
            self.end_dot = self.canvas.create_oval(340, 80, 350, 90, fill="blue")

            self.flag_fire_end *= -1
            self.docu -= 1
            self.label_docu.configure(text=str(self.docu))

        if self.canvas.coords(self.end_dot)[0] != 135.0:
            self.canvas.move(self.end_dot, -5, 0)

        if self.canvas.coords(self.end_dot)[0] != 135.0:
            self.canvas.after(20, self.fire_end)
        else:
            self.canvas.delete(self.end_dot)

            self.free += 1
            self.label_free.configure(text=str(self.free))
            self.label_marking.configure(text="MARKING M = [" + str(self.free) + ".free, "
                                              + str(self.busy) + ".busy, " + str(self.docu) + ".docu]")
            self.flag_fire_end *= -1

    def fire_change(self):
        if self.flag_fire_change == -1:
            self.change_dot = self.canvas.create_oval(280, 220, 290, 230, fill="blue")

            self.flag_fire_change *= -1
            self.busy -= 1
            self.label_busy.configure(text=str(self.busy))

        if self.canvas.coords(self.change_dot)[0] != 380.0:
            self.canvas.move(self.change_dot, 5, 0)
        elif self.canvas.coords(self.change_dot)[1] != 120.0:
            self.canvas.move(self.change_dot, 0, -5)

        if self.canvas.coords(self.change_dot)[1] != 120.0:
            self.canvas.after(20, self.fire_change)
        else:
            self.canvas.delete(self.change_dot)

            self.docu += 1
            self.label_docu.configure(text=str(self.docu))
            self.label_marking.configure(text="MARKING M = [" + str(self.free) + ".free, "
                                              + str(self.busy) + ".busy, " + str(self.docu) + ".docu]")
            self.flag_fire_change *= -1

    def handler(self):
        if self.flag_auto == 1:
            self.stop_fire()

        if self.flag_fire_change == 1 or self.flag_fire_end == 1 or self.flag_fire_start == 1:
            tkinter.messagebox.showwarning('Error', "Mode Run Firing is Running!")

        if tkinter.messagebox.askokcancel("Quit app ?", "Are you sure to quit"):
            self.isClosed = 1
            self.master.destroy()