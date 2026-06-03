---
search:
  boost: 10.0
---

# Class: DEHE 


_Concept representing region Hesse in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-HE](https://w3id.org/lmodel/dpv/loc/DE-HE)





```mermaid
 classDiagram
    class DEHE
    click DEHE href "../DEHE/"
      DE <|-- DEHE
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DEHE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-HE](https://w3id.org/lmodel/dpv/loc/DE-HE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-HE
* Hesse




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-HE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-HE |
| native | loc:DEHE |
| exact | dpv_loc:DE-HE, dpv_loc_owl:DE-HE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DEHE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-HE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hesse in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-HE
- Hesse
exact_mappings:
- dpv_loc:DE-HE
- dpv_loc_owl:DE-HE
is_a: DE
class_uri: loc:DE-HE

```
</details>

### Induced

<details>
```yaml
name: DEHE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-HE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hesse in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-HE
- Hesse
exact_mappings:
- dpv_loc:DE-HE
- dpv_loc_owl:DE-HE
is_a: DE
class_uri: loc:DE-HE

```
</details></div>