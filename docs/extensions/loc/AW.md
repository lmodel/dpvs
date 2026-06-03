---
search:
  boost: 10.0
---

# Class: AW 


_Concept representing Conutry of Aruba_



<div data-search-exclude markdown="1">



URI: [loc:AW](https://w3id.org/lmodel/dpv/loc/AW)





```mermaid
 classDiagram
    class AW
    click AW href "../AW/"
      NL <|-- AW
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **AW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AW](https://w3id.org/lmodel/dpv/loc/AW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Aruba




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AW |
| native | loc:AW |
| exact | dpv_loc:AW, dpv_loc_owl:AW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Conutry of Aruba
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Aruba
exact_mappings:
- dpv_loc:AW
- dpv_loc_owl:AW
is_a: NL
class_uri: loc:AW

```
</details>

### Induced

<details>
```yaml
name: AW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Conutry of Aruba
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Aruba
exact_mappings:
- dpv_loc:AW
- dpv_loc_owl:AW
is_a: NL
class_uri: loc:AW

```
</details></div>