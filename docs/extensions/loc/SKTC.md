---
search:
  boost: 10.0
---

# Class: SKTC 


_Concept representing region Trenčín Region in country Slovakia_



<div data-search-exclude markdown="1">



URI: [loc:SK-TC](https://w3id.org/lmodel/dpv/loc/SK-TC)





```mermaid
 classDiagram
    class SKTC
    click SKTC href "../SKTC/"
      SK <|-- SKTC
        click SK href "../SK/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SK](SK.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SKTC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SK-TC](https://w3id.org/lmodel/dpv/loc/SK-TC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SK-TC
* Trenčín Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SK-TC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SK-TC |
| native | loc:SKTC |
| exact | dpv_loc:SK-TC, dpv_loc_owl:SK-TC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SKTC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SK-TC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Trenčín Region in country Slovakia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SK-TC
- Trenčín Region
exact_mappings:
- dpv_loc:SK-TC
- dpv_loc_owl:SK-TC
is_a: SK
class_uri: loc:SK-TC

```
</details>

### Induced

<details>
```yaml
name: SKTC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SK-TC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Trenčín Region in country Slovakia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SK-TC
- Trenčín Region
exact_mappings:
- dpv_loc:SK-TC
- dpv_loc_owl:SK-TC
is_a: SK
class_uri: loc:SK-TC

```
</details></div>