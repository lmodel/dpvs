---
search:
  boost: 10.0
---

# Class: ESCL 


_Concept representing region Castile and León in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CL](https://w3id.org/lmodel/dpv/loc/ES-CL)





```mermaid
 classDiagram
    class ESCL
    click ESCL href "../ESCL/"
      ES <|-- ESCL
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CL](https://w3id.org/lmodel/dpv/loc/ES-CL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CL
* Castile and León




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CL |
| native | loc:ESCL |
| exact | dpv_loc:ES-CL, dpv_loc_owl:ES-CL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Castile and León in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CL
- Castile and León
exact_mappings:
- dpv_loc:ES-CL
- dpv_loc_owl:ES-CL
is_a: ES
class_uri: loc:ES-CL

```
</details>

### Induced

<details>
```yaml
name: ESCL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Castile and León in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CL
- Castile and León
exact_mappings:
- dpv_loc:ES-CL
- dpv_loc_owl:ES-CL
is_a: ES
class_uri: loc:ES-CL

```
</details></div>