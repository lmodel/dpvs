---
search:
  boost: 10.0
---

# Class: ITVA 


_Concept representing region Province of Varese in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-VA](https://w3id.org/lmodel/dpv/loc/IT-VA)





```mermaid
 classDiagram
    class ITVA
    click ITVA href "../ITVA/"
      IT <|-- ITVA
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITVA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-VA](https://w3id.org/lmodel/dpv/loc/IT-VA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-VA
* Province of Varese




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-VA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-VA |
| native | loc:ITVA |
| exact | dpv_loc:IT-VA, dpv_loc_owl:IT-VA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITVA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Varese in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VA
- Province of Varese
exact_mappings:
- dpv_loc:IT-VA
- dpv_loc_owl:IT-VA
is_a: IT
class_uri: loc:IT-VA

```
</details>

### Induced

<details>
```yaml
name: ITVA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-VA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Varese in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-VA
- Province of Varese
exact_mappings:
- dpv_loc:IT-VA
- dpv_loc_owl:IT-VA
is_a: IT
class_uri: loc:IT-VA

```
</details></div>