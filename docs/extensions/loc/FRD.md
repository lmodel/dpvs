---
search:
  boost: 10.0
---

# Class: FRD 


_Concept representing region Bourgogne in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-D](https://w3id.org/lmodel/dpv/loc/FR-D)





```mermaid
 classDiagram
    class FRD
    click FRD href "../FRD/"
      FR <|-- FRD
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRD**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-D](https://w3id.org/lmodel/dpv/loc/FR-D) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-D
* Bourgogne




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-D |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-D |
| native | loc:FRD |
| exact | dpv_loc:FR-D, dpv_loc_owl:FR-D |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-D
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bourgogne in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-D
- Bourgogne
exact_mappings:
- dpv_loc:FR-D
- dpv_loc_owl:FR-D
is_a: FR
class_uri: loc:FR-D

```
</details>

### Induced

<details>
```yaml
name: FRD
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-D
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bourgogne in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-D
- Bourgogne
exact_mappings:
- dpv_loc:FR-D
- dpv_loc_owl:FR-D
is_a: FR
class_uri: loc:FR-D

```
</details></div>