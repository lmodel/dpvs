---
search:
  boost: 10.0
---

# Class: IEMN 


_Concept representing region County Monaghan in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-MN](https://w3id.org/lmodel/dpv/loc/IE-MN)





```mermaid
 classDiagram
    class IEMN
    click IEMN href "../IEMN/"
      IE <|-- IEMN
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IEMN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-MN](https://w3id.org/lmodel/dpv/loc/IE-MN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-MN
* County Monaghan




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-MN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-MN |
| native | loc:IEMN |
| exact | dpv_loc:IE-MN, dpv_loc_owl:IE-MN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IEMN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-MN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Monaghan in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-MN
- County Monaghan
exact_mappings:
- dpv_loc:IE-MN
- dpv_loc_owl:IE-MN
is_a: IE
class_uri: loc:IE-MN

```
</details>

### Induced

<details>
```yaml
name: IEMN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-MN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Monaghan in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-MN
- County Monaghan
exact_mappings:
- dpv_loc:IE-MN
- dpv_loc_owl:IE-MN
is_a: IE
class_uri: loc:IE-MN

```
</details></div>