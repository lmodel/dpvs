---
search:
  boost: 10.0
---

# Class: IELM 


_Concept representing region County Leitrim in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-LM](https://w3id.org/lmodel/dpv/loc/IE-LM)





```mermaid
 classDiagram
    class IELM
    click IELM href "../IELM/"
      IE <|-- IELM
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IELM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-LM](https://w3id.org/lmodel/dpv/loc/IE-LM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-LM
* County Leitrim




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-LM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-LM |
| native | loc:IELM |
| exact | dpv_loc:IE-LM, dpv_loc_owl:IE-LM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IELM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-LM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Leitrim in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-LM
- County Leitrim
exact_mappings:
- dpv_loc:IE-LM
- dpv_loc_owl:IE-LM
is_a: IE
class_uri: loc:IE-LM

```
</details>

### Induced

<details>
```yaml
name: IELM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-LM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Leitrim in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-LM
- County Leitrim
exact_mappings:
- dpv_loc:IE-LM
- dpv_loc_owl:IE-LM
is_a: IE
class_uri: loc:IE-LM

```
</details></div>