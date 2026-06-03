---
search:
  boost: 10.0
---

# Class: ROCT 


_Concept representing region Constanța County in country Romania_



<div data-search-exclude markdown="1">



URI: [loc:RO-CT](https://w3id.org/lmodel/dpv/loc/RO-CT)





```mermaid
 classDiagram
    class ROCT
    click ROCT href "../ROCT/"
      RO <|-- ROCT
        click RO href "../RO/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [RO](RO.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ROCT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:RO-CT](https://w3id.org/lmodel/dpv/loc/RO-CT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* RO-CT
* Constanța County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#RO-CT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:RO-CT |
| native | loc:ROCT |
| exact | dpv_loc:RO-CT, dpv_loc_owl:RO-CT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ROCT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-CT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Constanța County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-CT
- Constanța County
exact_mappings:
- dpv_loc:RO-CT
- dpv_loc_owl:RO-CT
is_a: RO
class_uri: loc:RO-CT

```
</details>

### Induced

<details>
```yaml
name: ROCT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#RO-CT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Constanța County in country Romania
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- RO-CT
- Constanța County
exact_mappings:
- dpv_loc:RO-CT
- dpv_loc_owl:RO-CT
is_a: RO
class_uri: loc:RO-CT

```
</details></div>