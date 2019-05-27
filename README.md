
## Arabic Pronounce

This project is based on Dr. Nawar Halabi's work https://github.com/nawarhalabi/Arabic-Phonetiser. I am almost exaclty using the same code with just removing unneeded stuff and changing the format of the final output.

## Usage
```python
from arabic_pronounce import phonetise

phonetise("كلمةٌ")
>>> ['k l m t u1 n']
```

## Test
python -m pytest
