# Hétszegmenses számjegyek grafikus megjelenítése
## Karakterláncként megadott számjegyek hétszegmenses számjegyekként történő megjelenítését megvalósító grafikus elem osztály, amely a számjegyek kirajzolását a szegmenseket modellező pontok alapján végzi. 
A számjegyeket a hét szegmens pontjaival lehet meghatározni a *seven_segment_model* modulban a DigitSegmentDefinitions alosztályaként az ott látható két alosztályhoz (Digit1SegmentDefinitions és Digit2SegmentDefinitions) hasonló módon, a szegmenseket meghatározó pontok relatív távolságainak megadásával. A hét szegmensnek vízszintesen és függőlegesen szimmetrikusnak kell lenni. A szegmensek tervezéséhez a jelöléseket - amik egyúttal a programban változónevek is - az alábbi ábra mutatja.

<img src="https://github.com/pythontudasepites/seven_segment_digits/blob/main/seven_segment_digits_design.jpg" width="350" height="280">

Ha a szegmensek definiálása megvan, akkor a kívánt számjegyeket a *seven_segment_digit_widget* modul Digits7Segments osztály példányosításával lehet előállítani. A számjegyek egymást követően lesznek lehelyezve az osztálypéldányban mint tkinter keretben (Frame). 
A konstruktor első, *master* argumentuma a szülő grafikus elem, amely az osztálypéldányt menedzseli. A második, *digits* argumentummal a megjelenítendő számjegyeket kell megadni karakterláncként vagy int típusú pozitív számként. A harmadik, *width* argumentum a számok szélessége pixelben, ami egyben a szegmensszélesség is. A szegmensmagasságot és a szegmensek közötti függőleges rést opcionálisan lehet megadni a *segment_height* és *gap* argumentumokkal. Ha ezek az alapértelmezett None értéken vannak, akkor egy előre beállított, a szegmensszélességhez igazodó értékeket kapnak. Ezeket követően két, csak kulcsszavas opcionális argumentumot lehet megadni. A *segment_color* a számjegy, azaz a szegmensek színének beállítására szolgál, amit a szín érvényes nevével vagy színkóddal lehet megadni. 
A Digits7Segments a szegmensek pontjai alapján rajzolja meg a számjegyeket, azaz a szegmenseket reprezentáló sokszögeket. Ehhez a Digits7Segments példányosításakor a szegmenseket leíró valamely DigitSegmentDefinitions alosztályt kell megadni az opcionális *segmentsdefinitions_class* argumentummal, amelynek alapértelmezett értéke a *seven_segment_model* modul Digit1SegmentDefinitions osztálya.

A *seven_segment_digit_widget* modul One7SegmentDigit osztálya alapvetően egy segédosztály, de önállóan is alkalmazható, ha csak egyetlen számjegyet akarunk létrehozni. 

A *seven_segment_test_app* modul mutatja be a használatot, amellyel meghatározhatjuk a megjelenítendő számjegyeket, azok színét és méretét, valamint egy választógombbal a számjegyek formáját, stílusát váltogathatjuk. Néhány eredményképet alább láthatunk.
A program Python 3.10+ alatt fut.

Ami a gyakorlati alkalmazást illeti, a Digits7Segments osztály olyankor lehet hasznos, ha valamilyen digitális kijelzővel rendelkező készüléket vagy eszközt (pl. digitális óra, LCD kijelzős számológép, műszer stb.) akarunk programmal modellezni.

### Képernyőképek
<img src="https://github.com/pythontudasepites/seven_segment_digits/blob/main/seven_segment_digits_screenshots_github.jpg" width="720" height="420">
