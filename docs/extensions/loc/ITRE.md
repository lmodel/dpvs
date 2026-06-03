---
search:
  boost: 10.0
---

# Class: ITRE 


_Concept representing region Province of Reggio Emilia in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-RE](https://w3id.org/lmodel/dpv/loc/IT-RE)





```mermaid
 classDiagram
    class ITRE
    click ITRE href "../ITRE/"
      IT <|-- ITRE
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITRE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-RE](https://w3id.org/lmodel/dpv/loc/IT-RE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-RE
* Province of Reggio Emilia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-RE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-RE |
| native | loc:ITRE |
| exact | dpv_loc:IT-RE, dpv_loc_owl:IT-RE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITRE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-RE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Reggio Emilia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-RE
- Province of Reggio Emilia
exact_mappings:
- dpv_loc:IT-RE
- dpv_loc_owl:IT-RE
is_a: IT
class_uri: loc:IT-RE

```
</details>

### Induced

<details>
```yaml
name: ITRE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-RE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Reggio Emilia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-RE
- Province of Reggio Emilia
exact_mappings:
- dpv_loc:IT-RE
- dpv_loc_owl:IT-RE
is_a: IT
class_uri: loc:IT-RE

```
</details></div>