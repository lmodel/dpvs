---
search:
  boost: 10.0
---

# Class: DEMV 


_Concept representing region Mecklenburg-Vorpommern in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-MV](https://w3id.org/lmodel/dpv/loc/DE-MV)





```mermaid
 classDiagram
    class DEMV
    click DEMV href "../DEMV/"
      DE <|-- DEMV
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DEMV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-MV](https://w3id.org/lmodel/dpv/loc/DE-MV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-MV
* Mecklenburg-Western Pomerania




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-MV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-MV |
| native | loc:DEMV |
| exact | dpv_loc:DE-MV, dpv_loc_owl:DE-MV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DEMV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-MV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Mecklenburg-Vorpommern in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-MV
- Mecklenburg-Western Pomerania
exact_mappings:
- dpv_loc:DE-MV
- dpv_loc_owl:DE-MV
is_a: DE
class_uri: loc:DE-MV

```
</details>

### Induced

<details>
```yaml
name: DEMV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-MV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Mecklenburg-Vorpommern in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-MV
- Mecklenburg-Western Pomerania
exact_mappings:
- dpv_loc:DE-MV
- dpv_loc_owl:DE-MV
is_a: DE
class_uri: loc:DE-MV

```
</details></div>