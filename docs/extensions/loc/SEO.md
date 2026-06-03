---
search:
  boost: 10.0
---

# Class: SEO 


_Concept representing region Västra Götaland County in country Sweden_



<div data-search-exclude markdown="1">



URI: [loc:SE-O](https://w3id.org/lmodel/dpv/loc/SE-O)





```mermaid
 classDiagram
    class SEO
    click SEO href "../SEO/"
      SE <|-- SEO
        click SE href "../SE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [SE](SE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **SEO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SE-O](https://w3id.org/lmodel/dpv/loc/SE-O) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* SE-O
* Västra Götaland County




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SE-O |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SE-O |
| native | loc:SEO |
| exact | dpv_loc:SE-O, dpv_loc_owl:SE-O |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SEO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-O
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Västra Götaland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-O
- Västra Götaland County
exact_mappings:
- dpv_loc:SE-O
- dpv_loc_owl:SE-O
is_a: SE
class_uri: loc:SE-O

```
</details>

### Induced

<details>
```yaml
name: SEO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SE-O
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Västra Götaland County in country Sweden
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- SE-O
- Västra Götaland County
exact_mappings:
- dpv_loc:SE-O
- dpv_loc_owl:SE-O
is_a: SE
class_uri: loc:SE-O

```
</details></div>