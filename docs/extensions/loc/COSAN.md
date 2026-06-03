---
search:
  boost: 10.0
---

# Class: COSAN 


_Concept representing region Santander Department in country Colombia_



<div data-search-exclude markdown="1">



URI: [loc:CO-SAN](https://w3id.org/lmodel/dpv/loc/CO-SAN)





```mermaid
 classDiagram
    class COSAN
    click COSAN href "../COSAN/"
      CO <|-- COSAN
        click CO href "../CO/"
      
      
```





## Inheritance
* [CO](CO.md)
    * **COSAN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CO-SAN](https://w3id.org/lmodel/dpv/loc/CO-SAN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CO-SAN
* Santander Department




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CO-SAN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CO-SAN |
| native | loc:COSAN |
| exact | dpv_loc:CO-SAN, dpv_loc_owl:CO-SAN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: COSAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CO-SAN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Santander Department in country Colombia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CO-SAN
- Santander Department
exact_mappings:
- dpv_loc:CO-SAN
- dpv_loc_owl:CO-SAN
is_a: CO
class_uri: loc:CO-SAN

```
</details>

### Induced

<details>
```yaml
name: COSAN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CO-SAN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Santander Department in country Colombia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CO-SAN
- Santander Department
exact_mappings:
- dpv_loc:CO-SAN
- dpv_loc_owl:CO-SAN
is_a: CO
class_uri: loc:CO-SAN

```
</details></div>