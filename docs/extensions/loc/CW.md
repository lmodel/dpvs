---
search:
  boost: 10.0
---

# Class: CW 


_Concept representing Country of Curaçao_



<div data-search-exclude markdown="1">



URI: [loc:CW](https://w3id.org/lmodel/dpv/loc/CW)





```mermaid
 classDiagram
    class CW
    click CW href "../CW/"
      NL <|-- CW
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **CW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CW](https://w3id.org/lmodel/dpv/loc/CW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Curaçao




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CW |
| native | loc:CW |
| exact | dpv_loc:CW, dpv_loc_owl:CW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Curaçao
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Curaçao
exact_mappings:
- dpv_loc:CW
- dpv_loc_owl:CW
is_a: NL
class_uri: loc:CW

```
</details>

### Induced

<details>
```yaml
name: CW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Curaçao
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Curaçao
exact_mappings:
- dpv_loc:CW
- dpv_loc_owl:CW
is_a: NL
class_uri: loc:CW

```
</details></div>