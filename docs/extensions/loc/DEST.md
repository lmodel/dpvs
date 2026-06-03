---
search:
  boost: 10.0
---

# Class: DEST 


_Concept representing region Saxony-Anhalt in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-ST](https://w3id.org/lmodel/dpv/loc/DE-ST)





```mermaid
 classDiagram
    class DEST
    click DEST href "../DEST/"
      DE <|-- DEST
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DEST**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-ST](https://w3id.org/lmodel/dpv/loc/DE-ST) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-ST
* Saxony-Anhalt




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-ST |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-ST |
| native | loc:DEST |
| exact | dpv_loc:DE-ST, dpv_loc_owl:DE-ST |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DEST
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-ST
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saxony-Anhalt in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-ST
- Saxony-Anhalt
exact_mappings:
- dpv_loc:DE-ST
- dpv_loc_owl:DE-ST
is_a: DE
class_uri: loc:DE-ST

```
</details>

### Induced

<details>
```yaml
name: DEST
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-ST
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saxony-Anhalt in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-ST
- Saxony-Anhalt
exact_mappings:
- dpv_loc:DE-ST
- dpv_loc_owl:DE-ST
is_a: DE
class_uri: loc:DE-ST

```
</details></div>