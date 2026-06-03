---
search:
  boost: 10.0
---

# Class: SKBC 


_Concept representing region Banská Bystrica Region in country Slovakia_



<div data-search-exclude markdown="1">



URI: [loc:SK-BC](https://w3id.org/lmodel/dpv/loc/SK-BC)





```mermaid
 classDiagram
    class SKBC
    click SKBC href "../SKBC/"
      SK <|-- SKBC
        click SK href "../SK/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SK](SK.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SKBC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SK-BC](https://w3id.org/lmodel/dpv/loc/SK-BC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SK-BC
* Banská Bystrica Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SK-BC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SK-BC |
| native | loc:SKBC |
| exact | dpv_loc:SK-BC, dpv_loc_owl:SK-BC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SKBC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SK-BC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Banská Bystrica Region in country Slovakia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SK-BC
- Banská Bystrica Region
exact_mappings:
- dpv_loc:SK-BC
- dpv_loc_owl:SK-BC
is_a: SK
class_uri: loc:SK-BC

```
</details>

### Induced

<details>
```yaml
name: SKBC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SK-BC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Banská Bystrica Region in country Slovakia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SK-BC
- Banská Bystrica Region
exact_mappings:
- dpv_loc:SK-BC
- dpv_loc_owl:SK-BC
is_a: SK
class_uri: loc:SK-BC

```
</details></div>