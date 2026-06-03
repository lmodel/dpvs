---
search:
  boost: 10.0
---

# Class: EST 


_Concept representing region Province of Tarragona in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-T](https://w3id.org/lmodel/dpv/loc/ES-T)





```mermaid
 classDiagram
    class EST
    click EST href "../EST/"
      ES <|-- EST
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **EST**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-T](https://w3id.org/lmodel/dpv/loc/ES-T) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-T
* Province of Tarragona




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-T |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-T |
| native | loc:EST |
| exact | dpv_loc:ES-T, dpv_loc_owl:ES-T |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EST
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-T
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Tarragona in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-T
- Province of Tarragona
exact_mappings:
- dpv_loc:ES-T
- dpv_loc_owl:ES-T
is_a: ES
class_uri: loc:ES-T

```
</details>

### Induced

<details>
```yaml
name: EST
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-T
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Tarragona in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-T
- Province of Tarragona
exact_mappings:
- dpv_loc:ES-T
- dpv_loc_owl:ES-T
is_a: ES
class_uri: loc:ES-T

```
</details></div>