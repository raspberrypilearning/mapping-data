## Questionnaire rapide

Réponds aux trois questions. Il y a des indices pour te guider vers la bonne réponse.

Lorsque tu as répondu à chaque question, clique sur **Vérifier ma réponse**.

Amuse-toi bien !

--- question ---

---
legend: Question 1 sur 3
---

Dans ce projet, tu as stocké tes données dans des dictionnaires et des listes, y compris une liste de dictionnaires. Si tu avais cette liste de dictionnaires, quel code utiliserais-tu pour `print()` le nombre de chiens ?

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

  --- feedback --- Correct ! Cela affichera le nombre de chiens. --- /feedback ---

- ( )
```python
dogs = pets[2]
dogs_count = dogs['count']
print(dogs_count)
```

  --- feedback --- Non, pas tout à fait ! Les index de liste commencent à `0`, et pas à `1`. --- /feedback ---

- ( )
```python
dogs = pets['dog']
dogs_count = dogs['count']
print(dogs_count)
```

  --- feedback --- Pas exactement, `pets` est une liste et les nombres, appelés index, sont utilisés pour sélectionner les éléments dans une liste. --- /feedback ---

- ( )
```python
dogs = pets[1]
dogs_count = dogs['pet']
print(dogs_count)
```

  --- feedback --- Tu es proche ! C'est la mauvaise clé, mais dans le bon dictionnaire. --- /feedback ---

--- /choices ---

--- /question ---
