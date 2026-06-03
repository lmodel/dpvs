---
search:
  boost: 10.0
---

# Class: ESCT 


_Concept representing region Catalonia in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-CT](https://w3id.org/lmodel/dpv/loc/ES-CT)





```mermaid
 classDiagram
    class ESCT
    click ESCT href "../ESCT/"
      ES <|-- ESCT
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESCT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-CT](https://w3id.org/lmodel/dpv/loc/ES-CT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-CT
* Catalonia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-CT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-CT |
| native | loc:ESCT |
| exact | dpv_loc:ES-CT, dpv_loc_owl:ES-CT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESCT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Catalonia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CT
- Catalonia
exact_mappings:
- dpv_loc:ES-CT
- dpv_loc_owl:ES-CT
is_a: ES
class_uri: loc:ES-CT

```
</details>

### Induced

<details>
```yaml
name: ESCT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-CT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Catalonia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-CT
- Catalonia
exact_mappings:
- dpv_loc:ES-CT
- dpv_loc_owl:ES-CT
is_a: ES
class_uri: loc:ES-CT

```
</details></div>