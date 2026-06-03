---
search:
  boost: 10.0
---

# Class: DEBB 


_Concept representing region Brandenburg in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-BB](https://w3id.org/lmodel/dpv/loc/DE-BB)





```mermaid
 classDiagram
    class DEBB
    click DEBB href "../DEBB/"
      DE <|-- DEBB
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DEBB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-BB](https://w3id.org/lmodel/dpv/loc/DE-BB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-BB
* Brandenburg




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-BB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-BB |
| native | loc:DEBB |
| exact | dpv_loc:DE-BB, dpv_loc_owl:DE-BB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DEBB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-BB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Brandenburg in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-BB
- Brandenburg
exact_mappings:
- dpv_loc:DE-BB
- dpv_loc_owl:DE-BB
is_a: DE
class_uri: loc:DE-BB

```
</details>

### Induced

<details>
```yaml
name: DEBB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-BB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Brandenburg in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-BB
- Brandenburg
exact_mappings:
- dpv_loc:DE-BB
- dpv_loc_owl:DE-BB
is_a: DE
class_uri: loc:DE-BB

```
</details></div>