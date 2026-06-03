---
search:
  boost: 10.0
---

# Class: ITMT 


_Concept representing region Province of Matera in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-MT](https://w3id.org/lmodel/dpv/loc/IT-MT)





```mermaid
 classDiagram
    class ITMT
    click ITMT href "../ITMT/"
      IT <|-- ITMT
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITMT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-MT](https://w3id.org/lmodel/dpv/loc/IT-MT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-MT
* Province of Matera




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-MT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-MT |
| native | loc:ITMT |
| exact | dpv_loc:IT-MT, dpv_loc_owl:IT-MT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITMT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Matera in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MT
- Province of Matera
exact_mappings:
- dpv_loc:IT-MT
- dpv_loc_owl:IT-MT
is_a: IT
class_uri: loc:IT-MT

```
</details>

### Induced

<details>
```yaml
name: ITMT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-MT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Matera in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-MT
- Province of Matera
exact_mappings:
- dpv_loc:IT-MT
- dpv_loc_owl:IT-MT
is_a: IT
class_uri: loc:IT-MT

```
</details></div>