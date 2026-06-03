---
search:
  boost: 10.0
---

# Class: SE 


_Concept representing Country of Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE](https://w3id.org/lmodel/dpv/loc/SE)





```mermaid
 classDiagram
    class SE
    click SE href "../SE/"
      EEA30 <|-- SE
        click EEA30 href "../EEA30/"
      EEA31 <|-- SE
        click EEA31 href "../EEA31/"
      EU <|-- SE
        click EU href "../EU/"
      EU27 <|-- SE
        click EU27 href "../EU27/"
      EU28 <|-- SE
        click EU28 href "../EU28/"
      EEA <|-- SE
        click EEA href "../EEA/"
      

      SE <|-- SEAB
        click SEAB href "../SEAB/"
      SE <|-- SEAC
        click SEAC href "../SEAC/"
      SE <|-- SEBD
        click SEBD href "../SEBD/"
      SE <|-- SEC
        click SEC href "../SEC/"
      SE <|-- SED
        click SED href "../SED/"
      SE <|-- SEE
        click SEE href "../SEE/"
      SE <|-- SEF
        click SEF href "../SEF/"
      SE <|-- SEG
        click SEG href "../SEG/"
      SE <|-- SEH
        click SEH href "../SEH/"
      SE <|-- SEI
        click SEI href "../SEI/"
      SE <|-- SEK
        click SEK href "../SEK/"
      SE <|-- SEM
        click SEM href "../SEM/"
      SE <|-- SEN
        click SEN href "../SEN/"
      SE <|-- SEO
        click SEO href "../SEO/"
      SE <|-- SES
        click SES href "../SES/"
      SE <|-- SET
        click SET href "../SET/"
      SE <|-- SEU
        click SEU href "../SEU/"
      SE <|-- SEW
        click SEW href "../SEW/"
      SE <|-- SEX
        click SEX href "../SEX/"
      SE <|-- SEY
        click SEY href "../SEY/"
      SE <|-- SEZ
        click SEZ href "../SEZ/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **SE** [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * [SEAB](SEAB.md)
        * [SEAC](SEAC.md)
        * [SEBD](SEBD.md)
        * [SEC](SEC.md)
        * [SED](SED.md)
        * [SEE](SEE.md)
        * [SEF](SEF.md)
        * [SEG](SEG.md)
        * [SEH](SEH.md)
        * [SEI](SEI.md)
        * [SEK](SEK.md)
        * [SEM](SEM.md)
        * [SEN](SEN.md)
        * [SEO](SEO.md)
        * [SES](SES.md)
        * [SET](SET.md)
        * [SEU](SEU.md)
        * [SEW](SEW.md)
        * [SEX](SEX.md)
        * [SEY](SEY.md)
        * [SEZ](SEZ.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE](https://w3id.org/lmodel/dpv/loc/SE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Sweden




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE |
| native | loc:SE |
| exact | dpv_loc:SE, dpv_loc_owl:SE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Sweden
exact_mappings:
- dpv_loc:SE
- dpv_loc_owl:SE
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:SE

```
</details>

### Induced

<details>
```yaml
name: SE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Sweden
exact_mappings:
- dpv_loc:SE
- dpv_loc_owl:SE
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:SE

```
</details></div>