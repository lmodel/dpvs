---
search:
  boost: 10.0
---

# Class: ESRI 


_Concept representing region La Rioja (Spain) in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-RI](https://w3id.org/lmodel/dpv/loc/ES-RI)





```mermaid
 classDiagram
    class ESRI
    click ESRI href "../ESRI/"
      ES <|-- ESRI
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESRI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-RI](https://w3id.org/lmodel/dpv/loc/ES-RI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-RI
* La Rioja (Spain)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-RI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-RI |
| native | loc:ESRI |
| exact | dpv_loc:ES-RI, dpv_loc_owl:ES-RI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESRI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-RI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region La Rioja (Spain) in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-RI
- La Rioja (Spain)
exact_mappings:
- dpv_loc:ES-RI
- dpv_loc_owl:ES-RI
is_a: ES
class_uri: loc:ES-RI

```
</details>

### Induced

<details>
```yaml
name: ESRI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-RI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region La Rioja (Spain) in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-RI
- La Rioja (Spain)
exact_mappings:
- dpv_loc:ES-RI
- dpv_loc_owl:ES-RI
is_a: ES
class_uri: loc:ES-RI

```
</details></div>