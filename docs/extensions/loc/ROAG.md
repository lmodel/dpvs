---
search:
  boost: 10.0
---

# Class: ROAG 


_Concept representing region Argeș County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-AG](https://w3id.org/lmodel/dpv/loc/RO-AG)





```mermaid
 classDiagram
    class ROAG
    click ROAG href "../ROAG/"
      RO <|-- ROAG
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROAG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-AG](https://w3id.org/lmodel/dpv/loc/RO-AG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-AG
* Argeș County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-AG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-AG |
| native | loc:ROAG |
| exact | dpv_loc:RO-AG, dpv_loc_owl:RO-AG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROAG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-AG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Argeș County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-AG
- Argeș County
exact_mappings:
- dpv_loc:RO-AG
- dpv_loc_owl:RO-AG
is_a: RO
class_uri: loc:RO-AG

```
</details>

### Induced

<details>
```yaml
name: ROAG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-AG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Argeș County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-AG
- Argeș County
exact_mappings:
- dpv_loc:RO-AG
- dpv_loc_owl:RO-AG
is_a: RO
class_uri: loc:RO-AG

```
</details></div>