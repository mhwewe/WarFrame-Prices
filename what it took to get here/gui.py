from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pywmapi as wm
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


item1_link = "trumna_prime_set"
item2_link = "trumna_prime_set"
item3_link = "trumna_prime_set"
item4_link = "trumna_prime_set"
item5_link = "trumna_prime_set"
item6_link = "trumna_prime_set"

item1 = main("trumna_prime_set", "trumna_prime_set", arcane=False)
item2 = main("Quassus Prime Set", "quassus_prime_set", arcane=False)
item3 = main("Xaku Prime Set", "xaku_prime_set", arcane=False)
item4 = main("Sybaris Prime Set", "sybaris_prime_set", arcane=False)
item5 = main("Arcane Energize", "arcane_energize", arcane=True)
item6 = main("Khora Prime Set", "khora_prime_set", arcane=False)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "build" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("970x1000") ##### 970 Original width
window.configure(bg = "#101619")


canvas = Canvas(
    window,
    bg = "#101619",
    height = 1000,
    width = 970,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    500.0,
    500.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    157.0,
    152.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    157.0,
    27.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    296.0,
    69.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    296.0,
    102.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    296.0,
    102.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    296.0,
    69.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    296.0,
    136.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    296.0,
    169.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    296.0,
    203.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    296.0,
    236.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    485.0,
    152.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    485.0,
    27.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    813.0,
    152.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    813.0,
    27.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    951.0,
    103.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    623.0,
    103.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    623.0,
    70.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    623.0,
    136.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    623.0,
    169.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    623.0,
    202.0,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    623.0,
    235.0,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    951.0,
    70.0,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    951.0,
    136.0,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    951.0,
    169.0,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    951.0,
    202.0,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_27.png"))
image_27 = canvas.create_image(
    951.0,
    235.0,
    image=image_image_27
)

image_image_28 = PhotoImage(
    file=relative_to_assets("image_28.png"))
image_28 = canvas.create_image(
    813.0,
    413.0,
    image=image_image_28
)

image_image_29 = PhotoImage(
    file=relative_to_assets("image_29.png"))
image_29 = canvas.create_image(
    813.0,
    288.0,
    image=image_image_29
)

image_image_30 = PhotoImage(
    file=relative_to_assets("image_30.png"))
image_30 = canvas.create_image(
    813.0,
    674.0,
    image=image_image_30
)

image_image_31 = PhotoImage(
    file=relative_to_assets("image_31.png"))
image_31 = canvas.create_image(
    813.0,
    549.0,
    image=image_image_31
)

image_image_32 = PhotoImage(
    file=relative_to_assets("image_32.png"))
image_32 = canvas.create_image(
    485.0,
    413.0,
    image=image_image_32
)

image_image_33 = PhotoImage(
    file=relative_to_assets("image_33.png"))
image_33 = canvas.create_image(
    485.0,
    288.0,
    image=image_image_33
)

image_image_34 = PhotoImage(
    file=relative_to_assets("image_34.png"))
image_34 = canvas.create_image(
    623.0,
    364.0,
    image=image_image_34
)

image_image_35 = PhotoImage(
    file=relative_to_assets("image_35.png"))
image_35 = canvas.create_image(
    623.0,
    331.0,
    image=image_image_35
)

image_image_36 = PhotoImage(
    file=relative_to_assets("image_36.png"))
image_36 = canvas.create_image(
    951.0,
    364.0,
    image=image_image_36
)

image_image_37 = PhotoImage(
    file=relative_to_assets("image_37.png"))
image_37 = canvas.create_image(
    951.0,
    331.0,
    image=image_image_37
)

image_image_38 = PhotoImage(
    file=relative_to_assets("image_38.png"))
image_38 = canvas.create_image(
    951.0,
    397.0,
    image=image_image_38
)

image_image_39 = PhotoImage(
    file=relative_to_assets("image_39.png"))
image_39 = canvas.create_image(
    951.0,
    430.0,
    image=image_image_39
)

image_image_40 = PhotoImage(
    file=relative_to_assets("image_40.png"))
image_40 = canvas.create_image(
    951.0,
    463.0,
    image=image_image_40
)

image_image_41 = PhotoImage(
    file=relative_to_assets("image_41.png"))
image_41 = canvas.create_image(
    951.0,
    496.0,
    image=image_image_41
)

image_image_42 = PhotoImage(
    file=relative_to_assets("image_42.png"))
image_42 = canvas.create_image(
    951.0,
    625.0,
    image=image_image_42
)

image_image_43 = PhotoImage(
    file=relative_to_assets("image_43.png"))
image_43 = canvas.create_image(
    951.0,
    592.0,
    image=image_image_43
)

image_image_44 = PhotoImage(
    file=relative_to_assets("image_44.png"))
image_44 = canvas.create_image(
    951.0,
    658.0,
    image=image_image_44
)

image_image_45 = PhotoImage(
    file=relative_to_assets("image_45.png"))
image_45 = canvas.create_image(
    951.0,
    691.0,
    image=image_image_45
)

image_image_46 = PhotoImage(
    file=relative_to_assets("image_46.png"))
image_46 = canvas.create_image(
    951.0,
    724.0,
    image=image_image_46
)

image_image_47 = PhotoImage(
    file=relative_to_assets("image_47.png"))
image_47 = canvas.create_image(
    951.0,
    757.0,
    image=image_image_47
)

image_image_48 = PhotoImage(
    file=relative_to_assets("image_48.png"))
image_48 = canvas.create_image(
    623.0,
    397.0,
    image=image_image_48
)

image_image_49 = PhotoImage(
    file=relative_to_assets("image_49.png"))
image_49 = canvas.create_image(
    623.0,
    430.0,
    image=image_image_49
)

image_image_50 = PhotoImage(
    file=relative_to_assets("image_50.png"))
image_50 = canvas.create_image(
    623.0,
    463.0,
    image=image_image_50
)

image_image_51 = PhotoImage(
    file=relative_to_assets("image_51.png"))
image_51 = canvas.create_image(
    623.0,
    496.0,
    image=image_image_51
)

image_image_52 = PhotoImage(
    file=relative_to_assets("image_52.png"))
image_52 = canvas.create_image(
    485.0,
    674.0,
    image=image_image_52
)

image_image_53 = PhotoImage(
    file=relative_to_assets("image_53.png"))
image_53 = canvas.create_image(
    623.0,
    625.0,
    image=image_image_53
)

image_image_54 = PhotoImage(
    file=relative_to_assets("image_54.png"))
image_54 = canvas.create_image(
    623.0,
    592.0,
    image=image_image_54
)

image_image_55 = PhotoImage(
    file=relative_to_assets("image_55.png"))
image_55 = canvas.create_image(
    623.0,
    658.0,
    image=image_image_55
)

image_image_56 = PhotoImage(
    file=relative_to_assets("image_56.png"))
image_56 = canvas.create_image(
    623.0,
    691.0,
    image=image_image_56
)

image_image_57 = PhotoImage(
    file=relative_to_assets("image_57.png"))
image_57 = canvas.create_image(
    623.0,
    724.0,
    image=image_image_57
)

image_image_58 = PhotoImage(
    file=relative_to_assets("image_58.png"))
image_58 = canvas.create_image(
    623.0,
    757.0,
    image=image_image_58
)

image_image_59 = PhotoImage(
    file=relative_to_assets("image_59.png"))
image_59 = canvas.create_image(
    485.0,
    549.0,
    image=image_image_59
)

image_image_60 = PhotoImage(
    file=relative_to_assets("image_60.png"))
image_60 = canvas.create_image(
    157.0,
    413.0,
    image=image_image_60
)

image_image_61 = PhotoImage(
    file=relative_to_assets("image_61.png"))
image_61 = canvas.create_image(
    295.0,
    364.0,
    image=image_image_61
)

image_image_62 = PhotoImage(
    file=relative_to_assets("image_62.png"))
image_62 = canvas.create_image(
    295.0,
    331.0,
    image=image_image_62
)

image_image_63 = PhotoImage(
    file=relative_to_assets("image_63.png"))
image_63 = canvas.create_image(
    295.0,
    397.0,
    image=image_image_63
)

image_image_64 = PhotoImage(
    file=relative_to_assets("image_64.png"))
image_64 = canvas.create_image(
    295.0,
    430.0,
    image=image_image_64
)

image_image_65 = PhotoImage(
    file=relative_to_assets("image_65.png"))
image_65 = canvas.create_image(
    295.0,
    463.0,
    image=image_image_65
)

image_image_66 = PhotoImage(
    file=relative_to_assets("image_66.png"))
image_66 = canvas.create_image(
    295.0,
    496.0,
    image=image_image_66
)

image_image_67 = PhotoImage(
    file=relative_to_assets("image_67.png"))
image_67 = canvas.create_image(
    157.0,
    288.0,
    image=image_image_67
)

image_image_68 = PhotoImage(
    file=relative_to_assets("image_68.png"))
image_68 = canvas.create_image(
    157.0,
    674.0,
    image=image_image_68
)

image_image_69 = PhotoImage(
    file=relative_to_assets("image_69.png"))
image_69 = canvas.create_image(
    295.0,
    625.0,
    image=image_image_69
)

image_image_70 = PhotoImage(
    file=relative_to_assets("image_70.png"))
image_70 = canvas.create_image(
    295.0,
    592.0,
    image=image_image_70
)

image_image_71 = PhotoImage(
    file=relative_to_assets("image_71.png"))
image_71 = canvas.create_image(
    295.0,
    658.0,
    image=image_image_71
)

image_image_72 = PhotoImage(
    file=relative_to_assets("image_72.png"))
image_72 = canvas.create_image(
    295.0,
    691.0,
    image=image_image_72
)

image_image_73 = PhotoImage(
    file=relative_to_assets("image_73.png"))
image_73 = canvas.create_image(
    295.0,
    724.0,
    image=image_image_73
)

image_image_74 = PhotoImage(
    file=relative_to_assets("image_74.png"))
image_74 = canvas.create_image(
    295.0,
    757.0,
    image=image_image_74
)

image_image_75 = PhotoImage(
    file=relative_to_assets("image_75.png"))
image_75 = canvas.create_image(
    157.0,
    806.0,
    image=image_image_75
)

image_image_76 = PhotoImage(
    file=relative_to_assets("image_76.png"))
image_76 = canvas.create_image(
    485.0,
    910.0,
    image=image_image_76
)

image_image_77 = PhotoImage(
    file=relative_to_assets("image_77.png"))
image_77 = canvas.create_image(
    623.0,
    877.0,
    image=image_image_77
)

image_image_78 = PhotoImage(
    file=relative_to_assets("image_78.png"))
image_78 = canvas.create_image(
    623.0,
    844.0,
    image=image_image_78
)

image_image_79 = PhotoImage(
    file=relative_to_assets("image_79.png"))
image_79 = canvas.create_image(
    623.0,
    910.0,
    image=image_image_79
)

image_image_80 = PhotoImage(
    file=relative_to_assets("image_80.png"))
image_80 = canvas.create_image(
    623.0,
    943.0,
    image=image_image_80
)

image_image_81 = PhotoImage(
    file=relative_to_assets("image_81.png"))
image_81 = canvas.create_image(
    623.0,
    976.0,
    image=image_image_81
)

image_image_82 = PhotoImage(
    file=relative_to_assets("image_82.png"))
image_82 = canvas.create_image(
    485.0,
    807.0,
    image=image_image_82
)

image_image_83 = PhotoImage(
    file=relative_to_assets("image_83.png"))
image_83 = canvas.create_image(
    813.0,
    910.0,
    image=image_image_83
)

image_image_84 = PhotoImage(
    file=relative_to_assets("image_84.png"))
image_84 = canvas.create_image(
    951.0,
    877.0,
    image=image_image_84
)

image_image_85 = PhotoImage(
    file=relative_to_assets("image_85.png"))
image_85 = canvas.create_image(
    951.0,
    844.0,
    image=image_image_85
)

image_image_86 = PhotoImage(
    file=relative_to_assets("image_86.png"))
image_86 = canvas.create_image(
    951.0,
    910.0,
    image=image_image_86
)

image_image_87 = PhotoImage(
    file=relative_to_assets("image_87.png"))
image_87 = canvas.create_image(
    951.0,
    943.0,
    image=image_image_87
)

image_image_88 = PhotoImage(
    file=relative_to_assets("image_88.png"))
image_88 = canvas.create_image(
    951.0,
    976.0,
    image=image_image_88
)

image_image_89 = PhotoImage(
    file=relative_to_assets("image_89.png"))
image_89 = canvas.create_image(
    813.0,
    806.0,
    image=image_image_89
)

image_image_90 = PhotoImage(
    file=relative_to_assets("image_90.png"))
image_90 = canvas.create_image(
    157.0,
    549.0,
    image=image_image_90
)

image_image_91 = PhotoImage(
    file=relative_to_assets("image_91.png"))
image_91 = canvas.create_image(
    157.0,
    910.0,
    image=image_image_91
)

image_image_92 = PhotoImage(
    file=relative_to_assets("image_92.png"))
image_92 = canvas.create_image(
    295.0,
    879.0,
    image=image_image_92
)

image_image_93 = PhotoImage(
    file=relative_to_assets("image_93.png"))
image_93 = canvas.create_image(
    295.0,
    846.0,
    image=image_image_93
)

image_image_94 = PhotoImage(
    file=relative_to_assets("image_94.png"))
image_94 = canvas.create_image(
    295.0,
    912.0,
    image=image_image_94
)

image_image_95 = PhotoImage(
    file=relative_to_assets("image_95.png"))
image_95 = canvas.create_image(
    295.0,
    945.0,
    image=image_image_95
)

image_image_96 = PhotoImage(
    file=relative_to_assets("image_96.png"))
image_96 = canvas.create_image(
    295.0,
    978.0,
    image=image_image_96
)

canvas.create_text(
    56.0,
    12.0,
    anchor="nw",
    text="Trumna Prime Set",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

# canvas.create_text(
#     56.0,
#     12.0,
#     anchor="nw",
#     text="Trumna Prime Set",
#     fill="#FFFFFF",
#     font=("Inter", 24 * -1)
# )

canvas.create_text(
    901.0,
    967.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    967.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    934.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    934.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    901.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    901.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    868.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    868.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    835.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    835.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    712.0,
    792.0,
    anchor="nw",
    text="Trumna Prime Set",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    901.0,
    747.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    747.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    714.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    714.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    681.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    681.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    648.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    648.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    615.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    615.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    582.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    582.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    712.0,
    534.0,
    anchor="nw",
    text="Trumna Prime Set",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    901.0,
    486.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    486.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    453.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    453.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    420.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    420.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    387.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    387.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    354.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    354.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    321.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    321.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    712.0,
    273.0,
    anchor="nw",
    text="Trumna Prime Set",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    901.0,
    225.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    225.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    192.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    192.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    159.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    159.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    126.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    126.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    93.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    93.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    901.0,
    60.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    673.0,
    60.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    712.0,
    12.0,
    anchor="nw",
    text="Trumna Prime Set",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    573.0,
    967.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    967.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    934.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    934.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    901.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    901.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    868.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    868.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    835.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    835.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    384.0,
    793.0,
    anchor="nw",
    text="Trumna Prime Set",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    573.0,
    747.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    747.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    714.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    714.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    681.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    681.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    648.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    648.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    615.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    615.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    582.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    582.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    384.0,
    534.0,
    anchor="nw",
    text="Trumna Prime Set", ###########################################################################################
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    573.0,
    486.0,
    anchor="nw",
    text=item6[5][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    486.0,
    anchor="nw",
    text=item6[5][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    453.0,
    anchor="nw",
    text=item6[4][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    453.0,
    anchor="nw",
    text=item6[4][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    420.0,
    anchor="nw",
    text=item6[3][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    420.0,
    anchor="nw",
    text=item6[3][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    387.0,
    anchor="nw",
    text=item6[2][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    387.0,
    anchor="nw",
    text=item6[2][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    354.0,
    anchor="nw",
    text=item6[1][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    354.0,
    anchor="nw",
    text=item6[1][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    573.0,
    321.0,
    anchor="nw",
    text=item6[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    321.0,
    anchor="nw",
    text=item6[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    384.0,
    273.0,
    anchor="nw",
    text="Khora Prime Set",#################################################
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    570.0,
    225.0,
    anchor="nw",
    text=item5[5][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    225.0,
    anchor="nw",
    text=item5[5][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    570.0,
    192.0,
    anchor="nw",
    text=item5[4][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    192.0,
    anchor="nw",
    text=item5[4][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    570.0,
    159.0,
    anchor="nw",
    text=item5[3][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    159.0,
    anchor="nw",
    text=item5[3][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    570.0,
    126.0,
    anchor="nw",
    text=item5[2][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    126.0,
    anchor="nw",
    text=item5[2][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    570.0,
    93.0,
    anchor="nw",
    text=item5[1][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    93.0,
    anchor="nw",
    text=item5[1][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    570.0,
    60.0,
    anchor="nw",
    text=item5[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    345.0,
    60.0,
    anchor="nw",
    text=item5[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    384.0,
    12.0,
    anchor="nw",
    text="Arcane Energize",########################################################
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    245.0,
    967.0,
    anchor="nw",
    text=item4[4][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    967.0,
    anchor="nw",
    text=item4[4][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    934.0,
    anchor="nw",
    text=item4[3][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    934.0,
    anchor="nw",
    text=item4[3][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    901.0,
    anchor="nw",
    text=item4[2][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    901.0,
    anchor="nw",
    text=item4[2][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    868.0,
    anchor="nw",
    text=item4[1][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    868.0,
    anchor="nw",
    text=item4[1][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    835.0,
    anchor="nw",
    text=item4[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    835.0,
    anchor="nw",
    text=item4[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    56.0,
    792.0,
    anchor="nw",
    text="Sybaris Prime Set", ##################################################
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    245.0,
    747.0,
    anchor="nw",
    text=item3[5][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    747.0,
    anchor="nw",
    text=item3[5][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    714.0,
    anchor="nw",
    text=item3[4][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    714.0,
    anchor="nw",
    text=item3[4][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    681.0,
    anchor="nw",
    text=item3[3][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    681.0,
    anchor="nw",
    text=item3[3][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    648.0,
    anchor="nw",
    text=item3[2][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    648.0,
    anchor="nw",
    text=item3[2][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    615.0,
    anchor="nw",
    text=item3[1][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    615.0,
    anchor="nw",
    text=item3[1][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    582.0,
    anchor="nw",
    text=item3[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    582.0,
    anchor="nw",
    text=item3[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    56.0,
    534.0,
    anchor="nw",
    text="Xaku Prime Set", ############################################################################################
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    245.0,
    486.0,
    anchor="nw",
    text=item2[5][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    486.0,
    anchor="nw",
    text=item2[5][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    453.0,
    anchor="nw",
    text=item2[4][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    453.0,
    anchor="nw",
    text=item2[4][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    420.0,
    anchor="nw",
    text=item2[3][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    420.0,
    anchor="nw",
    text=item2[3][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    387.0,
    anchor="nw",
    text=item2[2][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    387.0,
    anchor="nw",
    text=item2[2][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    354.0,
    anchor="nw",
    text=item2[1][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    354.0,
    anchor="nw",
    text=item2[1][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    321.0,
    anchor="nw",
    text=item2[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    321.0,
    anchor="nw",
    text=item2[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    56.0,
    273.0,
    anchor="nw",
    text="Quassus Prime Set",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    245.0,
    225.0,
    anchor="nw",
    text=item1[5][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    225.0,
    anchor="nw",
    text=item1[5][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    192.0,
    anchor="nw",
    text=item1[4][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    192.0,
    anchor="nw",
    text=item1[4][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    159.0,
    anchor="nw",
    text=item1[3][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    159.0,
    anchor="nw",
    text=item1[3][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    126.0,
    anchor="nw",
    text=item1[2][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    126.0,
    anchor="nw",
    text=item1[2][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    93.0,
    anchor="nw",
    text=item1[1][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    93.0,
    anchor="nw",
    text=item1[1][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    245.0,
    60.0,
    anchor="nw",
    text=item1[0][1],
    fill="#CB4A9E",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    17.0,
    60.0,
    anchor="nw",
    text=item1[0][0],
    fill="#3C879C",
    font=("Inter", 16 * -1)
)


window.resizable(False, False)
window.mainloop()
