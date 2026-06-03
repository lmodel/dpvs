---
search:
  boost: 10.0
---

# Class: ESSE 


_Concept representing region Province of Seville in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-SE](https://w3id.org/lmodel/dpv/loc/ES-SE)





```mermaid
 classDiagram
    class ESSE
    click ESSE href "../ESSE/"
      ES <|-- ESSE
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESSE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-SE](https://w3id.org/lmodel/dpv/loc/ES-SE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-SE
* Province of Seville




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-SE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-SE |
| native | loc:ESSE |
| exact | dpv_loc:ES-SE, dpv_loc_owl:ES-SE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESSE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-SE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Seville in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-SE
- Province of Seville
exact_mappings:
- dpv_loc:ES-SE
- dpv_loc_owl:ES-SE
is_a: ES
class_uri: loc:ES-SE

```
</details>

### Induced

<details>
```yaml
name: ESSE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-SE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Seville in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-SE
- Province of Seville
exact_mappings:
- dpv_loc:ES-SE
- dpv_loc_owl:ES-SE
is_a: ES
class_uri: loc:ES-SE

```
</details></div>