## Snelle quiz

Beantwoord de drie vragen. Er zijn tips om je naar het juiste antwoord te leiden.

Klik na het beantwoorden van elke vraag op **Controleer mijn antwoord**.

Veel plezier!

--- question ---

---
legend: Vraag 1 van 3
---

In dit project heb je je gegevens opgeslagen in dictionaries en lijsten, inclusief een lijst met dictionaries. Als je deze lijst met dictionaries had, welke code zou je gebruiken om het aantal honden af te drukken (`print()`)?

```python
huisdieren = [
  {
    'huisdier': 'kat',
    'aantal': 9
  },
  {
    'huisdier': 'hond',
    'aantal': 4
  },
  {
    'huisdier': 'konijn',
    'aantal': 2
  }
]
```

--- choices ---

- (x)
```python
honden = huisdieren[1]
hond = honden['aantal']
print(hond)
```

  --- feedback ---
Klopt! Hiermee wordt het aantal honden afgedrukt.
--- /feedback ---

- ( )
```python
honden = huisdieren[2]
hond = honden['aantal']
print(hond)
```

  --- feedback ---
Niet helemaal! Lijstindexen beginnen bij `0`, niet bij `1`.
--- /feedback ---

- ( )
```python
honden = huisdieren['dog']
hond = honden['aantal']
print(hond)
```

  --- feedback ---
Niet precies, `huisdieren` is een lijst en getallen, (genaamd indexen) genoemd, worden gebruikt om items uit een lijst te selecteren.
--- /feedback ---

- ( )
```python
honden = huisdieren[1]
hond = honden['huisdier']
print(hond)
```

  --- feedback ---
Bijna! Dit is de verkeerde sleutel, maar in de juiste dictionary.
--- /feedback ---

--- /choices ---

--- /question ---
