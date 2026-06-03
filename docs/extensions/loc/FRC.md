---
search:
  boost: 10.0
---

# Class: FRC 


_Concept representing region Auvergne in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-C](https://w3id.org/lmodel/dpv/loc/FR-C)





```mermaid
 classDiagram
    class FRC
    click FRC href "../FRC/"
      FR <|-- FRC
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRC**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-C](https://w3id.org/lmodel/dpv/loc/FR-C) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-C
* Auvergne




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-C |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-C |
| native | loc:FRC |
| exact | dpv_loc:FR-C, dpv_loc_owl:FR-C |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Auvergne in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-C
- Auvergne
exact_mappings:
- dpv_loc:FR-C
- dpv_loc_owl:FR-C
is_a: FR
class_uri: loc:FR-C

```
</details>

### Induced

<details>
```yaml
name: FRC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-C
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Auvergne in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-C
- Auvergne
exact_mappings:
- dpv_loc:FR-C
- dpv_loc_owl:FR-C
is_a: FR
class_uri: loc:FR-C

```
</details></div>