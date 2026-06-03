---
search:
  boost: 10.0
---

# Class: ITCS 


_Concept representing region Province of Cosenza in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-CS](https://w3id.org/lmodel/dpv/loc/IT-CS)





```mermaid
 classDiagram
    class ITCS
    click ITCS href "../ITCS/"
      IT <|-- ITCS
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITCS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-CS](https://w3id.org/lmodel/dpv/loc/IT-CS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-CS
* Province of Cosenza




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-CS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-CS |
| native | loc:ITCS |
| exact | dpv_loc:IT-CS, dpv_loc_owl:IT-CS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITCS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Cosenza in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CS
- Province of Cosenza
exact_mappings:
- dpv_loc:IT-CS
- dpv_loc_owl:IT-CS
is_a: IT
class_uri: loc:IT-CS

```
</details>

### Induced

<details>
```yaml
name: ITCS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Cosenza in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CS
- Province of Cosenza
exact_mappings:
- dpv_loc:IT-CS
- dpv_loc_owl:IT-CS
is_a: IT
class_uri: loc:IT-CS

```
</details></div>