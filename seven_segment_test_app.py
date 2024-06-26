import seven_segment_model as model
from seven_segment_digit_widget import Digits7Segments
import tkinter as tk
from tkinter import colorchooser


class SevenSegmentDigitsTestApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Hétszegmenses számjegyek')
        # A főablak két részre van osztva két keretobjektummal.
        # A felsőben a beviteli űrlap szerepel, az alsóban a hétszegmenses számok jelennek meg.
        self.frame_top, self.frame_bottom = tk.Frame(self, borderwidth=1, relief=tk.SOLID), tk.Frame(self)

        # Grafikus elemek létrehozása.
        # A megjeleníteni kívánt számjegyek beviteli mezője a hozzátartozó címkével.
        self.digits = tk.StringVar(self, value='1234567890')
        lbl1 = tk.Label(self.frame_top, text='Számjegyek:', font=('Arial', 14))
        ebx1 = tk.Entry(self.frame_top, font=('Consolas', 16, 'bold'), textvariable=self.digits)
        # A megjeleníteni kívánt számjegyek színének beviteli mezője a hozzátartozó címkével. Itt nem csak a szín
        # kódját, hanem a szín érvényes nevét is be lehet írni. Egy külön nyomógombbal tetszőleges szín választható
        # a megjelenő palettáról.
        self.digit_color = tk.StringVar(self, value='black')
        lbl2 = tk.Label(self.frame_top, text='Számjegyszín:', font=('Arial', 14))
        ebx2 = tk.Entry(self.frame_top, font=('Consolas', 16, 'bold'), textvariable=self.digit_color)
        btn_color_selection = tk.Button(self.frame_top, text='Színválasztás', font=('Arial', 14),
                                        command=lambda: self.digit_color.set(
                                            c if (c := colorchooser.askcolor(color='black')[1]) is not None
                                            else self.digit_color.get()))
        # A megjeleníteni kívánt számjegyek pixelben mért szélességének beviteli mezője a hozzátartozó címkével.
        self.digit_width = tk.StringVar(self, value='60')
        lbl3 = tk.Label(self.frame_top, text='Számjegyszélesség:', font=('Arial', 14))
        ebx3 = tk.Entry(self.frame_top, font=('Consolas', 16, 'bold'), textvariable=self.digit_width)
        # A megjelenítendő számjegyek stílusának kiválasztását lehetővé tevő választógombok a hozzátartozó címkével.
        # Stílusváltás esetén a számok azonnal megjelennek az új kinézettel.
        lbl4 = tk.Label(self.frame_top, text='Számjegytípus:', font=('Arial', 14))
        self.rbvar = tk.IntVar(self, value=1)
        rb_common_configs = dict(variable=self.rbvar, font=('Arial', 14), indicatoron=True, anchor=tk.W)
        rb1 = tk.Radiobutton(self.frame_top, **rb_common_configs, text='stílus1', value=1,
                             command=self.create_digits)
        rb2 = tk.Radiobutton(self.frame_top, **rb_common_configs, text='stílus2', value=2,
                             command=self.create_digits)
        # A beviteli mezők tartalma szerinti számjegyek megjelenítése.
        btn_display = tk.Button(self.frame_top, text='Megjelenítés', font=('Arial', 14, 'bold'),
                                command=self.create_digits)

        # Grafikus elemek lehelyezése.
        self.frame_top.pack(fill=tk.BOTH)
        self.frame_bottom.pack(fill=tk.BOTH, pady=15)

        lbl1.grid(row=0, column=0, sticky='e')
        ebx1.grid(row=0, column=1)

        lbl2.grid(row=1, column=0, sticky='e')
        ebx2.grid(row=1, column=1)
        btn_color_selection.grid(row=1, column=2)

        lbl3.grid(row=2, column=0, sticky='e')
        ebx3.grid(row=2, column=1)

        lbl4.grid(row=3, column=0, sticky='e')
        rb1.grid(row=3, column=1, sticky='w')
        rb2.grid(row=4, column=1, sticky='w')

        btn_display.grid(row=5, column=0, sticky='w')

        self.segments_def_classes = {1: model.Digit1SegmentDefinitions, 2: model.Digit2SegmentDefinitions}

    def create_digits(self):
        """Új hétszegmenses számsorozat előállítása az aktuális jellemzők alapján."""
        # Az alsó keretből az eddigi számsorozat törlése.
        for d in self.frame_bottom.slaves():
            if type(d) is Digits7Segments:
                d.destroy()

        width: int = int(w) if (w := self.digit_width.get()) else 60
        segments_def_class = self.segments_def_classes[self.rbvar.get()]
        digit_7segments = Digits7Segments(self.frame_bottom,
                                          self.digits.get(), width, segment_color=self.digit_color.get(),
                                          segmentsdefinitions_class=segments_def_class)
        digit_7segments.pack(side=tk.LEFT)  # Lehelyezés az alsó keretben.

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = SevenSegmentDigitsTestApp()
    app.run()
