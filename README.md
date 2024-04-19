# Hétszegmenses számjegyek grafikus megjelenítése
## Karakterláncként megadott számjegyek hétszegmenses számjegyekként történő megjelenítését megvalósító grafikus elem osztály, amely a számjegyek kirajzolását a szegmenseket modellező pontok alapján végzi. 
A számjegyeket a hét szegmens pontjaival lehet meghatározni a *seven_segment_model* modulban a DigitSegmentDefinitions alosztályaként az ott látható két alosztályhoz (Digit1SegmentDefinitions és Digit2SegmentDefinitions) hasonló módon, a szegmenseket meghatározó pontok relatív távolságainak megadásával. Ehhez a jelöléseket - amik egyúttal a programban változónevek is - az alábbi ábra mutatja.

<img src="https://github.com/pythontudasepites/seven_segment_digits/blob/main/seven_segment_digits_design.jpg" width="350" height="280">

Ha a szegemensek definiálása megvan, akkor a kívánt számjegyeket a *seven_segment_digit_widget* modul Digits7Segments osztály példányosításával lehet előállítani. A számjegyek egymást követően lesznek lehelyezve az osztálypéldányban mint tkinter keretben (Frame). 
A konstruktor első, *master* argumentuma a szülő grafikus elem, amely az osztálypéldányt menedzseli. A második, *digits* argumentummal a megjelenítendő számjegyeket kell megadni karakterláncként vagy int típusú pozitív számként. A harmadik, *width* argumentum a számok szélessége pixelben, ami egyben a szegmensszélesség is. A szegmensmagasságot és a szegmensek közötti függőleges rést opcionálisan lehet megadni a *segment_height* és *gap* argumentumokkal. Ha ezek az alapértelmezett None értéken vannak, akkor egy előre beállított, a szegmensszélességhez igazodó értékeket kapnak. Ezeket követően két, csak kulcsszavas opcionális argumentumot lehet megadni. A *segment_color* a számjegy, azaz a szegmensek színének beállítására szolgál, amit a szín érvényes nevével vagy színkóddal lehet megadni. 

A Digit7Segments a szegmensek pontjai alapján rajzolja meg a számjegyeket, azaz a szegmenseket reprezentáló sokszögeket. Ehhez a Digit7Segments példányosításakor a pontokat leíró Digit7SegmentsPoints példányát kell átadni. A Digit7SegmentsPoints példány létrehozásakor kell megadni a számjegy szélességét pixelben, valamint a DigitSegmentDefinitions azon alosztályát, amely a kívánt stílusú szegmenseket definiálja. (A jelen esetben a Digit1SegmentDefinitions vagy Digit2SegmentDefinitions osztályokat.)

A *seven_segment_test_app* modul mutatja be a használatot, amellyel egy vagy több számjegyet jeleníthetünk meg, amelyek színét és méretét is előre meghatározhatjuk. Egy választógombbal pedig számjegystílust is válthatunk. Néhány eredményképet láthatunk alább.

### Képernyőképek
<img src="https://github.com/pythontudasepites/seven_segment_digits/blob/main/seven_segment_digits_screenshots_github.jpg" width="720" height="420">
