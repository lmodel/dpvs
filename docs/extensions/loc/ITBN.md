---
search:
  boost: 10.0
---

# Class: ITBN 


_Concept representing region Province of Benevento in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-BN](https://w3id.org/lmodel/dpv/loc/IT-BN)





```mermaid
 classDiagram
    class ITBN
    click ITBN href "../ITBN/"
      IT <|-- ITBN
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITBN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-BN](https://w3id.org/lmodel/dpv/loc/IT-BN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-BN
* Province of Benevento




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-BN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-BN |
| native | loc:ITBN |
| exact | dpv_loc:IT-BN, dpv_loc_owl:IT-BN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITBN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Benevento in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BN
- Province of Benevento
exact_mappings:
- dpv_loc:IT-BN
- dpv_loc_owl:IT-BN
is_a: IT
class_uri: loc:IT-BN

```
</details>

### Induced

<details>
```yaml
name: ITBN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-BN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Benevento in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-BN
- Province of Benevento
exact_mappings:
- dpv_loc:IT-BN
- dpv_loc_owl:IT-BN
is_a: IT
class_uri: loc:IT-BN

```
</details></div>