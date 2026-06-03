---
search:
  boost: 10.0
---

# Class: DESH 


_Concept representing region Schleswig-Holstein in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-SH](https://w3id.org/lmodel/dpv/loc/DE-SH)





```mermaid
 classDiagram
    class DESH
    click DESH href "../DESH/"
      DE <|-- DESH
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DESH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-SH](https://w3id.org/lmodel/dpv/loc/DE-SH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-SH
* Schleswig-Holstein




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-SH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-SH |
| native | loc:DESH |
| exact | dpv_loc:DE-SH, dpv_loc_owl:DE-SH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DESH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-SH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Schleswig-Holstein in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-SH
- Schleswig-Holstein
exact_mappings:
- dpv_loc:DE-SH
- dpv_loc_owl:DE-SH
is_a: DE
class_uri: loc:DE-SH

```
</details>

### Induced

<details>
```yaml
name: DESH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-SH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Schleswig-Holstein in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-SH
- Schleswig-Holstein
exact_mappings:
- dpv_loc:DE-SH
- dpv_loc_owl:DE-SH
is_a: DE
class_uri: loc:DE-SH

```
</details></div>