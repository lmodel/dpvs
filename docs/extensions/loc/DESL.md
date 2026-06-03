---
search:
  boost: 10.0
---

# Class: DESL 


_Concept representing region Saarland in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-SL](https://w3id.org/lmodel/dpv/loc/DE-SL)





```mermaid
 classDiagram
    class DESL
    click DESL href "../DESL/"
      DE <|-- DESL
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DESL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-SL](https://w3id.org/lmodel/dpv/loc/DE-SL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-SL
* Saarland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-SL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-SL |
| native | loc:DESL |
| exact | dpv_loc:DE-SL, dpv_loc_owl:DE-SL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DESL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-SL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saarland in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-SL
- Saarland
exact_mappings:
- dpv_loc:DE-SL
- dpv_loc_owl:DE-SL
is_a: DE
class_uri: loc:DE-SL

```
</details>

### Induced

<details>
```yaml
name: DESL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-SL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saarland in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-SL
- Saarland
exact_mappings:
- dpv_loc:DE-SL
- dpv_loc_owl:DE-SL
is_a: DE
class_uri: loc:DE-SL

```
</details></div>