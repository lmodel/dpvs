---
search:
  boost: 10.0
---

# Class: FRG 


_Concept representing region Champagne-Ardenne in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-G](https://w3id.org/lmodel/dpv/loc/FR-G)





```mermaid
 classDiagram
    class FRG
    click FRG href "../FRG/"
      FR <|-- FRG
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-G](https://w3id.org/lmodel/dpv/loc/FR-G) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-G
* Champagne-Ardenne




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-G |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-G |
| native | loc:FRG |
| exact | dpv_loc:FR-G, dpv_loc_owl:FR-G |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-G
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Champagne-Ardenne in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-G
- Champagne-Ardenne
exact_mappings:
- dpv_loc:FR-G
- dpv_loc_owl:FR-G
is_a: FR
class_uri: loc:FR-G

```
</details>

### Induced

<details>
```yaml
name: FRG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-G
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Champagne-Ardenne in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-G
- Champagne-Ardenne
exact_mappings:
- dpv_loc:FR-G
- dpv_loc_owl:FR-G
is_a: FR
class_uri: loc:FR-G

```
</details></div>