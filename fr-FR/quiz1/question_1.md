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
animaux = [
  {
    'animal': 'chat',
    'nombre': 9
  },
  {
    'animal': 'chien',
    'nombre': 4
  },
  {
    'animal': 'lapin',
    'nombre': 2
  }
]
```

--- choices ---

- (x)
```python
chiens = animaux[1]
nombre_de_chiens = chiens['nombre']
print(nombre_de_chiens)
```

  --- feedback ---
Correct ! Cela affichera le nombre de chiens.
--- /feedback ---

- ( )
```python
chiens = animaux[2]
nombre_de_chiens = chiens['nombre']
print(nombre_de_chiens)
```

  --- feedback ---
Non, pas tout à fait ! Les index de liste commencent à `0`, et pas à `1`.
--- /feedback ---

- ( )
```python
chiens = animaux['chien']
nombre_de_chiens = chiens['nombre']
print(nombre_de_chiens)
```

  --- feedback ---
Pas exactement, `animaux` est une liste et les nombres, appelés index, sont utilisés pour sélectionner les éléments dans une liste.
--- /feedback ---

- ( )
```python
chiens = animaux[1]
nombre_de_chiens = chiens['animal']
print(nombre_de_chiens)
```

  --- feedback ---
Tu es proche ! C'est la mauvaise clé, mais dans le bon dictionnaire.
--- /feedback ---

--- /choices ---

--- /question ---
