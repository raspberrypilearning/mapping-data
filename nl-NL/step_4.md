## Je gegevens markeren

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Toon je gegevens op de kaart en maak deze interactief.
</div>
<div>
![Een kaart met veel spelden. Informatie wordt weergegeven in de tekstuitvoer voor sommige spelden.](images/map_many_pins.png){:width="300px"}
</div>
</div>

Voordat je spelden op de kaart kunt zetten voor elke plaats die je gegevens hebt, moet je weten waar die plaatsen zijn. Het startersproject bevat code om je deze locaties te geven.

Je kunt de `haal_regio_coordinaten()` functie gebruiken om een dictionary met de coördinaten voor een regio terug te geven. Bijvoorbeeld `haal_regio_coordinaten('Japan')` zal `{'x': 880.151122422, 'y': 278.639809465}` retourneren.

--- task ---

Definieer een `teken_data()` functie om je gegevens op de kaart te plaatsen. Eerst kun je gewoon de naam van de regio en de `x` en `y` coördinaten afdrukken.

Het zou door je `regio_lijst` moeten lopen en een lijn voor elke regio moeten afdrukken.

--- code ---
---
language: python
filename: main.py teken_gegevens()
---
def teken_gegevens():
    for regio in regio_lijst:
        regio_naam = regio['regio'] # Haal de naam van de regio op
        regio_coordinaten = haal_regio_coordinaten(regio_naam) # Gebruik de naam om coördinaten te krijgen
        regio_x = regio_coordinaten['x'] # Verkrijg het x-coördinaat
        regio_y = regio_coordinaten['y'] # Verkrijg het y-coördinaat
        print(regio_naam, regio_x, regio_y)

--- /code ---

--- /task ---

--- task ---

Maak in je `setup()` functie een comment van je `teken_speld()` code en roep in plaats daarvan `teken_data()` aan.

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: false
line_number_start: 
line_highlights: 12-13
---
def setup():
    # Zet de code om eenmalig uit te voeren hieronder
    size(991, 768)
    image(
        kaart, # De afbeelding die wordt getekend
        0, # De x van de linkerbovenhoek
        0, # De y van de linkerbovenhoek
        width, # De breedte van de afbeelding
        height # De hoogte van de afbeelding
    )
    # teken_speld(300, 300, Color(255,0,0))
    teken_gegevens()
  
--- /code ---

--- /task ---

--- task ---

In plaats van de naam van de regio en de coördinaten af te drukken, je kan je `teken_speld()` functie gebruiken om je spelden op de kaart te plaatsen. De onderstaande code geeft de spelden een rode kleur (`Color(255, 0, 9)`), maar je kunt ook een andere kleur kiezen.

--- code ---
---
language: python
filename: main.py teken_gegevens()
line_numbers: false
line_number_start: 
line_highlights: 7-9
---
def teken_gegevens():
    for regio in regio_lijst:
        regio_naam = regio['regio'] # Haal de naam van de regio op 
        regio_coordinaten = haal_regio_coordinaten(regio_naam) # Gebruik de naam om coördinaten te krijgen
        regio_x = regio_coordinaten['x'] # Verkrijg het x-coördinaat
        regio_y = regio_coordinaten['y'] # Verkrijg het y-coördinaat
        #print(regio_naam, regio_x, regio_y)
        regio_kleur = Color(255, 0, 0) # Stel de speld kleur in 
        teken_speld(regio_x, regio_y, regio_kleur) # Teken de speld

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je programma uit. Er zouden veel spelden op je kaart moeten verschijnen! Afhankelijk van de gegevens die je hebt gekozen, zie je mogelijk meer of minder spelden dan in de onderstaande afbeelding.

![Een zwart wit kaart met veel rode stippen erop.](images/map_many_pins.png)

--- /task ---

Vervolgens moet je wat code toevoegen om gebruikers op een speld te laten klikken en wat informatie te zien krijgen. Om dit te doen, moet elke speld een andere kleur hebben, en je hebt een manier nodig om die kleuren aan de juiste gegevens te koppelen.

--- task ---

**Kies:** Elke speld heeft een unieke kleur nodig. Maar er zijn veel verschillende manieren om dit mogelijk te maken. Hier zijn een paar suggesties, maar je kunt er zelf een maken.

--- collapse ---
---
title: Wijzig de waarde van één kleur
---
Dit voorbeeld verandert de waarde voor het rood wanneer de code een speld plaatst:

--- code ---
---
language: python
filename: main.py teken_gegevens()
line_numbers: false
line_number_start: 
line_highlights: 2, 9, 11
---
def teken_gegevens():
    rood_waarde = 255 # Stel een startwaarde voor rood in

    for regio in regio_lijst:
        regio_naam = regio['naam']
        regio_coordinaten = haal_regio_coordinaten(regio_naam)
        regio_x = regio_coordinaten['x']
        regio_y = regio_coordinaten['y']
        regio_kleur = Color(rood_waarde, 0, 0) # Gebruik de rode waarde in de kleur
        teken_speld(regio_x, regio_y, regio_kleur)
        rood_waarde -= 1 # Wijzig de roodwaarde

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Wijzig de waarde van meerdere kleuren
---
In dit voorbeeld worden de rode, groene en blauwe waarden gewijzigd telkens wanneer de code een speld plaatst:

--- code ---
---
language: python
filename: main.py — teken_gegevens()
line_numbers: false
line_number_start: 
line_highlights: 2-4, 10, 12-14
---
def teken_gegevens():
    rood_waarde = 255 # Stel een startwaarde voor rood in
    blauw_waarde = 0
    groen_waarde = 255
    for regio in regio_lijst:
        regio_naam = regio['regio']
        regio_coordinaten = haal_regio_coordinaten(regio_naam)
        regio_x = regio_coordinaten['x']
        regio_y = regio_coordinaten['y']
        regio_kleur = Color(rood_waarde, groen_waarde, blauw_waarde) # Gebruik alle kleuren
        teken_speld(regio_x, regio_y, regio_kleur)
        rood_waarde -= 1 # Wijzig de roodwaarde
        groen_waarde += 1 # Wijzig de groenwaarde
        blauw_waarde -= 1 # Wijzig de blauwwaarde

--- /code ---

--- /collapse ---

--- collapse ---
---
title: Kies willekeurige kleuren
---

Bovenaan je code, bij je andere imports moet je ook `randint` importeren uit de `random` library.

Je kunt dan een willekeurige kleur kiezen voor jouw regio kleuren; een andere kleur zal worden gekozen telkens wanneer de `for` lus wordt uitgevoerd. Er is een kans dat twee of meer kleuren hetzelfde zijn, maar deze kans is zeer klein.

**Waarschuwing:** Elke keer dat de kaart wordt getekend, wordt er een nieuwe kleur gekozen, zodat je spelden gaan knipperen.

--- code ---
---
language: python
filename: main.py — teken_gegevens()
line_numbers: false
line_number_start:
line_highlights: 1, 9
---
from random import randint

def teken_gegevens():
    for regio in regio_lijst:
        regio_naam = regio['naam']
        regio_coordinaten = haal_regio_coordinaten(regio_naam)
        regio_x = regio_coordinaten['x']
        regio_y = regio_coordinaten['y']
        regio_kleur = Color(randint(0,255), randint(0,255), randint(0,255)) # Selecteer een willekeurige kleur
        teken_speld(regio_x, regio_y, regio_kleur)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Test:** Voer je programma uit en controleer of de spelden verschillende kleuren hebben. Als je niet veel spelden hebt, kan het moeilijk te achterhalen zijn. Probeer in dat geval grotere veranderingen tussen elke speld te gebruiken.

--- /task ---

Je kaart heeft unieke spelden voor elke locatie, maar je moet wat code toevoegen om deze spelden te koppelen aan de informatie die je gebruikers wilt laten zien.

--- task ---

Om de kleur van de pin te gebruiken om de informatie op te zoeken, moet je **een dictionary maken** om de kleuren op te slaan en deze aan de regio te koppelen.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 7
---
#!/bin/python3
from p5 import *
from regions import haal_regio_coordinaten
from random import randint

regio_lijst = []
kleuren = {}
--- /code ---

--- /task ---

--- task ---

Terwijl de spelden worden geplaatst, kan de `regio` samen met de kleur van de spelden in de dictionary worden opgeslagen.

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 9
---
def teken_gegevens():
    rood_waarde = 255
    for regio in regio_lijst:
        regio_naam = regio['regio'] # Haal de naam van de regio op
        regio_coordinaten = haal_regio_coordinaten(regio_naam) # Gebruik de naam om coördinaten te krijgen
        regio_x = regio_coordinaten['x'] # Verkrijg het x-coördinaat
        regio_y = regio_coordinaten['y'] # Verkrijg het y-coördinaat
        regio_kleur = Color(rood_waarde, 100, 0) # Stel de speld kleur in
        kleuren[regio_kleur.hex] = regio
        teken_speld(regio_x, regio_y, regio_kleur)
        rood_waarde -= 1
--- /code ---

--- /task ---

Wanneer de gebruiker op een speld klikt, wordt de hexadecimale kleurwaarde van de speld opgehaald en vervolgens wordt de overeenkomstige regio in de dictionary gezocht.

--- task ---

In je `muis_geklikt()` functie zoek je de `pixel_kleur` in de `kleuren` dictionary en print de `regio`.

**Onthoud** dat `kleuren` een dictionary met dictionaries is. Je moet de dictionary van regionale informatie krijgen en dan de informatie uit deze dictionary ophalen. Bijvoorbeeld:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 4-5
---
def mouse_pressed():
    # Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex
    feiten = kleuren[pixel_kleur]
    print(feiten['regio'])
--- /code ---

--- /task ---

--- task ---

Het is belangrijk om te controleren of een sleutel in een dictionary staat. Als je op een gebied zonder speld op de kaart klikt, ontvang je een `KeyError`.

Je kunt controleren of een waarde in een dictionary staat door `in` te gebruiken:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 4-8
---
def mouse_pressed():
    # Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex
    if pixel_kleur in kleuren:
        feiten = kleuren[pixel_kleur]
        print(feiten['regio'])
    else:
        print('Regio niet gedetecteerd')
--- /code ---

--- /task ---

--- task ---

**Test:** Voer je programma uit. Klik op een speld en controleer of jouw programma de gegevens over dat gebied correct afdrukt.

--- /task ---

--- task ---

Je kunt andere feiten printen over de regio waarop je hebt geklikt door meer `print()` opdrachten toe te voegen. Dit is afhankelijk van de dataset die je gebruikt. Als je bijvoorbeeld `happy.csv` hebt gebruikt, kun je het volgende afdrukken:

--- code ---
---
language: python
filename: main.py
line_numbers: false
line_number_start: 
line_highlights: 7-8
---
def mouse_pressed():
    # Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex
    if pixel_kleur in kleuren:
        feiten = kleuren[pixel_kleur]
        print(feiten['regio'])
        print(feiten['rangorde_geluk'])  # Je eerste data feit
        print(feiten['geluk_score'])  # Je tweede data feit
    else:
        print('Regio niet gedetecteerd')
--- /code ---

--- /task ---

--- task ---

**Fouten opsporen:** Mogelijk vind je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

--- collapse ---
---
title: Mijn spelden verschijnen niet op de kaart
---

Als je spelden niet op de kaart verschijnen, controleer dan of je je `teken_data()` functie aanroept vanuit je `setup()` functie.

--- /collapse ---

--- collapse ---
---
title: Ik krijg een melding over een 'KeyError'
---

Als je een bericht over 'KeyError' krijgt controleer of de spelling van je dictionary sleutels overeenstemt met waardes wanneer je ze uitleest. Of de letters HOOFDLETTERS of kleine letters zijn, is ook belangrijk.

Als de fout betrekking heeft op het dictionary `kleuren`, controleer dan of de sleutel bestaat in `kleuren` voordat je probeert de waarde op te halen.

--- /collapse ---

--- collapse ---
---
title: Er wordt steeds 'Regio niet gedetecteerd' weergegeven
---

Je muisklik moet in het midden van je speld staan om ervoor te zorgen dat de juiste kleur wordt gedetecteerd.

Probeer dichter bij het midden van je speld te klikken.

--- /collapse ---

--- /task ---

--- save ---
