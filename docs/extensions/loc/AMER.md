---
search:
  boost: 10.0
---

# Class: AMER 


_Concept representing region Yerevan in country Armenia_



<div data-search-exclude markdown="1">



URI: [loc:AM-ER](https://w3id.org/lmodel/dpv/loc/AM-ER)





```mermaid
 classDiagram
    class AMER
    click AMER href "../AMER/"
      AM <|-- AMER
        click AM href "../AM/"
      
      
```





## Inheritance
* [AM](AM.md)
    * **AMER**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AM-ER](https://w3id.org/lmodel/dpv/loc/AM-ER) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* AM-ER
* Yerevan




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AM-ER |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AM-ER |
| native | loc:AMER |
| exact | dpv_loc:AM-ER, dpv_loc_owl:AM-ER |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AMER
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AM-ER
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Yerevan in country Armenia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AM-ER
- Yerevan
exact_mappings:
- dpv_loc:AM-ER
- dpv_loc_owl:AM-ER
is_a: AM
class_uri: loc:AM-ER

```
</details>

### Induced

<details>
```yaml
name: AMER
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AM-ER
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Yerevan in country Armenia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AM-ER
- Yerevan
exact_mappings:
- dpv_loc:AM-ER
- dpv_loc_owl:AM-ER
is_a: AM
class_uri: loc:AM-ER

```
</details></div>