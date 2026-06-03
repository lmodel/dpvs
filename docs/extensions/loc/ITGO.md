---
search:
  boost: 10.0
---

# Class: ITGO 


_Concept representing region Province of Gorizia in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-GO](https://w3id.org/lmodel/dpv/loc/IT-GO)





```mermaid
 classDiagram
    class ITGO
    click ITGO href "../ITGO/"
      IT <|-- ITGO
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITGO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-GO](https://w3id.org/lmodel/dpv/loc/IT-GO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-GO
* Province of Gorizia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-GO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-GO |
| native | loc:ITGO |
| exact | dpv_loc:IT-GO, dpv_loc_owl:IT-GO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITGO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-GO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Gorizia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-GO
- Province of Gorizia
exact_mappings:
- dpv_loc:IT-GO
- dpv_loc_owl:IT-GO
is_a: IT
class_uri: loc:IT-GO

```
</details>

### Induced

<details>
```yaml
name: ITGO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-GO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Gorizia in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-GO
- Province of Gorizia
exact_mappings:
- dpv_loc:IT-GO
- dpv_loc_owl:IT-GO
is_a: IT
class_uri: loc:IT-GO

```
</details></div>