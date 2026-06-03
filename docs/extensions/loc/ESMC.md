---
search:
  boost: 10.0
---

# Class: ESMC 


_Concept representing region Region of Murcia in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-MC](https://w3id.org/lmodel/dpv/loc/ES-MC)





```mermaid
 classDiagram
    class ESMC
    click ESMC href "../ESMC/"
      ES <|-- ESMC
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESMC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-MC](https://w3id.org/lmodel/dpv/loc/ES-MC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-MC
* Region of Murcia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-MC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-MC |
| native | loc:ESMC |
| exact | dpv_loc:ES-MC, dpv_loc_owl:ES-MC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESMC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-MC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Region of Murcia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-MC
- Region of Murcia
exact_mappings:
- dpv_loc:ES-MC
- dpv_loc_owl:ES-MC
is_a: ES
class_uri: loc:ES-MC

```
</details>

### Induced

<details>
```yaml
name: ESMC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-MC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Region of Murcia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-MC
- Region of Murcia
exact_mappings:
- dpv_loc:ES-MC
- dpv_loc_owl:ES-MC
is_a: ES
class_uri: loc:ES-MC

```
</details></div>