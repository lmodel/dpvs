---
search:
  boost: 10.0
---

# Class: ESVC 


_Concept representing region Land of Valencia in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-VC](https://w3id.org/lmodel/dpv/loc/ES-VC)





```mermaid
 classDiagram
    class ESVC
    click ESVC href "../ESVC/"
      ES <|-- ESVC
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESVC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-VC](https://w3id.org/lmodel/dpv/loc/ES-VC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-VC
* Land of Valencia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-VC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-VC |
| native | loc:ESVC |
| exact | dpv_loc:ES-VC, dpv_loc_owl:ES-VC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESVC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-VC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Land of Valencia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-VC
- Land of Valencia
exact_mappings:
- dpv_loc:ES-VC
- dpv_loc_owl:ES-VC
is_a: ES
class_uri: loc:ES-VC

```
</details>

### Induced

<details>
```yaml
name: ESVC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-VC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Land of Valencia in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-VC
- Land of Valencia
exact_mappings:
- dpv_loc:ES-VC
- dpv_loc_owl:ES-VC
is_a: ES
class_uri: loc:ES-VC

```
</details></div>