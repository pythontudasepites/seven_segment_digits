
from seven_segment_model import SegmentId, DigitSegmentDefinitions, Digit1SegmentDefinitions, Digit2SegmentDefinitions, Digit7SegmentsPoints
import tkinter as tk

class Digit7Segments(tk.Frame):
    """Egy olyan grafikus elemet (widget) valósít meg, amely a render_digits() metódusnak karakterláncként átadott számjegyeket
    hétszegmenses számjegyek formájában rajzolja ki és helyezi el egymást követően egy keretben (Frame).
    """
    def __init__(self, master, digits_7segments_points: Digit7SegmentsPoints):
        super().__init__(master)
        self.digits_7segments_points = digits_7segments_points  # A kirajzolandó számjegy szegmenseinek pontjai.
        # Egy számjegy rajzelemeit tartalmazó vászon elem létrehozása.
        self.cnv: tk.Canvas = tk.Canvas(self,  width=digits_7segments_points.width, height=digits_7segments_points.height)
        self.cnv.pack()
        # A szegmenseket grafikusan megvalósító sokszögek létrehozása a szegmensek modellbeli pontjai alapján.
        # A sokszögekhez egy közös, valamint a szegmensek elrendezési pozíciója szerinti egyedi tageket rendelünk.
        self.all_segment_tags = set()
        for key, segment_points in digits_7segments_points.segments.items():
            self.all_segment_tags.add(key.name)
            self.cnv.create_polygon(*segment_points, fill='black', state=tk.HIDDEN, tag=('SEGMENT', key.name))

    def _render_one_digit(self, num: int | str):
        """A megadott számjegy kirajzolása a vásznon a megfelelő sokszögek megjelenítésének engedélyezésével."""
        num = str(num)
        self.cnv.itemconfig('SEGMENT', state=tk.HIDDEN)  # Induláskor minden szegmens megjelenítése le van tiltva.
        # Az egyes számjegyekhez hozzárendeljük a megjelenítendő szegmensek azonosítóit.
        num_segments_to_be_displayed = {'0': self.all_segment_tags - {SegmentId.CENTER.name},
                                        '1': {SegmentId.TOP_RIGHT.name, SegmentId.BOTTOM_RIGHT.name},
                                        '2': self.all_segment_tags - {SegmentId.TOP_LEFT.name, SegmentId.BOTTOM_RIGHT.name},
                                        '3': self.all_segment_tags - {SegmentId.TOP_LEFT.name, SegmentId.BOTTOM_LEFT.name},
                                        '4': {SegmentId.TOP_LEFT.name, SegmentId.TOP_RIGHT.name, SegmentId.CENTER.name,
                                              SegmentId.BOTTOM_RIGHT.name},
                                        '5': self.all_segment_tags - {SegmentId.TOP_RIGHT.name, SegmentId.BOTTOM_LEFT.name},
                                        '6': self.all_segment_tags - {SegmentId.TOP_RIGHT.name},
                                        '7': {SegmentId.TOP.name, SegmentId.TOP_RIGHT.name, SegmentId.BOTTOM_RIGHT.name},
                                        '8': self.all_segment_tags,
                                        '9': self.all_segment_tags - {SegmentId.BOTTOM_LEFT.name}}
        # A megjelenítendő szegmensek kirajzolását engedélyezzük.
        for tg in num_segments_to_be_displayed.get(num, ()):
            self.cnv.itemconfig(tg, state=tk.NORMAL)

    def config(self, **kw):
        """Felülírt config metódus, hogy a vászon és a szegmensek jellemzőit (pl. színét) be lehessen állítani."""
        if 'segment_color' in kw:
            self.cnv.itemconfig('SEGMENT', fill=kw['segment_color'])
        if 'bg' in kw:
            self.cnv.config(bg=kw['bg'])

    def render_digits(self, digits: str, segment_color='black'):
        """Több számjegy egymás melleti megjelenítése egy keret elemen, ha az első argumentum csak számjegyeket tartalmazó karakterlánc.
        A metódus a keret elemet adja vissza.
        """
        if digits.isdecimal():
            for w in self.master.slaves():
                if str(w) == 'digitframe':
                    w.destroy()
            frame_with_digits = tk.Frame(self.master, name='digitframe')
            for digit in digits:
                cd = Digit7Segments(frame_with_digits, self.digits_7segments_points)
                cd.config(segment_color=segment_color)
                cd._render_one_digit(digit)
                cd.pack(side=tk.LEFT, padx=(0, 2))
            return frame_with_digits

