
--- question ---

---
legend: Question 2 sur 3
---

Tu as utilisé des fonctions avec des paramètres pour charger tes données et créer tes repères de carte. Laquelle de ces fonctions accepterait deux nombres comme paramètres, les multiplierait et imprimerait le résultat ?

--- choices ---

- ( )
```python
def ma_fonction():
  a = 5
  b = 3
  resultat = a * b
  print(resultat)
```

  --- feedback ---
Pas tout à fait ! Cette fonction multiplie deux nombres, mais ce sont toujours les mêmes nombres. Les paramètres te permettent d'utiliser le même code sur différentes entrées.
--- /feedback ---

- ( )
```python
def ma_fonction(a, b):
  print(10)
```

  --- feedback ---
Pas exactement. Cette fonction accepte deux paramètres, mais elle ne les utilise pas. La fonction affiche `10` peu importe la saisie qu'elle reçoit.
--- /feedback ---

- ( )
```python
def ma_fonction():
  resultat = a * b
  print(resultat)
```

  --- feedback ---
Tu es proche. Cette fonction fonctionne avec `a` et `b` comme s'il s'agissait de paramètres. Mais ils ne sont jamais réellement définis comme paramètres de la fonction.
--- /feedback ---

- (x)
```python
def ma_fonction(a, b):
  resultat = a * b
  print(resultat)
```

  --- feedback ---
C'est correct ! Cette fonction prend `a` et `b` comme paramètres, les multiplie et imprime le résultat.
--- /feedback ---

--- /choices ---

--- /question ---
