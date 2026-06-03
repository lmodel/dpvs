---
search:
  boost: 10.0
---

# Class: IEMH 


_Concept representing region County Meath in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-MH](https://w3id.org/lmodel/dpv/loc/IE-MH)





```mermaid
 classDiagram
    class IEMH
    click IEMH href "../IEMH/"
      IE <|-- IEMH
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IEMH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-MH](https://w3id.org/lmodel/dpv/loc/IE-MH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-MH
* County Meath




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-MH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-MH |
| native | loc:IEMH |
| exact | dpv_loc:IE-MH, dpv_loc_owl:IE-MH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IEMH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-MH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Meath in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-MH
- County Meath
exact_mappings:
- dpv_loc:IE-MH
- dpv_loc_owl:IE-MH
is_a: IE
class_uri: loc:IE-MH

```
</details>

### Induced

<details>
```yaml
name: IEMH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-MH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Meath in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-MH
- County Meath
exact_mappings:
- dpv_loc:IE-MH
- dpv_loc_owl:IE-MH
is_a: IE
class_uri: loc:IE-MH

```
</details></div>