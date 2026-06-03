---
search:
  boost: 10.0
---

# Class: ESMA 


_Concept representing region Province of Málaga in country Spain_



<div data-search-exclude markdown="1">



URI: [loc:ES-MA](https://w3id.org/lmodel/dpv/loc/ES-MA)





```mermaid
 classDiagram
    class ESMA
    click ESMA href "../ESMA/"
      ES <|-- ESMA
        click ES href "../ES/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [ES](ES.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ESMA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ES-MA](https://w3id.org/lmodel/dpv/loc/ES-MA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* ES-MA
* Province of Málaga




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ES-MA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ES-MA |
| native | loc:ESMA |
| exact | dpv_loc:ES-MA, dpv_loc_owl:ES-MA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ESMA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-MA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Málaga in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-MA
- Province of Málaga
exact_mappings:
- dpv_loc:ES-MA
- dpv_loc_owl:ES-MA
is_a: ES
class_uri: loc:ES-MA

```
</details>

### Induced

<details>
```yaml
name: ESMA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ES-MA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Málaga in country Spain
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- ES-MA
- Province of Málaga
exact_mappings:
- dpv_loc:ES-MA
- dpv_loc_owl:ES-MA
is_a: ES
class_uri: loc:ES-MA

```
</details></div>