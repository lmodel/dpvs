---
search:
  boost: 10.0
---

# Class: DENW 


_Concept representing region North Rhine-Westphalia in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-NW](https://w3id.org/lmodel/dpv/loc/DE-NW)





```mermaid
 classDiagram
    class DENW
    click DENW href "../DENW/"
      DE <|-- DENW
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DENW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-NW](https://w3id.org/lmodel/dpv/loc/DE-NW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-NW
* North Rhine-Westphalia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-NW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-NW |
| native | loc:DENW |
| exact | dpv_loc:DE-NW, dpv_loc_owl:DE-NW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DENW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-NW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region North Rhine-Westphalia in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-NW
- North Rhine-Westphalia
exact_mappings:
- dpv_loc:DE-NW
- dpv_loc_owl:DE-NW
is_a: DE
class_uri: loc:DE-NW

```
</details>

### Induced

<details>
```yaml
name: DENW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-NW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region North Rhine-Westphalia in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-NW
- North Rhine-Westphalia
exact_mappings:
- dpv_loc:DE-NW
- dpv_loc_owl:DE-NW
is_a: DE
class_uri: loc:DE-NW

```
</details></div>