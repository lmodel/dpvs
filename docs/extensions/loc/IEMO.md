---
search:
  boost: 10.0
---

# Class: IEMO 


_Concept representing region County Mayo in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-MO](https://w3id.org/lmodel/dpv/loc/IE-MO)





```mermaid
 classDiagram
    class IEMO
    click IEMO href "../IEMO/"
      IE <|-- IEMO
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IEMO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-MO](https://w3id.org/lmodel/dpv/loc/IE-MO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-MO
* County Mayo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-MO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-MO |
| native | loc:IEMO |
| exact | dpv_loc:IE-MO, dpv_loc_owl:IE-MO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IEMO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Mayo in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-MO
- County Mayo
exact_mappings:
- dpv_loc:IE-MO
- dpv_loc_owl:IE-MO
is_a: IE
class_uri: loc:IE-MO

```
</details>

### Induced

<details>
```yaml
name: IEMO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-MO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Mayo in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-MO
- County Mayo
exact_mappings:
- dpv_loc:IE-MO
- dpv_loc_owl:IE-MO
is_a: IE
class_uri: loc:IE-MO

```
</details></div>