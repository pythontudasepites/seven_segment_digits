
from __future__ import annotations
from typing import NamedTuple
from enum import Enum

class Point(NamedTuple):
    x: int | float
    y: int | float

    def shift(self, dx, dy):
        """Olyan új ponttal tér vissza, amelynek koordinátái a self példányéhoz képest az argumentumban megadott értékkel el vannak tolva."""
        return type(self)(self.x + dx, self.y + dy)

    def reflect_about_line(self, p1: Point, p2: Point):
        """A pontnak a p1 és p2 pontok által meghatározott tengelyre vett tükörkép pontjával tér vissza.
        A tükörpont meghatározása komplex számokkal való műveletekkel valósul meg.
        """
        pc, p1c, p2c = complex(*self), complex(*p1), complex(*p2)
        ps = pc - p1c
        psi = ps.conjugate()
        psir = psi * (p2c - p1c) / (p2c - p1c).conjugate()
        p_reflected = psir + p1c
        return Point(p_reflected.real, p_reflected.imag)

# A szegemensek pozíciójának azonosítását meghatározó konstansok felsorolástípusban.
SegmentId = Enum('SegmentId', 'TOP TOP_LEFT TOP_RIGHT CENTER BOTTOM_LEFT BOTTOM_RIGHT BOTTOM')

class DigitSegmentDefinitions:
    """Egy adott felépítésű számjegy szegmenseinek leírásához a szegmenseket meghatározó pontok relatív távolságait tárolja, amelyek alapján 
    a metódussal az origóhoz képest a pontokat előállítja a szegmens szélessége és magassága alapján.
    """
    def __init__(self, segment_width, segment_height, gap):
        self.segment_width, self.segment_height = segment_width, segment_height
        self.gap = gap
        self.ssh = dict()  # Adott szegmenshez tárolja a pontok relatív távolságait.

    def get_segment_points(self, segment_id: SegmentId):
        shifts: list = self.ssh[segment_id]
        points: list = [Point(0, 0).shift(*shifts[0])]
        for dx, dy in shifts[1:]:
            points.append(points[-1].shift(dx, dy))
        return points

class Digit1SegmentDefinitions(DigitSegmentDefinitions):
    """Adott felépítésű számjegy szegmenseinek leírásához a TOP, TOP_LEFT és CENTER szegmenseket meghatározó pontok relatív távolságainak megadása."""
    def __init__(self, segment_width, segment_height, gap):
        super().__init__(segment_width, segment_height, gap)
        w, h = self.segment_width, self.segment_height
        self.ssh = {SegmentId.TOP: [(0, 0), (w, 0), (-h, +h), (-(w - 2 * h), 0)],
                   SegmentId.TOP_LEFT: [(0, 0), (h, h), (0, (w - 2 * h)), (-h / 2, h / 2), (-h / 2, -h / 2)],
                   SegmentId.CENTER: [(h / 2, h / 2), (h / 2, -h / 2), ((w - 2 * h), 0), (h / 2, h / 2), (-h / 2, +h / 2), (-(w - 2 * h), 0)]}
                                      

class Digit2SegmentDefinitions(DigitSegmentDefinitions):
    """Adott felépítésű számjegy szegmenseinek leírásához a TOP, TOP_LEFT és CENTER szegmenseket meghatározó pontok relatív távolságainak megadása."""
    def __init__(self, segment_width, segment_height, gap):
        super().__init__(segment_width, segment_height, gap)
        w, h = self.segment_width, self.segment_height
        self.ssh = {SegmentId.TOP: [(h / 2, h / 2), (h / 2, -h / 2), ((w - 2 * h), 0), (h / 2, h / 2), (-h / 2, +h / 2), (-(w - 2 * h), 0)],
                   SegmentId.TOP_LEFT: [(h / 2, h / 2), (h / 2, h / 2), (0, (w - 2 * h)), (-h / 2, h / 2), (-h / 2, -h / 2), (0, -(w - 2 * h))]}       
        self.ssh[SegmentId.CENTER] = self.ssh[SegmentId.TOP]

class Digit7SegmentsPoints:
    """A számjegy felépítése a szegmensekből"""
    def __init__(self, width, segment_definition: type[DigitSegmentDefinitions]):
        self.width = width  # A számjegy szélessége.
        self.segments: dict = {}
        
        # A szegmensek szélessége megegyezik a számjegy szélességével, a számjegy magassága a szélesség
        # választott százaléka.
        segment_width, segment_height = width, width * 0.2
        segment_def = segment_definition(segment_width, segment_height, width * 0.025)
        
        # Az egyes szegmensek számjegyen belüli pozicionálása.
        # Mivel a megtervezett számjegyek mind a magasság, mind a szélesség felezővonalra szimmetrikusak, így
        # a TOP, TOP_LEFT és CENTER szegmensekből a többi tengelyes tükrözéssel származtatható.
        s_top = segment_def.get_segment_points(SegmentId.TOP)
        s_topleft = [p.shift(0, segment_def.gap) for p in segment_def.get_segment_points(SegmentId.TOP_LEFT)]
        
        # A TOP_LEFT legalsó pontja, amihez képest a CENTER gap mértékkel lefelé el lesz tolva.
        pshift: Point = max(s_topleft, key=lambda p: p.y)
        s_center = [p.shift(0, pshift[1] - segment_height / 2).shift(0, segment_def.gap)
                    for p in segment_def.get_segment_points(SegmentId.CENTER)]

        # Vertikális tükrözési tengely két pontja, amely a felső szegmens szélességének felezővonala.
        pv1 = Point(width / 2, 0)
        pv2 = Point(width / 2, 10)

        # Horizontális tükrözési tengely két pontja, amely a középső szegmens vízszintes felezővonala.
        ph1 = min(s_center, key=lambda p: p.x)
        ph2 = max(s_center, key=lambda p: p.x)

        # A topright a topleft vertikalis tükörképe.
        s_topright = [p.reflect_about_line(pv1, pv2) for p in s_topleft]
        # A bottomleft a topleft horizontális tükörképe.
        s_bottomleft = [p.reflect_about_line(ph1, ph2) for p in s_topleft]
        # A bottomright a bottomleft vertikális tükörképe.
        s_bottomright = [p.reflect_about_line(pv1, pv2) for p in s_bottomleft]
        # A bottom a top horizontális tükörképe.
        s_bottom = [p.reflect_about_line(ph1, ph2) for p in s_top]
        
        # Létrejövő szegmensek pontjainak eltárolás.
        self.segments.update({SegmentId.TOP: s_top, SegmentId.TOP_LEFT: s_topleft, SegmentId.TOP_RIGHT: s_topright,
                              SegmentId.CENTER: s_center,
                              SegmentId.BOTTOM_LEFT: s_bottomleft, SegmentId.BOTTOM_RIGHT: s_bottomright, SegmentId.BOTTOM: s_bottom})

        # A számjegy tényleges magasságát csak a szegmenspozíciók után tudjuk meghatározni.
        self.height = max(s_bottom, key=lambda p: p.y).y


