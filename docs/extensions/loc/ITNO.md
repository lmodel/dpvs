---
search:
  boost: 10.0
---

# Class: ITNO 


_Concept representing region Province of Novara in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-NO](https://w3id.org/lmodel/dpv/loc/IT-NO)





```mermaid
 classDiagram
    class ITNO
    click ITNO href "../ITNO/"
      IT <|-- ITNO
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITNO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-NO](https://w3id.org/lmodel/dpv/loc/IT-NO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-NO
* Province of Novara




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-NO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-NO |
| native | loc:ITNO |
| exact | dpv_loc:IT-NO, dpv_loc_owl:IT-NO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITNO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-NO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Novara in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-NO
- Province of Novara
exact_mappings:
- dpv_loc:IT-NO
- dpv_loc_owl:IT-NO
is_a: IT
class_uri: loc:IT-NO

```
</details>

### Induced

<details>
```yaml
name: ITNO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-NO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Novara in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-NO
- Province of Novara
exact_mappings:
- dpv_loc:IT-NO
- dpv_loc_owl:IT-NO
is_a: IT
class_uri: loc:IT-NO

```
</details></div>