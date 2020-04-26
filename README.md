# xmlconverter

## Text to XML Converter



Denna konverterare tar emot en textfil från ett gammalt utomstående system och skriver om denna fil till XML.

Givet basen

> P|förnamn|efternamn
>
> T|mobilnummer|fastnätsnummer
>
> A|gata|stad|postnummer
>
> F|namn|födelseår

Där Person kan följas av Telefon, Adress och Familj<br>

Familj kan följas av Telefon, Adress

Generera XML likt:<br>

<code>
    <people>
        <person>
            <firstname></firstname>
            <lastname></lastname>
            <address>
            </address>
            <phone>
            </phone>
            <family>
                <name>..</name>
                <born>..</born>
            </family>
        </person>
        <person>...</person>
    </people>
</code>
