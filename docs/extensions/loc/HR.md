---
search:
  boost: 10.0
---

# Class: HR 


_Concept representing Country of Croatia_



<div data-search-exclude markdown="1">



URI: [loc:HR](https://w3id.org/lmodel/dpv/loc/HR)





```mermaid
 classDiagram
    class HR
    click HR href "../HR/"
      EEA30 <|-- HR
        click EEA30 href "../EEA30/"
      EEA31 <|-- HR
        click EEA31 href "../EEA31/"
      EU <|-- HR
        click EU href "../EU/"
      EU27 <|-- HR
        click EU27 href "../EU27/"
      EU28 <|-- HR
        click EU28 href "../EU28/"
      EEA <|-- HR
        click EEA href "../EEA/"
      

      HR <|-- HR01
        click HR01 href "../HR01/"
      HR <|-- HR02
        click HR02 href "../HR02/"
      HR <|-- HR03
        click HR03 href "../HR03/"
      HR <|-- HR04
        click HR04 href "../HR04/"
      HR <|-- HR05
        click HR05 href "../HR05/"
      HR <|-- HR06
        click HR06 href "../HR06/"
      HR <|-- HR07
        click HR07 href "../HR07/"
      HR <|-- HR08
        click HR08 href "../HR08/"
      HR <|-- HR09
        click HR09 href "../HR09/"
      HR <|-- HR10
        click HR10 href "../HR10/"
      HR <|-- HR11
        click HR11 href "../HR11/"
      HR <|-- HR12
        click HR12 href "../HR12/"
      HR <|-- HR13
        click HR13 href "../HR13/"
      HR <|-- HR14
        click HR14 href "../HR14/"
      HR <|-- HR15
        click HR15 href "../HR15/"
      HR <|-- HR16
        click HR16 href "../HR16/"
      HR <|-- HR17
        click HR17 href "../HR17/"
      HR <|-- HR18
        click HR18 href "../HR18/"
      HR <|-- HR19
        click HR19 href "../HR19/"
      HR <|-- HR20
        click HR20 href "../HR20/"
      HR <|-- HR21
        click HR21 href "../HR21/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **HR** [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * [HR01](HR01.md)
        * [HR02](HR02.md)
        * [HR03](HR03.md)
        * [HR04](HR04.md)
        * [HR05](HR05.md)
        * [HR06](HR06.md)
        * [HR07](HR07.md)
        * [HR08](HR08.md)
        * [HR09](HR09.md)
        * [HR10](HR10.md)
        * [HR11](HR11.md)
        * [HR12](HR12.md)
        * [HR13](HR13.md)
        * [HR14](HR14.md)
        * [HR15](HR15.md)
        * [HR16](HR16.md)
        * [HR17](HR17.md)
        * [HR18](HR18.md)
        * [HR19](HR19.md)
        * [HR20](HR20.md)
        * [HR21](HR21.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:HR](https://w3id.org/lmodel/dpv/loc/HR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Croatia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#HR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:HR |
| native | loc:HR |
| exact | dpv_loc:HR, dpv_loc_owl:HR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Croatia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Croatia
exact_mappings:
- dpv_loc:HR
- dpv_loc_owl:HR
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:HR

```
</details>

### Induced

<details>
```yaml
name: HR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#HR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Croatia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Croatia
exact_mappings:
- dpv_loc:HR
- dpv_loc_owl:HR
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:HR

```
</details></div>