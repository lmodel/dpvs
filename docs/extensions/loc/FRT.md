---
search:
  boost: 10.0
---

# Class: FRT 


_Concept representing region Poitou-Charentes in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-T](https://w3id.org/lmodel/dpv/loc/FR-T)





```mermaid
 classDiagram
    class FRT
    click FRT href "../FRT/"
      FR <|-- FRT
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-T](https://w3id.org/lmodel/dpv/loc/FR-T) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-T
* Poitou-Charentes




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-T |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-T |
| native | loc:FRT |
| exact | dpv_loc:FR-T, dpv_loc_owl:FR-T |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-T
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Poitou-Charentes in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-T
- Poitou-Charentes
exact_mappings:
- dpv_loc:FR-T
- dpv_loc_owl:FR-T
is_a: FR
class_uri: loc:FR-T

```
</details>

### Induced

<details>
```yaml
name: FRT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-T
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Poitou-Charentes in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-T
- Poitou-Charentes
exact_mappings:
- dpv_loc:FR-T
- dpv_loc_owl:FR-T
is_a: FR
class_uri: loc:FR-T

```
</details></div>