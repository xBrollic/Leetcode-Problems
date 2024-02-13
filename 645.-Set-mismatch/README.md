# 645 - Set mismatch

## Beskrivning av problemet:

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

## Metod 1

### Kod:
```python
result = []
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] and nums[0] == 1 and nums[i]-nums[i-1] <= 1:
            result.append(nums[i])
            result.append(nums[i]+1)
        if nums[i] == nums[i+1] and nums[0] == 1 and nums[i]-nums[i-1] > 1:
            result.append(nums[i])
            result.append(nums[i]-1)
        if nums[i] == nums[i+1] and nums[0]!=1:
            result.append(nums[i])
            result.append(nums[i]-1)
    return result
```
1. Sorterar listan så siffrorna är eskalerande
2. Kollar först igenom om en siffra framför är densamma, första siffran i listan är 1 och om distansen mellan siffran är 1. `nums[i]` blir då siffran som är duppletten och `nums[i]+1` blir då siffran som saknas.
3. Kollar igenom listan igen, men villkoren ändras. Om distansen mellan siffrorna är mer än 1 så blir duppletten densamma, men andra outputen blir `nums[i]-1`

### Kritik för metod 1

Väldigt ofaktoriserad kod och kollar igenom för många gånger. Borde istället kolla igenom listan och jämföra den med en korrekt lista. Ex
`[1,2,2,4]` (Inkorrekt) med `[1,2,3,4]` (Korrekt).

## Metod 2

### Kod:
```python
def findErrorNums(self, nums: list[int]) -> list[int]:
    nums.sort()
    dupe = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i != j:
                dupe = nums[i]
    for i in range(len(nums)):
        if i+1 != nums[i]:
            return [dupe, i+1]
```

1. Sortera listan, skapar en variabel `dupe` som kommer innehålla dupletter.
2. Loopar igenom listan två gånger `[i][j]` och jämför alla siffror med varandra, om den hittar två av en siffra så läggs siffran i `dupe` variabeln.
3. Loopar igenom listan igen och jämför den med den korrekta listan. När den itererar igenom listan så kollar den om `i+1` är olikt med `nums[i]`, vilket då den kommer returnera en ny lista med `dupe` och `i+1`, vilket är dupletten och siffran som borde vara där egentligen.

### Kritik för metod 2

Koden fungerar bra, men i ett edge case t.ex: `[1,5,3,2,2,7,6,4,8,9]` så sorteras den först genom till `[1,2,2,3,4,5,6,7,8,9]` vilket då duppletten förflyttar hela restan av siffrorna, vilket i detta fall är det 10 som saknas och 10 blev bytt med 2. En En alternativ metod skulle kunna vara att använda `set()` funktionen, vilket skapar ett set, som tar bort duppletter, och sorterar listan. Sedan använder `list()` och gör om den till en lista. Sen loopar jag igenom den listan med en korrekt lista med längden av ursprungslistan, vilket sen returnerar siffran om den inte är lika med den nya listan. 