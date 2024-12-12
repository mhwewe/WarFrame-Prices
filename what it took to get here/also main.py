import pywmapi as wm
from customtkinter import *
from tkinter import Frame, Label, PhotoImage


def main(item_name, item_link, arcane):
    n = -1;prices = [];names = [];lis = [];rows = 100;c = 0

    item1 = item_name
    l = wm.items.get_orders(item_link)
    w = len(l)

    while n >= -w:
        if ("OrderType.sell" in str(l[n])) and ("Status.ingame" in str(l[n])) and arcane is True and ("mod_rank=5" in str(l[n])):
            Name = str(l[n]).split("ingame_name='")
            Name = Name[1].split("', avatar")
            name = Name[0]
            names.append(name)

            Price = str(l[n]).split("platinum=")
            Price = Price[1].split(', quantit')
            price = int(Price[0])
            prices.append(price)
            c += 1
        if ("OrderType.sell" in str(l[n])) and ("Status.ingame" in str(l[n])) and arcane is False:
            Name = str(l[n]).split("ingame_name='")
            Name = Name[1].split("', avatar")
            name = Name[0]
            names.append(name)

            Price = str(l[n]).split("platinum=")
            Price = Price[1].split(', quantit')
            price = int(Price[0])
            prices.append(price)
            c += 1
        n = n - 1
    if rows > c:
        rows = c
    i = 0;
    li = []
    for price_name in sorted(zip(prices, names)):
        name_price = (
        price_name[1], f"{price_name[0]} P", f"/w {price_name[1]} Yo I want the {item1} for {price_name[0]} Plat")
        lis.append(name_price)
        i = i + 1
        if i == rows: break
    t = 0
    return lis


rows=6
i=0
item1 = main("trumna_prime_set", "trumna_prime_set", arcane=False)
item2 = main("Quassus Prime Set", "quassus_prime_set", arcane=False)
item3 = main("Xaku Prime Set", "xaku_prime_set", arcane=False)
item4 = main("Sybaris Prime Set", "sybaris_prime_set", arcane=False)
item5 = main("Arcane Energize", "arcane_energize", arcane=True)
item6 = main("Khora Prime Set", "khora_prime_set", arcane=False)
#########################################################################
def frame(frame_n_x, frame_n_y):
    frame_n = CTkFrame(master=gui, fg_color="#171e21", bg_color="#101619", border_color="#5ff5ff", border_width=2,corner_radius=7)
    frame_n.place(x=frame_n_x, y=frame_n_y)
    return frame_n

def frame_name(frame_n_x, frame_n_y):
    frame_n = CTkFrame(master=gui, fg_color="#919596", bg_color="#101619", border_color="#5ff5ff", border_width=2,corner_radius=7)
    frame_n.place(x=frame_n_x, y=frame_n_y)
    return frame_n
#########################################################################
def label_n_p(item, frame1, frame2):
    i = 0
    rows = 6
    while i < rows:
        label = CTkLabel(master=frame1, text=f"{item[i][0]}", font=("Arial", 22), width=230)
        label.pack(anchor="center", expand=True, pady=5, padx=10)
        i += 1
    i = 0
    while i < rows:
        label1 = CTkLabel(master=frame2, text=f"{item[i][1]}", font=("Arial", 22), width=65)
        label1.pack(anchor="center", expand=True, pady=5, padx=10)
        i += 1
#########################################################################
gui = CTk()
gui.geometry("800x970")
gui.config(background="#101619")
#########################################################################
# Colors
WHITE = "#3492b0"
DARK_BLUE = "#171e21"
SECOND_DARK_BLUE = "#071013"
logo = PhotoImage(file="Warframe market logo crop.png")
gui.iconphoto(True, logo)
# Custom Title Bar
class TitleBar(Frame):
    def __init__(self, parent, title: str):
        self.root = parent
        self.root.overrideredirect(True)  # For Remove Default Title Bar
        super().__init__(parent, bg=DARK_BLUE)
        self.nav_title = Label(self, text=title, foreground=WHITE, background=DARK_BLUE)

        self.nav_title.bind("<ButtonPress-1>", self.oldxyset_label)
        self.nav_title.bind("<B1-Motion>", self.move)

        self.nav_title.pack(side="left", padx=(10))

        CTkButton(self, text='✕', cursor="hand2", corner_radius=0, fg_color=DARK_BLUE,
                  hover_color=SECOND_DARK_BLUE, width=20,command=self.close_window).pack(side="right")
        self.bind("<ButtonPress-1>", self.oldxyset)
        self.bind("<B1-Motion>", self.move)

    def oldxyset(self, event):
        self.oldx = event.x
        self.oldy = event.y

    def oldxyset_label(self, event):
        self.oldx = event.x + self.nav_title.winfo_x()
        self.oldy = event.y + self.nav_title.winfo_y()

    def move(self, event):
        self.y = event.y_root - self.oldy
        self.x = event.x_root - self.oldx
        self.root.geometry(f"+{self.x}+{self.y}")

    def close_window(self):
        self.root.destroy()

# Set Title Bar
titlebar = TitleBar(gui, title="Test Window")
titlebar.pack(fill="both")
#########################################################################
frame1= frame(frame_n_x=5, frame_n_y=40)
frame2= frame(frame_n_x=260, frame_n_y=40)
label_n_p(item1,frame1,frame2)
frame1= frame(frame_n_x=5, frame_n_y=273)
frame2= frame(frame_n_x=260, frame_n_y=273)
label_n_p(item2,frame1,frame2)
frame1= frame(frame_n_x=5, frame_n_y=506)
frame2= frame(frame_n_x=260, frame_n_y=506)
label_n_p(item3,frame1,frame2)
frame1= frame(frame_n_x=5, frame_n_y=739)
frame2= frame(frame_n_x=260, frame_n_y=739)
label_n_p(item4,frame1,frame2)
frame1= frame(frame_n_x=355, frame_n_y=40)
frame2= frame(frame_n_x=610, frame_n_y=40)
label_n_p(item5,frame1,frame2)
frame1= frame(frame_n_x=355, frame_n_y=273)
frame2= frame(frame_n_x=610, frame_n_y=273)
label_n_p(item6,frame1,frame2)
#########################################################################
gui.mainloop()

