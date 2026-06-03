---
search:
  boost: 10.0
---

# Class: ESTE 


_Concept representing region Province of Teruel in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-TE](https://w3id.org/lmodel/dpv/loc/ES-TE)





```mermaid
 classDiagram
    class ESTE
    click ESTE href "../ESTE/"
      ES <|-- ESTE
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESTE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-TE](https://w3id.org/lmodel/dpv/loc/ES-TE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-TE
* Province of Teruel




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-TE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-TE |
| native | loc:ESTE |
| exact | dpv_loc:ES-TE, dpv_loc_owl:ES-TE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESTE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-TE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Teruel in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-TE
- Province of Teruel
exact_mappings:
- dpv_loc:ES-TE
- dpv_loc_owl:ES-TE
is_a: ES
class_uri: loc:ES-TE

```
</details>

### Induced

<details>
```yaml
name: ESTE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-TE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Teruel in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-TE
- Province of Teruel
exact_mappings:
- dpv_loc:ES-TE
- dpv_loc_owl:ES-TE
is_a: ES
class_uri: loc:ES-TE

```
</details></div>