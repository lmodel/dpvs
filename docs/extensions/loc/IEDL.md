---
search:
  boost: 10.0
---

# Class: IEDL 


_Concept representing region County Donegal in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-DL](https://w3id.org/lmodel/dpv/loc/IE-DL)





```mermaid
 classDiagram
    class IEDL
    click IEDL href "../IEDL/"
      IE <|-- IEDL
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IEDL**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-DL](https://w3id.org/lmodel/dpv/loc/IE-DL) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-DL
* County Donegal




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-DL |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-DL |
| native | loc:IEDL |
| exact | dpv_loc:IE-DL, dpv_loc_owl:IE-DL |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IEDL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-DL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Donegal in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-DL
- County Donegal
exact_mappings:
- dpv_loc:IE-DL
- dpv_loc_owl:IE-DL
is_a: IE
class_uri: loc:IE-DL

```
</details>

### Induced

<details>
```yaml
name: IEDL
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-DL
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Donegal in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-DL
- County Donegal
exact_mappings:
- dpv_loc:IE-DL
- dpv_loc_owl:IE-DL
is_a: IE
class_uri: loc:IE-DL

```
</details></div>