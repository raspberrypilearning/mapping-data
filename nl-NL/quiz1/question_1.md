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
pets = [
  {
    'pet': 'cat',
    'count': 9
  },
  {
    'pet': 'dog',
    'count': 4
  },
  {
    'pet': 'rabbit',
    'count': 2
  }
]
```

--- choices ---

- (x)
```python
dogs = pets[1]
dogs_count = dogs['count']
print(dogs_count)
```

  --- feedback --- Klopt! Hiermee wordt het aantal honden afgedrukt. --- /feedback ---

- ( )
```python
dogs = pets[2]
dogs_count = dogs['count']
print(dogs_count)
```

  --- feedback --- Niet helemaal! Lijstindexen beginnen bij `0`, niet bij `1`. --- /feedback ---

- ( )
```python
dogs = pets['dog']
dogs_count = dogs['count']
print(dogs_count)
```

  --- feedback --- Niet precies, `huisdieren` is een lijst en getallen, (genaamd indexen) genoemd, worden gebruikt om items uit een lijst te selecteren. --- /feedback ---

- ( )
```python
dogs = pets[1]
dogs_count = dogs['pet']
print(dogs_count)
```

  --- feedback --- Bijna! Dit is de verkeerde sleutel, maar in de juiste dictionary. --- /feedback ---

--- /choices ---

--- /question ---
