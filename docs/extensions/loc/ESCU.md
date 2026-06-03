---
search:
  boost: 10.0
---

# Class: ESCU 


_Concept representing region Province of Cuenca in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CU](https://w3id.org/lmodel/dpv/loc/ES-CU)





```mermaid
 classDiagram
    class ESCU
    click ESCU href "../ESCU/"
      ES <|-- ESCU
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCU**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CU](https://w3id.org/lmodel/dpv/loc/ES-CU) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CU
* Province of Cuenca




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CU |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CU |
| native | loc:ESCU |
| exact | dpv_loc:ES-CU, dpv_loc_owl:ES-CU |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Cuenca in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CU
- Province of Cuenca
exact_mappings:
- dpv_loc:ES-CU
- dpv_loc_owl:ES-CU
is_a: ES
class_uri: loc:ES-CU

```
</details>

### Induced

<details>
```yaml
name: ESCU
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CU
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Cuenca in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CU
- Province of Cuenca
exact_mappings:
- dpv_loc:ES-CU
- dpv_loc_owl:ES-CU
is_a: ES
class_uri: loc:ES-CU

```
</details></div>