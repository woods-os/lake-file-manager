#!/usr/bin/python3




import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk #, Gdk
from gi.repository.GdkPixbuf import Pixbuf

from os import listdir, system, path


#location = ""

#location_list = listdir(location)


class fileBrowser(Gtk.Window):

    def __init__(self,location):
        Gtk.Window.__init__(self, title="Files")
        self.set_default_size(600, 500)

        #vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        #vbox.set_homogeneous(False)

        inputbar = Gtk.Entry()
        inputbar.set_text("Location")
        #vbox.pack_start(inputbar, True, True, 0)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        #vbox.pack_start(scrolled, True, True, 0)

        #path = "/"

        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(30)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

        self.create_flowbox(flowbox, location)

        scrolled.add(flowbox)

        #self.add(vbox)
        self.add(scrolled)
        self.show_all()




    def addBtn(self, name, icon, location):


        liststore = Gtk.ListStore(Pixbuf, str)
        iconview = Gtk.IconView.new()
        iconview.set_model(liststore)
        iconview.set_pixbuf_column(0)
        iconview.set_text_column(1)

        pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 48, 0)
        liststore.append([pixbuf, location])

        #label = Gtk.Label(location)


        btn = Gtk.Button()

        btn.add(iconview)
        #btn.add(label)
        btn.connect("clicked", self.btnclicked,location)




# IMPLEMENT THIS METHOD *ASAP*  --------------------------
#    def btnClick (event):
#        if event == "clicked":
#            print ("fired!")
#            system(executable)
#
#    btn.connect("clicked", btnClick)
# --------------------------------------------------------
        #flowbox.add(btn)
        #btnList.append(row)
        return btn


    def btnclicked(self,button, location):
        newfm = fileBrowser(location)
        newfm.connect("delete-event", Gtk.main_quit)
        newfm.show_all()
        Gtk.main()



    def create_flowbox (self, flowbox, loc):
        for item in sorted(listdir(loc)):
            location = item
            icon = "firefox"
            if path.isdir(loc+item):
                location = loc + item + "/"
                icon = "folder"
            button = self.addBtn(item,icon,location)
            flowbox.add(button)


win = fileBrowser("/")
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
