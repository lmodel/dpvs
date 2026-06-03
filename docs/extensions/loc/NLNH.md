---
search:
  boost: 10.0
---

# Class: NLNH 


_Concept representing region North Holland in country Netherlands_



<div data-search-exclude markdown="1">



URI: [loc:NL-NH](https://w3id.org/lmodel/dpv/loc/NL-NH)





```mermaid
 classDiagram
    class NLNH
    click NLNH href "../NLNH/"
      NL <|-- NLNH
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NLNH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NL-NH](https://w3id.org/lmodel/dpv/loc/NL-NH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NL-NH
* North Holland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NL-NH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NL-NH |
| native | loc:NLNH |
| exact | dpv_loc:NL-NH, dpv_loc_owl:NL-NH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NLNH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-NH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region North Holland in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-NH
- North Holland
exact_mappings:
- dpv_loc:NL-NH
- dpv_loc_owl:NL-NH
is_a: NL
class_uri: loc:NL-NH

```
</details>

### Induced

<details>
```yaml
name: NLNH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-NH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region North Holland in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-NH
- North Holland
exact_mappings:
- dpv_loc:NL-NH
- dpv_loc_owl:NL-NH
is_a: NL
class_uri: loc:NL-NH

```
</details></div>