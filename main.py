import re
a = '''97+ 180+  31 87+ 113+  10  250+  27   87+  87+ 119+ 112+  13 4 250+ 108+  28  135  240+ 112+ 192+ 192+  26  108+ 250+   6  250+ 256+  30  250+  38  250+ 205+ 245+ 110+  76+ 175+ 107+ 270+  24  196+  60   20   68+  20   30   60  109   65   33   95   28   42 83+ 95+ 107+  85+ 120+ 120+ 212+  59  185+ 280+ 162  145+  11  145+ 180   83+ 212+ 172  212+  10  120+  10  115+  78+  43  198  244+ 120+ 23  196  235   26   30  207+ 130   83+ 186+ 205+  79+ 207+ 213+  14   94+ 186+   8   88   79+ 216+  43   61   79+ 186+  72  106+ 121+ 146+ 206+ 200+ 209+  79+ 194+ 209+  54+ 146+ 121+ 121+ 7 146+ 129 186+ 8 146+ 213+ 245+ 209+ 146+ 270+ 186+ 121+ 214 186+  65 171 22+ 213+  79+ 230+ 209+ 230+ 245+ 205+ 208+  64 10  111  107+ 147+  54+  90  210+  91+ 187+  26  107+ 154  113 7 40   90+
107+  35  147+ 214+ 246+  23  117+ 285+ 271+ 215+ 211+ 108+ 118+ 188+ 126   41  241  209+  60+ 123+  11  215+ 170  148+ 150   96  180 258+  90+  29+ 207   29   95+ 214+ 187+ 247+ 258+  33+ 231+  87+  88+  88+  88+  88+ 214+  87+  71+ 140+  10  187+ 147+  85+ 246+  75+ 215+  45   12+ 256+  95+ 172   73   91+ 187+  72+  73   33   43   77  100  210+ 193   80+  32   86+ 187+  66   74+  30+ 134+  94+ 215+ 201+  90  220+ 245+  78   82+  74+ 233+ 174+  74+  50  187+  94+  67   82  174+ 109+ 109+ 105+ 278+  74+  95+ 257+ 115   44  197+ 237+ 104+ 214+ 174+ 245+  10   63+ 147+ 233+ 246+  30  197+ 195+ 104+ 187+  55  237+ 201+ 172+ 107+ 244+ 244+  15   15  244+ 250+ 244+ 14 80+ 16+'''
a.strip()
while "  " in a:
    a = a.replace("  ", " ")
while "\n" in a:
    a = a.replace("\n", " ")

a = a.split(" ")
for item in a:
    if "+" in item:
        print(item)