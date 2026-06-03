---
search:
  boost: 10.0
---

# Class: ITTS 


_Concept representing region Province of Trieste in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-TS](https://w3id.org/lmodel/dpv/loc/IT-TS)





```mermaid
 classDiagram
    class ITTS
    click ITTS href "../ITTS/"
      IT <|-- ITTS
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITTS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-TS](https://w3id.org/lmodel/dpv/loc/IT-TS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-TS
* Province of Trieste




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-TS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-TS |
| native | loc:ITTS |
| exact | dpv_loc:IT-TS, dpv_loc_owl:IT-TS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITTS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Trieste in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TS
- Province of Trieste
exact_mappings:
- dpv_loc:IT-TS
- dpv_loc_owl:IT-TS
is_a: IT
class_uri: loc:IT-TS

```
</details>

### Induced

<details>
```yaml
name: ITTS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Trieste in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TS
- Province of Trieste
exact_mappings:
- dpv_loc:IT-TS
- dpv_loc_owl:IT-TS
is_a: IT
class_uri: loc:IT-TS

```
</details></div>