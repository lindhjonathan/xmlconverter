# xmlconverter

## Text to XML Converter description

Denna konverterare tar emot en textfil från ett gammalt utomstående system och skriver om denna fil till XML.

Givet basen av en textfil likt:

> P|förnamn|efternamn
>
> T|mobilnummer|fastnätsnummer
>
> A|gata|stad|postnummer
>
> F|namn|födelseår

Där Person kan följas av Telefon, Adress och Familj<br>

Familj kan följas av Telefon, Adress

Generera XML likt:

```
> <people>
>     <person>
>         <firstname></firstname>
>         <lastname></lastname>
>         <address>
>         </address>
>         <phone>
>         </phone>
>         <family>
>             <name>..</name>
>             <born>..</born>
>         </family>
>     </person>
>     <person>...</person>
> </people>
```

## Dependencies

This converter script runs in a python 3.6.9 environment
The script assumes the base text file to convert to be named 'to_transform.txt'

## Installation

1. Clone or download this repository
2. Move to directory ../xmlconverter
3. Run by typing 'python3 transformer.py'
4. On success, an XML file will be generated in the current folder called 'transformed.xml'
