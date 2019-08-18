# Fraction To Text

a light tool for coverting fraction to english text which can use in your text normalization code.

## Quick Start

### Git Clone Repo

git clone this repo to the root directory of your project which need to use it.

```
cd /path/to/proj
git clone https://github.com/Joee1995/fraction_to_text.git
```

after that, your doc tree should be:

```
proj                        # root of your project
|--- fraction_to_text       # this fraction-to-text tool
     |--- FractionToText.py
     |--- ...
|--- text_normalize.py      # your text normalization code
|--- ...
```

### How to Use ?

```
# text_normalize.py
from fraction_to_text.FractionToText import FractionToText

ftt = FractionToText()
print(ftt.covert(number='1/2'))
print(ftt.covert(number='5/7'))
print(ftt.covert(number='32 17/129'))
```

## Reference

thinks to [cornellsteven/fractions-to-words](<https://github.com/cornellsteven/fractions-to-words>) .

