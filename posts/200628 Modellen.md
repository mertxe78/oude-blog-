# Kernconcepten van data science: modellen

Een kernconcept binnen data science en analytics zijn modellen. Of je nou iets leest over data analytics, data science of artifical intelligence; het model speelt een centrale rol. Zonder goed begrip van wat nu precies bedoelt wordt met een model, voelt de toepassing als een *black box*. Om beter te kunnen doorgronden welk onderliggende mechanisme van toepassing is helpt het enorm om de definitie, technieken en doeleinden omtrent modelleren scherp te hebben.

## Definitie

Een model is te defineren als ***een versimpele weergave van de werkelijkheid, ten behoeve van een vooraf gespecificeerd doel***. Niets meer, niets minder.

Deze versimpeling vindt plaats op basis van assumpties over wat wel en wat niet belangrijk is voor betreffende toepassing. Een model abstraheert details die niet van belang zijn, en behoudt datgene wa wel van belang is.

## Voorbeelden van modellen

* Een routekaart is een weergave van de wereld,  met als doel om navigeren te vereenvoudigen
* Een marquette is een versimpele weergave van bouwproject, met als doel om een beeld te krijgen bij de vormgeving
* Een conceptueel model relateert verschillende concepten op een hoger niveau aan elkaar om de werking van een complex systeem te representeren

## Technieken om te modelleren

* **Statistisch modelleren**: modeleren waarbij begrip van relaties van belang is. Omvat hypothesevorming vooraf; welke variabele beïnvloedt wat? Wat zijn de verbanden? Uiteindelijke model valideert deze hypothese.
* **Machine learning**: modeleren waarbij begrip van relaties tussen variablen niet van belang is, en het gaat om een zo goed mogelijke voorspelling van de target variabele te doen. Geen hypothesevorming. "Leert" zelf patronen in de data; training en validatie van split in data (train- en testset).

## Doeleinden

Het maken van modellen is veelal onder te verdelen in verschillende doeleinden.

* **Descriptieve modellen**: begrip opdoen van een bestaand fenomeen
* **Voorspelmodellen** (predictive model): zo goed mogelijk benaderen van een vooraf gespecificeerde target variabele. een formule om een bepaalde waarde van keuze te benaderen. Die formule kan wiskundig zijn, of een logical statement zoals een business rule.

## Eigenschappen modellen

* Een model is altijd een versimpelde, en dus inherent onjuiste, weergave van de werkelijkheid
* In het geval van machine learning is een model verouderd op het moment dat het in gebruik wordt genomen; omdat historische data anders zal zijn dan data van de huidige realiteit

> "All models are wrong but some are useful."
> -- George E.P. Box
