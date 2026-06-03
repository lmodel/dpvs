---
search:
  boost: 10.0
---

# Class: ESTO 


_Concept representing region Province of Toledo in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-TO](https://w3id.org/lmodel/dpv/loc/ES-TO)





```mermaid
 classDiagram
    class ESTO
    click ESTO href "../ESTO/"
      ES <|-- ESTO
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESTO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-TO](https://w3id.org/lmodel/dpv/loc/ES-TO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-TO
* Province of Toledo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-TO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-TO |
| native | loc:ESTO |
| exact | dpv_loc:ES-TO, dpv_loc_owl:ES-TO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESTO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-TO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Toledo in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-TO
- Province of Toledo
exact_mappings:
- dpv_loc:ES-TO
- dpv_loc_owl:ES-TO
is_a: ES
class_uri: loc:ES-TO

```
</details>

### Induced

<details>
```yaml
name: ESTO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-TO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Toledo in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-TO
- Province of Toledo
exact_mappings:
- dpv_loc:ES-TO
- dpv_loc_owl:ES-TO
is_a: ES
class_uri: loc:ES-TO

```
</details></div>