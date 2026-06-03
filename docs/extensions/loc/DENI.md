---
search:
  boost: 10.0
---

# Class: DENI 


_Concept representing region Lower Saxony in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-NI](https://w3id.org/lmodel/dpv/loc/DE-NI)





```mermaid
 classDiagram
    class DENI
    click DENI href "../DENI/"
      DE <|-- DENI
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DENI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-NI](https://w3id.org/lmodel/dpv/loc/DE-NI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-NI
* Lower Saxony




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-NI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-NI |
| native | loc:DENI |
| exact | dpv_loc:DE-NI, dpv_loc_owl:DE-NI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DENI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-NI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Lower Saxony in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-NI
- Lower Saxony
exact_mappings:
- dpv_loc:DE-NI
- dpv_loc_owl:DE-NI
is_a: DE
class_uri: loc:DE-NI

```
</details>

### Induced

<details>
```yaml
name: DENI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-NI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Lower Saxony in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-NI
- Lower Saxony
exact_mappings:
- dpv_loc:DE-NI
- dpv_loc_owl:DE-NI
is_a: DE
class_uri: loc:DE-NI

```
</details></div>