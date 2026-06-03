---
search:
  boost: 10.0
---

# Class: ITAL 


_Concept representing region Province of Alessandria in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-AL](https://w3id.org/lmodel/dpv/loc/IT-AL)





```mermaid
 classDiagram
    class ITAL
    click ITAL href "../ITAL/"
      IT <|-- ITAL
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITAL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-AL](https://w3id.org/lmodel/dpv/loc/IT-AL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-AL
* Province of Alessandria




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-AL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-AL |
| native | loc:ITAL |
| exact | dpv_loc:IT-AL, dpv_loc_owl:IT-AL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Alessandria in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AL
- Province of Alessandria
exact_mappings:
- dpv_loc:IT-AL
- dpv_loc_owl:IT-AL
is_a: IT
class_uri: loc:IT-AL

```
</details>

### Induced

<details>
```yaml
name: ITAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Alessandria in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AL
- Province of Alessandria
exact_mappings:
- dpv_loc:IT-AL
- dpv_loc_owl:IT-AL
is_a: IT
class_uri: loc:IT-AL

```
</details></div>