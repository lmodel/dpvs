---
search:
  boost: 10.0
---

# Class: ROCJ 


_Concept representing region Cluj County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-CJ](https://w3id.org/lmodel/dpv/loc/RO-CJ)





```mermaid
 classDiagram
    class ROCJ
    click ROCJ href "../ROCJ/"
      RO <|-- ROCJ
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROCJ**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-CJ](https://w3id.org/lmodel/dpv/loc/RO-CJ) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-CJ
* Cluj County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-CJ |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-CJ |
| native | loc:ROCJ |
| exact | dpv_loc:RO-CJ, dpv_loc_owl:RO-CJ |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROCJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-CJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Cluj County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-CJ
- Cluj County
exact_mappings:
- dpv_loc:RO-CJ
- dpv_loc_owl:RO-CJ
is_a: RO
class_uri: loc:RO-CJ

```
</details>

### Induced

<details>
```yaml
name: ROCJ
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-CJ
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Cluj County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-CJ
- Cluj County
exact_mappings:
- dpv_loc:RO-CJ
- dpv_loc_owl:RO-CJ
is_a: RO
class_uri: loc:RO-CJ

```
</details></div>