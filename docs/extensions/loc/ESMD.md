---
search:
  boost: 10.0
---

# Class: ESMD 


_Concept representing region Community of Madrid in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-MD](https://w3id.org/lmodel/dpv/loc/ES-MD)





```mermaid
 classDiagram
    class ESMD
    click ESMD href "../ESMD/"
      ES <|-- ESMD
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESMD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-MD](https://w3id.org/lmodel/dpv/loc/ES-MD) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-MD
* Community of Madrid




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-MD |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-MD |
| native | loc:ESMD |
| exact | dpv_loc:ES-MD, dpv_loc_owl:ES-MD |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESMD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-MD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Community of Madrid in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-MD
- Community of Madrid
exact_mappings:
- dpv_loc:ES-MD
- dpv_loc_owl:ES-MD
is_a: ES
class_uri: loc:ES-MD

```
</details>

### Induced

<details>
```yaml
name: ESMD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-MD
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Community of Madrid in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-MD
- Community of Madrid
exact_mappings:
- dpv_loc:ES-MD
- dpv_loc_owl:ES-MD
is_a: ES
class_uri: loc:ES-MD

```
</details></div>