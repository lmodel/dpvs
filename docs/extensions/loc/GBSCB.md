---
search:
  boost: 10.0
---

# Class: GBSCB 


_Concept representing region Scottish Borders in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-SCB](https://w3id.org/lmodel/dpv/loc/GB-SCB)





```mermaid
 classDiagram
    class GBSCB
    click GBSCB href "../GBSCB/"
      GB <|-- GBSCB
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBSCB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-SCB](https://w3id.org/lmodel/dpv/loc/GB-SCB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-SCB
* Scottish Borders




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-SCB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-SCB |
| native | loc:GBSCB |
| exact | dpv_loc:GB-SCB, dpv_loc_owl:GB-SCB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBSCB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SCB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Scottish Borders in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SCB
- Scottish Borders
exact_mappings:
- dpv_loc:GB-SCB
- dpv_loc_owl:GB-SCB
is_a: GB
class_uri: loc:GB-SCB

```
</details>

### Induced

<details>
```yaml
name: GBSCB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-SCB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Scottish Borders in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-SCB
- Scottish Borders
exact_mappings:
- dpv_loc:GB-SCB
- dpv_loc_owl:GB-SCB
is_a: GB
class_uri: loc:GB-SCB

```
</details></div>