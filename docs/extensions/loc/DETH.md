---
search:
  boost: 10.0
---

# Class: DETH 


_Concept representing region Thuringia in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-TH](https://w3id.org/lmodel/dpv/loc/DE-TH)





```mermaid
 classDiagram
    class DETH
    click DETH href "../DETH/"
      DE <|-- DETH
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DETH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-TH](https://w3id.org/lmodel/dpv/loc/DE-TH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-TH
* Thuringia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-TH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-TH |
| native | loc:DETH |
| exact | dpv_loc:DE-TH, dpv_loc_owl:DE-TH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DETH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-TH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Thuringia in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-TH
- Thuringia
exact_mappings:
- dpv_loc:DE-TH
- dpv_loc_owl:DE-TH
is_a: DE
class_uri: loc:DE-TH

```
</details>

### Induced

<details>
```yaml
name: DETH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-TH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Thuringia in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-TH
- Thuringia
exact_mappings:
- dpv_loc:DE-TH
- dpv_loc_owl:DE-TH
is_a: DE
class_uri: loc:DE-TH

```
</details></div>