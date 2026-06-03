---
search:
  boost: 10.0
---

# Class: ITTA 


_Concept representing region Province of Taranto in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-TA](https://w3id.org/lmodel/dpv/loc/IT-TA)





```mermaid
 classDiagram
    class ITTA
    click ITTA href "../ITTA/"
      IT <|-- ITTA
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITTA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-TA](https://w3id.org/lmodel/dpv/loc/IT-TA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-TA
* Province of Taranto




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-TA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-TA |
| native | loc:ITTA |
| exact | dpv_loc:IT-TA, dpv_loc_owl:IT-TA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITTA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Taranto in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TA
- Province of Taranto
exact_mappings:
- dpv_loc:IT-TA
- dpv_loc_owl:IT-TA
is_a: IT
class_uri: loc:IT-TA

```
</details>

### Induced

<details>
```yaml
name: ITTA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Taranto in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TA
- Province of Taranto
exact_mappings:
- dpv_loc:IT-TA
- dpv_loc_owl:IT-TA
is_a: IT
class_uri: loc:IT-TA

```
</details></div>