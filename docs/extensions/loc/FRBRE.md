---
search:
  boost: 10.0
---

# Class: FRBRE 


_Concept representing region Région Bretagne in country France_



<div data-search-exclude markdown="1">



URI: [loc:FR-BRE](https://w3id.org/lmodel/dpv/loc/FR-BRE)





```mermaid
 classDiagram
    class FRBRE
    click FRBRE href "../FRBRE/"
      FR <|-- FRBRE
        click FR href "../FR/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [FR](FR.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **FRBRE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:FR-BRE](https://w3id.org/lmodel/dpv/loc/FR-BRE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* FR-BRE
* Région Bretagne




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#FR-BRE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:FR-BRE |
| native | loc:FRBRE |
| exact | dpv_loc:FR-BRE, dpv_loc_owl:FR-BRE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FRBRE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-BRE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Région Bretagne in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-BRE
- Région Bretagne
exact_mappings:
- dpv_loc:FR-BRE
- dpv_loc_owl:FR-BRE
is_a: FR
class_uri: loc:FR-BRE

```
</details>

### Induced

<details>
```yaml
name: FRBRE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#FR-BRE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Région Bretagne in country France
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- FR-BRE
- Région Bretagne
exact_mappings:
- dpv_loc:FR-BRE
- dpv_loc_owl:FR-BRE
is_a: FR
class_uri: loc:FR-BRE

```
</details></div>