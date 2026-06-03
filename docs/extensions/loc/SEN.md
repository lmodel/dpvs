---
search:
  boost: 10.0
---

# Class: SEN 


_Concept representing region Halland County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-N](https://w3id.org/lmodel/dpv/loc/SE-N)





```mermaid
 classDiagram
    class SEN
    click SEN href "../SEN/"
      SE <|-- SEN
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-N](https://w3id.org/lmodel/dpv/loc/SE-N) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-N
* Halland County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-N |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-N |
| native | loc:SEN |
| exact | dpv_loc:SE-N, dpv_loc_owl:SE-N |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-N
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Halland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-N
- Halland County
exact_mappings:
- dpv_loc:SE-N
- dpv_loc_owl:SE-N
is_a: SE
class_uri: loc:SE-N

```
</details>

### Induced

<details>
```yaml
name: SEN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-N
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Halland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-N
- Halland County
exact_mappings:
- dpv_loc:SE-N
- dpv_loc_owl:SE-N
is_a: SE
class_uri: loc:SE-N

```
</details></div>