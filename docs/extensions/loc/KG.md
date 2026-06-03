---
search:
  boost: 10.0
---

# Class: KG 


_Concept representing Country of Kyrgyzstan_



<div data-search-exclude markdown="1">



URI: [loc:KG](https://w3id.org/lmodel/dpv/loc/KG)





```mermaid
 classDiagram
    class KG
    click KG href "../KG/"
      KG <|-- KGB
        click KGB href "../KGB/"
      KG <|-- KGC
        click KGC href "../KGC/"
      KG <|-- KGGB
        click KGGB href "../KGGB/"
      KG <|-- KGGO
        click KGGO href "../KGGO/"
      KG <|-- KGJ
        click KGJ href "../KGJ/"
      KG <|-- KGN
        click KGN href "../KGN/"
      KG <|-- KGO
        click KGO href "../KGO/"
      KG <|-- KGT
        click KGT href "../KGT/"
      KG <|-- KGY
        click KGY href "../KGY/"
      
      
```





## Inheritance
* **KG**
    * [KGB](KGB.md)
    * [KGC](KGC.md)
    * [KGGB](KGGB.md)
    * [KGGO](KGGO.md)
    * [KGJ](KGJ.md)
    * [KGN](KGN.md)
    * [KGO](KGO.md)
    * [KGT](KGT.md)
    * [KGY](KGY.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:KG](https://w3id.org/lmodel/dpv/loc/KG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Kyrgyzstan




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#KG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:KG |
| native | loc:KG |
| exact | dpv_loc:KG, dpv_loc_owl:KG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: KG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#KG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Kyrgyzstan
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Kyrgyzstan
exact_mappings:
- dpv_loc:KG
- dpv_loc_owl:KG
class_uri: loc:KG

```
</details>

### Induced

<details>
```yaml
name: KG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#KG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Kyrgyzstan
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Kyrgyzstan
exact_mappings:
- dpv_loc:KG
- dpv_loc_owl:KG
class_uri: loc:KG

```
</details></div>