---
search:
  boost: 10.0
---

# Class: DEBW 


_Concept representing region Baden-Württemberg in country Germany_



<div data-search-exclude markdown="1">



URI: [loc:DE-BW](https://w3id.org/lmodel/dpv/loc/DE-BW)





```mermaid
 classDiagram
    class DEBW
    click DEBW href "../DEBW/"
      DE <|-- DEBW
        click DE href "../DE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [DE](DE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **DEBW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DE-BW](https://w3id.org/lmodel/dpv/loc/DE-BW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DE-BW
* Baden-Württemberg




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DE-BW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DE-BW |
| native | loc:DEBW |
| exact | dpv_loc:DE-BW, dpv_loc_owl:DE-BW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DEBW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-BW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Baden-Württemberg in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-BW
- Baden-Württemberg
exact_mappings:
- dpv_loc:DE-BW
- dpv_loc_owl:DE-BW
is_a: DE
class_uri: loc:DE-BW

```
</details>

### Induced

<details>
```yaml
name: DEBW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DE-BW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Baden-Württemberg in country Germany
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DE-BW
- Baden-Württemberg
exact_mappings:
- dpv_loc:DE-BW
- dpv_loc_owl:DE-BW
is_a: DE
class_uri: loc:DE-BW

```
</details></div>