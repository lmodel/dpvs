---
search:
  boost: 10.0
---

# Class: ESSA 


_Concept representing region Province of Salamanca in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-SA](https://w3id.org/lmodel/dpv/loc/ES-SA)





```mermaid
 classDiagram
    class ESSA
    click ESSA href "../ESSA/"
      ES <|-- ESSA
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESSA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-SA](https://w3id.org/lmodel/dpv/loc/ES-SA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-SA
* Province of Salamanca




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-SA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-SA |
| native | loc:ESSA |
| exact | dpv_loc:ES-SA, dpv_loc_owl:ES-SA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Salamanca in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-SA
- Province of Salamanca
exact_mappings:
- dpv_loc:ES-SA
- dpv_loc_owl:ES-SA
is_a: ES
class_uri: loc:ES-SA

```
</details>

### Induced

<details>
```yaml
name: ESSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Salamanca in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-SA
- Province of Salamanca
exact_mappings:
- dpv_loc:ES-SA
- dpv_loc_owl:ES-SA
is_a: ES
class_uri: loc:ES-SA

```
</details></div>