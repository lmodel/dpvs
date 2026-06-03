---
search:
  boost: 10.0
---

# Class: FIIS 


_Concept representing region Eastern Finland in country Finland_



<div data-search-exclude markdown="1">



URI: [loc:FI-IS](https://w3id.org/lmodel/dpv/loc/FI-IS)





```mermaid
 classDiagram
    class FIIS
    click FIIS href "../FIIS/"
      FI <|-- FIIS
        click FI href "../FI/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FI](FI.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FIIS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FI-IS](https://w3id.org/lmodel/dpv/loc/FI-IS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FI-IS
* Eastern Finland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FI-IS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FI-IS |
| native | loc:FIIS |
| exact | dpv_loc:FI-IS, dpv_loc_owl:FI-IS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FIIS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FI-IS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Eastern Finland in country Finland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FI-IS
- Eastern Finland
exact_mappings:
- dpv_loc:FI-IS
- dpv_loc_owl:FI-IS
is_a: FI
class_uri: loc:FI-IS

```
</details>

### Induced

<details>
```yaml
name: FIIS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FI-IS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Eastern Finland in country Finland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FI-IS
- Eastern Finland
exact_mappings:
- dpv_loc:FI-IS
- dpv_loc_owl:FI-IS
is_a: FI
class_uri: loc:FI-IS

```
</details></div>