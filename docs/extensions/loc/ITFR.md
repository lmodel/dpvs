---
search:
  boost: 10.0
---

# Class: ITFR 


_Concept representing region Province of Frosinone in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-FR](https://w3id.org/lmodel/dpv/loc/IT-FR)





```mermaid
 classDiagram
    class ITFR
    click ITFR href "../ITFR/"
      IT <|-- ITFR
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITFR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-FR](https://w3id.org/lmodel/dpv/loc/IT-FR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-FR
* Province of Frosinone




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-FR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-FR |
| native | loc:ITFR |
| exact | dpv_loc:IT-FR, dpv_loc_owl:IT-FR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITFR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-FR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Frosinone in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-FR
- Province of Frosinone
exact_mappings:
- dpv_loc:IT-FR
- dpv_loc_owl:IT-FR
is_a: IT
class_uri: loc:IT-FR

```
</details>

### Induced

<details>
```yaml
name: ITFR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-FR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Frosinone in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-FR
- Province of Frosinone
exact_mappings:
- dpv_loc:IT-FR
- dpv_loc_owl:IT-FR
is_a: IT
class_uri: loc:IT-FR

```
</details></div>