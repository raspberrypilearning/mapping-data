
--- question ---

---
legend: Vraag 2 van 3
---

Je hebt functies met parameters gebruikt om jouw gegevens te laden en je kaartspelden te maken. Welke van deze functies zou twee getallen als parameters accepteren, deze vermenigvuldigen en het resultaat afdrukken?

--- choices ---

- ( )
```python
def mijn_functie():
  a = 5
  b = 3
  resultaat = a * b
  print(resultaat)
```

  --- feedback ---
Niet helemaal! Deze functie vermenigvuldigt wel twee getallen, maar het zijn altijd dezelfde getallen. De parameters laten je dezelfde code gebruiken op verschillende inputs.
--- /feedback ---

- ( )
```python
def mijn_functie(a, b):
  print(10)
```

  --- feedback ---
Niet helemaal. Deze functie accepteert twee parameters, maar gebruikt ze nergens voor. De functie drukt `10` af, ongeacht welke invoer deze ontvangt.
--- /feedback ---

- ( )
```python
def mijn_functie():
  resultaat = a * b
  print(resultaat)
```

  --- feedback ---
Bijna. Deze functie werkt met `a` en `b` alsof het parameters zijn. Maar ze worden nooit daadwerkelijk ingesteld als parameters voor de functie.
--- /feedback ---

- (x)
```python
def mijn_functie(a, b):
  resultaat = a * b
  print(resultaat)
```

  --- feedback ---
Dat klopt! Deze functie neemt `a` en `b` als parameters, vermenigvuldigt deze en drukt het resultaat af.
--- /feedback ---

--- /choices ---

--- /question ---
