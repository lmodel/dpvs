---
search:
  boost: 10.0
---

# Class: ITPN 


_Concept representing region Province of Pordenone in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-PN](https://w3id.org/lmodel/dpv/loc/IT-PN)





```mermaid
 classDiagram
    class ITPN
    click ITPN href "../ITPN/"
      IT <|-- ITPN
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITPN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-PN](https://w3id.org/lmodel/dpv/loc/IT-PN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-PN
* Province of Pordenone




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-PN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-PN |
| native | loc:ITPN |
| exact | dpv_loc:IT-PN, dpv_loc_owl:IT-PN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITPN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Pordenone in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PN
- Province of Pordenone
exact_mappings:
- dpv_loc:IT-PN
- dpv_loc_owl:IT-PN
is_a: IT
class_uri: loc:IT-PN

```
</details>

### Induced

<details>
```yaml
name: ITPN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-PN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Pordenone in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-PN
- Province of Pordenone
exact_mappings:
- dpv_loc:IT-PN
- dpv_loc_owl:IT-PN
is_a: IT
class_uri: loc:IT-PN

```
</details></div>