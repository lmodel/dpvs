---
search:
  boost: 10.0
---

# Class: ITCR 


_Concept representing region Province of Cremona in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-CR](https://w3id.org/lmodel/dpv/loc/IT-CR)





```mermaid
 classDiagram
    class ITCR
    click ITCR href "../ITCR/"
      IT <|-- ITCR
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITCR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-CR](https://w3id.org/lmodel/dpv/loc/IT-CR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-CR
* Province of Cremona




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-CR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-CR |
| native | loc:ITCR |
| exact | dpv_loc:IT-CR, dpv_loc_owl:IT-CR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITCR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Cremona in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CR
- Province of Cremona
exact_mappings:
- dpv_loc:IT-CR
- dpv_loc_owl:IT-CR
is_a: IT
class_uri: loc:IT-CR

```
</details>

### Induced

<details>
```yaml
name: ITCR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-CR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Cremona in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-CR
- Province of Cremona
exact_mappings:
- dpv_loc:IT-CR
- dpv_loc_owl:IT-CR
is_a: IT
class_uri: loc:IT-CR

```
</details></div>