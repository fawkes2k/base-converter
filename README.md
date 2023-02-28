# Base converter
Convert between positional numeral system in given base and decimal

Example:
```
>>> from base_converter import BaseConverter
>>> seximal = BaseConverter('012345')
>>> seximal.decimal_to_base(2022)
'13210'
>>> seximal.base_to_decimal('4424')
1024
```
