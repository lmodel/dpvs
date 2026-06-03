---
search:
  boost: 10.0
---

# Class: FILS 


_Concept representing region Western Finland in country Finland_



<div data-search-exclude markdown="1">



URI: [loc:FI-LS](https://w3id.org/lmodel/dpv/loc/FI-LS)





```mermaid
 classDiagram
    class FILS
    click FILS href "../FILS/"
      FI <|-- FILS
        click FI href "../FI/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FI](FI.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FILS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FI-LS](https://w3id.org/lmodel/dpv/loc/FI-LS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FI-LS
* Western Finland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FI-LS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FI-LS |
| native | loc:FILS |
| exact | dpv_loc:FI-LS, dpv_loc_owl:FI-LS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FILS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FI-LS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Western Finland in country Finland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FI-LS
- Western Finland
exact_mappings:
- dpv_loc:FI-LS
- dpv_loc_owl:FI-LS
is_a: FI
class_uri: loc:FI-LS

```
</details>

### Induced

<details>
```yaml
name: FILS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FI-LS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Western Finland in country Finland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FI-LS
- Western Finland
exact_mappings:
- dpv_loc:FI-LS
- dpv_loc_owl:FI-LS
is_a: FI
class_uri: loc:FI-LS

```
</details></div>