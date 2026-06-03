---
search:
  boost: 10.0
---

# Class: DEHB 


_Concept representing region Bremen (state) in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-HB](https://w3id.org/lmodel/dpv/loc/DE-HB)





```mermaid
 classDiagram
    class DEHB
    click DEHB href "../DEHB/"
      DE <|-- DEHB
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DEHB**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-HB](https://w3id.org/lmodel/dpv/loc/DE-HB) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-HB
* Bremen (state)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-HB |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-HB |
| native | loc:DEHB |
| exact | dpv_loc:DE-HB, dpv_loc_owl:DE-HB |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DEHB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-HB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bremen (state) in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-HB
- Bremen (state)
exact_mappings:
- dpv_loc:DE-HB
- dpv_loc_owl:DE-HB
is_a: DE
class_uri: loc:DE-HB

```
</details>

### Induced

<details>
```yaml
name: DEHB
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-HB
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Bremen (state) in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-HB
- Bremen (state)
exact_mappings:
- dpv_loc:DE-HB
- dpv_loc_owl:DE-HB
is_a: DE
class_uri: loc:DE-HB

```
</details></div>