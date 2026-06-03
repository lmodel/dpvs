---
search:
  boost: 10.0
---

# Class: ESBA 


_Concept representing region Province of Badajoz in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-BA](https://w3id.org/lmodel/dpv/loc/ES-BA)





```mermaid
 classDiagram
    class ESBA
    click ESBA href "../ESBA/"
      ES <|-- ESBA
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESBA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-BA](https://w3id.org/lmodel/dpv/loc/ES-BA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-BA
* Province of Badajoz




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-BA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-BA |
| native | loc:ESBA |
| exact | dpv_loc:ES-BA, dpv_loc_owl:ES-BA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESBA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-BA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Badajoz in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-BA
- Province of Badajoz
exact_mappings:
- dpv_loc:ES-BA
- dpv_loc_owl:ES-BA
is_a: ES
class_uri: loc:ES-BA

```
</details>

### Induced

<details>
```yaml
name: ESBA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-BA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Badajoz in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-BA
- Province of Badajoz
exact_mappings:
- dpv_loc:ES-BA
- dpv_loc_owl:ES-BA
is_a: ES
class_uri: loc:ES-BA

```
</details></div>