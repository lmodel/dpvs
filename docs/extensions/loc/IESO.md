---
search:
  boost: 10.0
---

# Class: IESO 


_Concept representing region County Sligo in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-SO](https://w3id.org/lmodel/dpv/loc/IE-SO)





```mermaid
 classDiagram
    class IESO
    click IESO href "../IESO/"
      IE <|-- IESO
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IESO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-SO](https://w3id.org/lmodel/dpv/loc/IE-SO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-SO
* County Sligo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-SO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-SO |
| native | loc:IESO |
| exact | dpv_loc:IE-SO, dpv_loc_owl:IE-SO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IESO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-SO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Sligo in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-SO
- County Sligo
exact_mappings:
- dpv_loc:IE-SO
- dpv_loc_owl:IE-SO
is_a: IE
class_uri: loc:IE-SO

```
</details>

### Induced

<details>
```yaml
name: IESO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-SO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Sligo in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-SO
- County Sligo
exact_mappings:
- dpv_loc:IE-SO
- dpv_loc_owl:IE-SO
is_a: IE
class_uri: loc:IE-SO

```
</details></div>