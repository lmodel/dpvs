---
search:
  boost: 10.0
---

# Class: BirthCountry 


_Information about country of birth_



<div data-search-exclude markdown="1">



URI: [pd:BirthCountry](https://w3id.org/lmodel/dpv/pd/BirthCountry)





```mermaid
 classDiagram
    class BirthCountry
    click BirthCountry href "../BirthCountry/"
      DpvLocation <|-- BirthCountry
        click DpvLocation href "../DpvLocation/"
      DpvCountry <|-- BirthCountry
        click DpvCountry href "../DpvCountry/"
      BirthPlace <|-- BirthCountry
        click BirthPlace href "../BirthPlace/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DpvLocation](DpvLocation.md)
        * [BirthPlace](BirthPlace.md)
            * **BirthCountry** [ [DpvLocation](DpvLocation.md) [DpvCountry](DpvCountry.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:BirthCountry](https://w3id.org/lmodel/dpv/pd/BirthCountry) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Birth Country




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#BirthCountry |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:BirthCountry |
| native | pd:BirthCountry |
| exact | dpv_pd:BirthCountry, dpv_pd_owl:BirthCountry |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BirthCountry
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BirthCountry
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about country of birth
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Birth Country
exact_mappings:
- dpv_pd:BirthCountry
- dpv_pd_owl:BirthCountry
is_a: BirthPlace
mixins:
- DpvLocation
- DpvCountry
class_uri: pd:BirthCountry

```
</details>

### Induced

<details>
```yaml
name: BirthCountry
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BirthCountry
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about country of birth
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Birth Country
exact_mappings:
- dpv_pd:BirthCountry
- dpv_pd_owl:BirthCountry
is_a: BirthPlace
mixins:
- DpvLocation
- DpvCountry
class_uri: pd:BirthCountry

```
</details></div>