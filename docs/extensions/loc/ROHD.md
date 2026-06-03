---
search:
  boost: 10.0
---

# Class: ROHD 


_Concept representing region Hunedoara County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-HD](https://w3id.org/lmodel/dpv/loc/RO-HD)





```mermaid
 classDiagram
    class ROHD
    click ROHD href "../ROHD/"
      RO <|-- ROHD
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROHD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-HD](https://w3id.org/lmodel/dpv/loc/RO-HD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-HD
* Hunedoara County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-HD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-HD |
| native | loc:ROHD |
| exact | dpv_loc:RO-HD, dpv_loc_owl:RO-HD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROHD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-HD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hunedoara County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-HD
- Hunedoara County
exact_mappings:
- dpv_loc:RO-HD
- dpv_loc_owl:RO-HD
is_a: RO
class_uri: loc:RO-HD

```
</details>

### Induced

<details>
```yaml
name: ROHD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-HD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hunedoara County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-HD
- Hunedoara County
exact_mappings:
- dpv_loc:RO-HD
- dpv_loc_owl:RO-HD
is_a: RO
class_uri: loc:RO-HD

```
</details></div>