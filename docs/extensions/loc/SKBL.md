---
search:
  boost: 10.0
---

# Class: SKBL 


_Concept representing region Bratislava Region in country Slovakia_



<div data-search-exclude markdown="1">



URI: [loc:SK-BL](https://w3id.org/lmodel/dpv/loc/SK-BL)





```mermaid
 classDiagram
    class SKBL
    click SKBL href "../SKBL/"
      SK <|-- SKBL
        click SK href "../SK/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SK](SK.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SKBL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SK-BL](https://w3id.org/lmodel/dpv/loc/SK-BL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SK-BL
* Bratislava Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SK-BL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SK-BL |
| native | loc:SKBL |
| exact | dpv_loc:SK-BL, dpv_loc_owl:SK-BL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SKBL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SK-BL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bratislava Region in country Slovakia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SK-BL
- Bratislava Region
exact_mappings:
- dpv_loc:SK-BL
- dpv_loc_owl:SK-BL
is_a: SK
class_uri: loc:SK-BL

```
</details>

### Induced

<details>
```yaml
name: SKBL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SK-BL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bratislava Region in country Slovakia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SK-BL
- Bratislava Region
exact_mappings:
- dpv_loc:SK-BL
- dpv_loc_owl:SK-BL
is_a: SK
class_uri: loc:SK-BL

```
</details></div>