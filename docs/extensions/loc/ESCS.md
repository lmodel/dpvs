---
search:
  boost: 10.0
---

# Class: ESCS 


_Concept representing region Province of Castellón in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CS](https://w3id.org/lmodel/dpv/loc/ES-CS)





```mermaid
 classDiagram
    class ESCS
    click ESCS href "../ESCS/"
      ES <|-- ESCS
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CS](https://w3id.org/lmodel/dpv/loc/ES-CS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CS
* Province of Castellón




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CS |
| native | loc:ESCS |
| exact | dpv_loc:ES-CS, dpv_loc_owl:ES-CS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Castellón in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CS
- Province of Castellón
exact_mappings:
- dpv_loc:ES-CS
- dpv_loc_owl:ES-CS
is_a: ES
class_uri: loc:ES-CS

```
</details>

### Induced

<details>
```yaml
name: ESCS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Castellón in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CS
- Province of Castellón
exact_mappings:
- dpv_loc:ES-CS
- dpv_loc_owl:ES-CS
is_a: ES
class_uri: loc:ES-CS

```
</details></div>