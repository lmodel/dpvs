---
search:
  boost: 10.0
---

# Class: SES 


_Concept representing region Värmland County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-S](https://w3id.org/lmodel/dpv/loc/SE-S)





```mermaid
 classDiagram
    class SES
    click SES href "../SES/"
      SE <|-- SES
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SES**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-S](https://w3id.org/lmodel/dpv/loc/SE-S) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-S
* Värmland County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-S |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-S |
| native | loc:SES |
| exact | dpv_loc:SE-S, dpv_loc_owl:SE-S |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SES
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-S
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Värmland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-S
- Värmland County
exact_mappings:
- dpv_loc:SE-S
- dpv_loc_owl:SE-S
is_a: SE
class_uri: loc:SE-S

```
</details>

### Induced

<details>
```yaml
name: SES
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-S
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Värmland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-S
- Värmland County
exact_mappings:
- dpv_loc:SE-S
- dpv_loc_owl:SE-S
is_a: SE
class_uri: loc:SE-S

```
</details></div>