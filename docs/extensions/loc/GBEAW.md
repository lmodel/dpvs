---
search:
  boost: 10.0
---

# Class: GBEAW 


_Concept representing region England and Wales in country United Kingdom_

_of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-EAW](https://w3id.org/lmodel/dpv/loc/GB-EAW)





```mermaid
 classDiagram
    class GBEAW
    click GBEAW href "../GBEAW/"
      GB <|-- GBEAW
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBEAW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-EAW](https://w3id.org/lmodel/dpv/loc/GB-EAW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-EAW
* England and Wales




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-EAW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-EAW |
| native | loc:GBEAW |
| exact | dpv_loc:GB-EAW, dpv_loc_owl:GB-EAW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBEAW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-EAW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region England and Wales in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-EAW
- England and Wales
exact_mappings:
- dpv_loc:GB-EAW
- dpv_loc_owl:GB-EAW
is_a: GB
class_uri: loc:GB-EAW

```
</details>

### Induced

<details>
```yaml
name: GBEAW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-EAW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region England and Wales in country United Kingdom

  of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-EAW
- England and Wales
exact_mappings:
- dpv_loc:GB-EAW
- dpv_loc_owl:GB-EAW
is_a: GB
class_uri: loc:GB-EAW

```
</details></div>