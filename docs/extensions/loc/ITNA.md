---
search:
  boost: 10.0
---

# Class: ITNA 


_Concept representing region Metropolitan city of Naples in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-NA](https://w3id.org/lmodel/dpv/loc/IT-NA)





```mermaid
 classDiagram
    class ITNA
    click ITNA href "../ITNA/"
      IT <|-- ITNA
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITNA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-NA](https://w3id.org/lmodel/dpv/loc/IT-NA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-NA
* Metropolitan city of Naples




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-NA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-NA |
| native | loc:ITNA |
| exact | dpv_loc:IT-NA, dpv_loc_owl:IT-NA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITNA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-NA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Metropolitan city of Naples in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-NA
- Metropolitan city of Naples
exact_mappings:
- dpv_loc:IT-NA
- dpv_loc_owl:IT-NA
is_a: IT
class_uri: loc:IT-NA

```
</details>

### Induced

<details>
```yaml
name: ITNA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-NA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Metropolitan city of Naples in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-NA
- Metropolitan city of Naples
exact_mappings:
- dpv_loc:IT-NA
- dpv_loc_owl:IT-NA
is_a: IT
class_uri: loc:IT-NA

```
</details></div>