---
search:
  boost: 10.0
---

# Class: ESH 


_Concept representing region Province of Huelva in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-H](https://w3id.org/lmodel/dpv/loc/ES-H)





```mermaid
 classDiagram
    class ESH
    click ESH href "../ESH/"
      ES <|-- ESH
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-H](https://w3id.org/lmodel/dpv/loc/ES-H) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-H
* Province of Huelva




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-H |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-H |
| native | loc:ESH |
| exact | dpv_loc:ES-H, dpv_loc_owl:ES-H |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-H
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Huelva in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-H
- Province of Huelva
exact_mappings:
- dpv_loc:ES-H
- dpv_loc_owl:ES-H
is_a: ES
class_uri: loc:ES-H

```
</details>

### Induced

<details>
```yaml
name: ESH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-H
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Huelva in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-H
- Province of Huelva
exact_mappings:
- dpv_loc:ES-H
- dpv_loc_owl:ES-H
is_a: ES
class_uri: loc:ES-H

```
</details></div>