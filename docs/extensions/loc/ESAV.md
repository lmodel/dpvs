---
search:
  boost: 10.0
---

# Class: ESAV 


_Concept representing region Province of Ávila in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-AV](https://w3id.org/lmodel/dpv/loc/ES-AV)





```mermaid
 classDiagram
    class ESAV
    click ESAV href "../ESAV/"
      ES <|-- ESAV
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESAV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-AV](https://w3id.org/lmodel/dpv/loc/ES-AV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-AV
* Province of Ávila




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-AV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-AV |
| native | loc:ESAV |
| exact | dpv_loc:ES-AV, dpv_loc_owl:ES-AV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESAV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-AV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ávila in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-AV
- Province of Ávila
exact_mappings:
- dpv_loc:ES-AV
- dpv_loc_owl:ES-AV
is_a: ES
class_uri: loc:ES-AV

```
</details>

### Induced

<details>
```yaml
name: ESAV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-AV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Ávila in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-AV
- Province of Ávila
exact_mappings:
- dpv_loc:ES-AV
- dpv_loc_owl:ES-AV
is_a: ES
class_uri: loc:ES-AV

```
</details></div>