# xmlconverter

###Text to XML Converter

Det ena systemet levererar ett radbaserat filformat medan det andra kräver XML. Du ska skriva en konverterare som bygger upp rätt XML-struktur.

Givet basen

> P|förnamn|efternamn
>
> T|mobilnummer|fastnätsnummer
>
> A|gata|stad|postnummer
>
> F|namn|födelseår

Där Person kan följas av Telefon, Adress och Familj
Familj kan följas av Telefon, Adress

Generera XML likt:
<people>
    <person>
        <firstname></firstname>
        <lastname></lastname>
        <address>
        </address>
        <phone>
        </phone>
        <family>
        </family>
    </person>
    <person>...</person>
</people>
