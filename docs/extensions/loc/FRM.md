---
search:
  boost: 10.0
---

# Class: FRM 


_Concept representing region Lorraine in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-M](https://w3id.org/lmodel/dpv/loc/FR-M)





```mermaid
 classDiagram
    class FRM
    click FRM href "../FRM/"
      FR <|-- FRM
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-M](https://w3id.org/lmodel/dpv/loc/FR-M) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-M
* Lorraine




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-M |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-M |
| native | loc:FRM |
| exact | dpv_loc:FR-M, dpv_loc_owl:FR-M |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-M
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Lorraine in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-M
- Lorraine
exact_mappings:
- dpv_loc:FR-M
- dpv_loc_owl:FR-M
is_a: FR
class_uri: loc:FR-M

```
</details>

### Induced

<details>
```yaml
name: FRM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-M
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Lorraine in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-M
- Lorraine
exact_mappings:
- dpv_loc:FR-M
- dpv_loc_owl:FR-M
is_a: FR
class_uri: loc:FR-M

```
</details></div>