---
search:
  boost: 10.0
---

# Class: ESAL 


_Concept representing region Province of Almería in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-AL](https://w3id.org/lmodel/dpv/loc/ES-AL)





```mermaid
 classDiagram
    class ESAL
    click ESAL href "../ESAL/"
      ES <|-- ESAL
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESAL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-AL](https://w3id.org/lmodel/dpv/loc/ES-AL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-AL
* Province of Almería




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-AL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-AL |
| native | loc:ESAL |
| exact | dpv_loc:ES-AL, dpv_loc_owl:ES-AL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-AL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Almería in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-AL
- Province of Almería
exact_mappings:
- dpv_loc:ES-AL
- dpv_loc_owl:ES-AL
is_a: ES
class_uri: loc:ES-AL

```
</details>

### Induced

<details>
```yaml
name: ESAL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-AL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Almería in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-AL
- Province of Almería
exact_mappings:
- dpv_loc:ES-AL
- dpv_loc_owl:ES-AL
is_a: ES
class_uri: loc:ES-AL

```
</details></div>