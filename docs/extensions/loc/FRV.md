---
search:
  boost: 10.0
---

# Class: FRV 


_Concept representing region Rhône-Alpes in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-V](https://w3id.org/lmodel/dpv/loc/FR-V)





```mermaid
 classDiagram
    class FRV
    click FRV href "../FRV/"
      FR <|-- FRV
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-V](https://w3id.org/lmodel/dpv/loc/FR-V) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-V
* Rhône-Alpes




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-V |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-V |
| native | loc:FRV |
| exact | dpv_loc:FR-V, dpv_loc_owl:FR-V |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-V
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Rhône-Alpes in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-V
- Rhône-Alpes
exact_mappings:
- dpv_loc:FR-V
- dpv_loc_owl:FR-V
is_a: FR
class_uri: loc:FR-V

```
</details>

### Induced

<details>
```yaml
name: FRV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-V
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Rhône-Alpes in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-V
- Rhône-Alpes
exact_mappings:
- dpv_loc:FR-V
- dpv_loc_owl:FR-V
is_a: FR
class_uri: loc:FR-V

```
</details></div>