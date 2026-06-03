---
search:
  boost: 10.0
---

# Class: DEHH 


_Concept representing region Hamburg in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-HH](https://w3id.org/lmodel/dpv/loc/DE-HH)





```mermaid
 classDiagram
    class DEHH
    click DEHH href "../DEHH/"
      DE <|-- DEHH
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DEHH**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-HH](https://w3id.org/lmodel/dpv/loc/DE-HH) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-HH
* Hamburg




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-HH |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-HH |
| native | loc:DEHH |
| exact | dpv_loc:DE-HH, dpv_loc_owl:DE-HH |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DEHH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-HH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hamburg in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-HH
- Hamburg
exact_mappings:
- dpv_loc:DE-HH
- dpv_loc_owl:DE-HH
is_a: DE
class_uri: loc:DE-HH

```
</details>

### Induced

<details>
```yaml
name: DEHH
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-HH
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Hamburg in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-HH
- Hamburg
exact_mappings:
- dpv_loc:DE-HH
- dpv_loc_owl:DE-HH
is_a: DE
class_uri: loc:DE-HH

```
</details></div>