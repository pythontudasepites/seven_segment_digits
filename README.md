# Hétszegmenses számjegyek grafikus megjelenítése
## Karakterláncként megadott számjegyek hétszegmenses számjegyekként történő megjelenítését megvalósító grafikus elem (widget), amely a számjegyek kirajzolását a szegmenseket modellező pontok alapján végzi. Különböző számjegystílusokat lehet definiálni az egyes szegmensek pontjainak meghatározásával. 
A számjegyeket a hét szegmens pontjaival lehet meghatározni a *seven_segment_model* modulban a DigitSegmentDefinitions alosztályaként az ott látható két alosztályhoz (Digit1SegmentDefinitions és Digit2SegmentDefinitions) hasonló módon a szegmenseket meghatározó pontok relatív távolságainak megadásával. Ehhez a jelöléseket - amik egyúttal a változónevek is - a mellékelt 1. ábra mutatja.

<img src="https://github.com/pythontudasepites/seven_segment_digits/blob/main/seven_segment_digits_design.jpg" width="492" height="400">

Ha a szegemensek definiálása megvan, akkor a kívánt számjegyeket a *seven_segment_digit_widget* modul Digit7Segments osztály példányának render_digits() metódusa rajzolja meg és helyezi el egymást követően egy tkinter keretben (Frame). A render_digits() metódus első argumentuma a megjelenítendő számjegyek karakterláncként megadva; a második opcionális argumentummal a szegmensek színe határozható meg a szín érvényes nevével vagy színkóddal.

A Digit7Segments a szegmensek pontjai alapján rajzolja meg a számjegyeket, azaz a szegmenseket reprezentáló sokszögeket. Ehhez a Digit7Segments példányosításakor a pontokat leíró Digit7SegmentsPoints példányát kell átadni. A Digit7SegmentsPoints példány létrehozásakor kell megadni a számjegy szélességét pixelben, valamint a DigitSegmentDefinitions azon alosztályát, amely a kívánt stílusú szegmenseket definiálja. (A jelen esetben a Digit1SegmentDefinitions vagy Digit2SegmentDefinitions osztályokat.)

A *seven_segment_test_app* modul mutatja be a használatot, amellyel egy vagy több számjegyet jeleníthetünk meg, amelyek színét és méretét is előre meghatározhatjuk. Egy választógombbal pedig számjegystílust is válthatunk. Néhány eredményképet láthatunk alább:

### Képernyőképek
<img src="https://github.com/pythontudasepites/seven_segment_digits/blob/main/seven_segment_digits_screenshots_github.jpg" width="818" height="480">
