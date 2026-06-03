---
search:
  boost: 10.0
---

# Class: ROAB 


_Concept representing region Alba County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-AB](https://w3id.org/lmodel/dpv/loc/RO-AB)





```mermaid
 classDiagram
    class ROAB
    click ROAB href "../ROAB/"
      RO <|-- ROAB
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROAB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-AB](https://w3id.org/lmodel/dpv/loc/RO-AB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-AB
* Alba County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-AB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-AB |
| native | loc:ROAB |
| exact | dpv_loc:RO-AB, dpv_loc_owl:RO-AB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROAB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-AB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Alba County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-AB
- Alba County
exact_mappings:
- dpv_loc:RO-AB
- dpv_loc_owl:RO-AB
is_a: RO
class_uri: loc:RO-AB

```
</details>

### Induced

<details>
```yaml
name: ROAB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-AB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Alba County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-AB
- Alba County
exact_mappings:
- dpv_loc:RO-AB
- dpv_loc_owl:RO-AB
is_a: RO
class_uri: loc:RO-AB

```
</details></div>