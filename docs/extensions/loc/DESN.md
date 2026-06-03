---
search:
  boost: 10.0
---

# Class: DESN 


_Concept representing region Saxony in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-SN](https://w3id.org/lmodel/dpv/loc/DE-SN)





```mermaid
 classDiagram
    class DESN
    click DESN href "../DESN/"
      DE <|-- DESN
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DESN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-SN](https://w3id.org/lmodel/dpv/loc/DE-SN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-SN
* Saxony




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-SN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-SN |
| native | loc:DESN |
| exact | dpv_loc:DE-SN, dpv_loc_owl:DE-SN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DESN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-SN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saxony in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-SN
- Saxony
exact_mappings:
- dpv_loc:DE-SN
- dpv_loc_owl:DE-SN
is_a: DE
class_uri: loc:DE-SN

```
</details>

### Induced

<details>
```yaml
name: DESN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-SN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Saxony in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-SN
- Saxony
exact_mappings:
- dpv_loc:DE-SN
- dpv_loc_owl:DE-SN
is_a: DE
class_uri: loc:DE-SN

```
</details></div>