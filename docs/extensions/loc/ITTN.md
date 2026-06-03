---
search:
  boost: 10.0
---

# Class: ITTN 


_Concept representing region Province of Trento in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-TN](https://w3id.org/lmodel/dpv/loc/IT-TN)





```mermaid
 classDiagram
    class ITTN
    click ITTN href "../ITTN/"
      IT <|-- ITTN
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITTN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-TN](https://w3id.org/lmodel/dpv/loc/IT-TN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-TN
* Province of Trento




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-TN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-TN |
| native | loc:ITTN |
| exact | dpv_loc:IT-TN, dpv_loc_owl:IT-TN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITTN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Trento in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TN
- Province of Trento
exact_mappings:
- dpv_loc:IT-TN
- dpv_loc_owl:IT-TN
is_a: IT
class_uri: loc:IT-TN

```
</details>

### Induced

<details>
```yaml
name: ITTN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Trento in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TN
- Province of Trento
exact_mappings:
- dpv_loc:IT-TN
- dpv_loc_owl:IT-TN
is_a: IT
class_uri: loc:IT-TN

```
</details></div>