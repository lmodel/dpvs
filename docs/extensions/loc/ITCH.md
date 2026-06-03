---
search:
  boost: 10.0
---

# Class: ITCH 


_Concept representing region Province of Chieti in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-CH](https://w3id.org/lmodel/dpv/loc/IT-CH)





```mermaid
 classDiagram
    class ITCH
    click ITCH href "../ITCH/"
      IT <|-- ITCH
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITCH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-CH](https://w3id.org/lmodel/dpv/loc/IT-CH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-CH
* Province of Chieti




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-CH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-CH |
| native | loc:ITCH |
| exact | dpv_loc:IT-CH, dpv_loc_owl:IT-CH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITCH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Chieti in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CH
- Province of Chieti
exact_mappings:
- dpv_loc:IT-CH
- dpv_loc_owl:IT-CH
is_a: IT
class_uri: loc:IT-CH

```
</details>

### Induced

<details>
```yaml
name: ITCH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Chieti in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CH
- Province of Chieti
exact_mappings:
- dpv_loc:IT-CH
- dpv_loc_owl:IT-CH
is_a: IT
class_uri: loc:IT-CH

```
</details></div>