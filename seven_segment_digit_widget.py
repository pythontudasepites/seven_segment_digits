
from seven_segment_model import SegmentId, Digit7SegmentsPoints
import seven_segment_model as model
import tkinter as tk

class One7SegmentDigit(tk.Frame):
    """Egy olyan grafikus elemet valósít meg, amely a render_digit() metódusnak str vagy int típusú argumentumként 
    átadott számjegyet hétszegmenses számjegy formájában rajzolja ki.
    """
    def __init__(self, master, digits_7segments_points: Digit7SegmentsPoints):
        super().__init__(master)
        self.digits_7segments_points = digits_7segments_points  # A kirajzolandó számjegy szegmenseinek pontjai.
        # Egy számjegy rajzelemeit tartalmazó vászon elem létrehozása.
        self.cnv: tk.Canvas = tk.Canvas(self, width=digits_7segments_points.width,
                                        height=digits_7segments_points.height, highlightthickness=0)
        self.cnv.pack()
        # A szegmenseket grafikusan megvalósító sokszögek létrehozása a szegmensek modellbeli pontjai alapján.
        # A sokszögekhez egy közös, valamint a szegmensek elrendezési pozíciója szerinti egyedi tageket rendelünk.
        self.all_segment_tags = set()
        for key, segment_points in digits_7segments_points.segments.items():
            self.all_segment_tags.add(key.name)
            self.cnv.create_polygon(*segment_points, fill='black', state=tk.HIDDEN, tag=('SEGMENT', key.name))

    def render_digit(self, num: int | str):
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
        return self

    def config(self, **kw):
        """Felülírt config metódus, hogy a szegmensek színét be lehessen állítani."""
        if 'segment_color' in kw:
            self.cnv.itemconfig('SEGMENT', fill=kw['segment_color'])

class Digits7Segments(tk.Frame):
    """Egy olyan grafikus elemet valósít meg, amely a konstruktorban a 'digits' str vagy int típusú argumentummal  
    meghatározott számjegyeket a megadott szélességű hétszegmenses számjegyek formájában rajzolja ki egymást követően, a
    'segment_color' színben, és 'segmentsdefinitions_class' osztály által definiált stílusban.
    A szegmensek magassága és szélessége, valamint a szegmensek között függőleges rés opcionálisan megadható.
    """
    def __init__(self, master, digits: int | str, width: int, segment_height: int | None = None, gap: int | None = None,
                 *, segment_color: str = 'black',
                 segmentsdefinitions_class: type[model.DigitSegmentDefinitions] = model.Digit1SegmentDefinitions):
        super().__init__(master)
        if not isinstance(digits, (int, str)):
            raise ValueError('A megjelenítendő számsorozat csak int vagy str típusú lehet.')
        elif type(digits) is str:
            if not digits.isdecimal():
                raise ValueError('A megjelenítendő karakersorozat csak decimális számjegyeket tartalmazhat.')
        self.digits = str(digits)
        self.width = width
        self.segment_height = width * 0.2 if segment_height is None else segment_height
        self.gap = width * 0.025 if gap is None else gap
        self.segment_color = segment_color
        self.segmentsdefinitions_class = segmentsdefinitions_class

        for digit in self.digits:
            one_digit = One7SegmentDigit(self, Digit7SegmentsPoints(
                segmentsdefinitions_class(self.width, self.segment_height, self.gap))).render_digit(digit)
            one_digit.config(segment_color=self.segment_color)
            one_digit.pack(side=tk.LEFT, padx=self.width*0.1)

