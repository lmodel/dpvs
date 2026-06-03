---
search:
  boost: 10.0
---

# Class: DEBY 


_Concept representing region Bavaria in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-BY](https://w3id.org/lmodel/dpv/loc/DE-BY)





```mermaid
 classDiagram
    class DEBY
    click DEBY href "../DEBY/"
      DE <|-- DEBY
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DEBY**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-BY](https://w3id.org/lmodel/dpv/loc/DE-BY) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-BY
* Bavaria




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-BY |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-BY |
| native | loc:DEBY |
| exact | dpv_loc:DE-BY, dpv_loc_owl:DE-BY |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DEBY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-BY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bavaria in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-BY
- Bavaria
exact_mappings:
- dpv_loc:DE-BY
- dpv_loc_owl:DE-BY
is_a: DE
class_uri: loc:DE-BY

```
</details>

### Induced

<details>
```yaml
name: DEBY
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-BY
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bavaria in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-BY
- Bavaria
exact_mappings:
- dpv_loc:DE-BY
- dpv_loc_owl:DE-BY
is_a: DE
class_uri: loc:DE-BY

```
</details></div>