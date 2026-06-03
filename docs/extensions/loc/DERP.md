---
search:
  boost: 10.0
---

# Class: DERP 


_Concept representing region Rhineland-Palatinate in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-RP](https://w3id.org/lmodel/dpv/loc/DE-RP)





```mermaid
 classDiagram
    class DERP
    click DERP href "../DERP/"
      DE <|-- DERP
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DERP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-RP](https://w3id.org/lmodel/dpv/loc/DE-RP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-RP
* Rhineland-Palatinate




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-RP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-RP |
| native | loc:DERP |
| exact | dpv_loc:DE-RP, dpv_loc_owl:DE-RP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DERP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-RP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Rhineland-Palatinate in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-RP
- Rhineland-Palatinate
exact_mappings:
- dpv_loc:DE-RP
- dpv_loc_owl:DE-RP
is_a: DE
class_uri: loc:DE-RP

```
</details>

### Induced

<details>
```yaml
name: DERP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-RP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Rhineland-Palatinate in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-RP
- Rhineland-Palatinate
exact_mappings:
- dpv_loc:DE-RP
- dpv_loc_owl:DE-RP
is_a: DE
class_uri: loc:DE-RP

```
</details></div>