---
search:
  boost: 10.0
---

# Class: IECN 


_Concept representing region County Cavan in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-CN](https://w3id.org/lmodel/dpv/loc/IE-CN)





```mermaid
 classDiagram
    class IECN
    click IECN href "../IECN/"
      IE <|-- IECN
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IECN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-CN](https://w3id.org/lmodel/dpv/loc/IE-CN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-CN
* County Cavan




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-CN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-CN |
| native | loc:IECN |
| exact | dpv_loc:IE-CN, dpv_loc_owl:IE-CN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IECN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-CN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Cavan in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-CN
- County Cavan
exact_mappings:
- dpv_loc:IE-CN
- dpv_loc_owl:IE-CN
is_a: IE
class_uri: loc:IE-CN

```
</details>

### Induced

<details>
```yaml
name: IECN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-CN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Cavan in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-CN
- County Cavan
exact_mappings:
- dpv_loc:IE-CN
- dpv_loc_owl:IE-CN
is_a: IE
class_uri: loc:IE-CN

```
</details></div>