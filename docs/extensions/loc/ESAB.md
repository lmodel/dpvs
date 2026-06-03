---
search:
  boost: 10.0
---

# Class: ESAB 


_Concept representing region Province of Albacete in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-AB](https://w3id.org/lmodel/dpv/loc/ES-AB)





```mermaid
 classDiagram
    class ESAB
    click ESAB href "../ESAB/"
      ES <|-- ESAB
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESAB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-AB](https://w3id.org/lmodel/dpv/loc/ES-AB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-AB
* Province of Albacete




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-AB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-AB |
| native | loc:ESAB |
| exact | dpv_loc:ES-AB, dpv_loc_owl:ES-AB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESAB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-AB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Albacete in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-AB
- Province of Albacete
exact_mappings:
- dpv_loc:ES-AB
- dpv_loc_owl:ES-AB
is_a: ES
class_uri: loc:ES-AB

```
</details>

### Induced

<details>
```yaml
name: ESAB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-AB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Albacete in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-AB
- Province of Albacete
exact_mappings:
- dpv_loc:ES-AB
- dpv_loc_owl:ES-AB
is_a: ES
class_uri: loc:ES-AB

```
</details></div>