---
search:
  boost: 10.0
---

# Class: NLZE 


_Concept representing region Zeeland in country Netherlands_



<div data-search-exclude markdown="1">



URI: [loc:NL-ZE](https://w3id.org/lmodel/dpv/loc/NL-ZE)





```mermaid
 classDiagram
    class NLZE
    click NLZE href "../NLZE/"
      NL <|-- NLZE
        click NL href "../NL/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [NL](NL.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **NLZE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:NL-ZE](https://w3id.org/lmodel/dpv/loc/NL-ZE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* NL-ZE
* Zeeland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#NL-ZE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:NL-ZE |
| native | loc:NLZE |
| exact | dpv_loc:NL-ZE, dpv_loc_owl:NL-ZE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NLZE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-ZE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Zeeland in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-ZE
- Zeeland
exact_mappings:
- dpv_loc:NL-ZE
- dpv_loc_owl:NL-ZE
is_a: NL
class_uri: loc:NL-ZE

```
</details>

### Induced

<details>
```yaml
name: NLZE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#NL-ZE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Zeeland in country Netherlands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- NL-ZE
- Zeeland
exact_mappings:
- dpv_loc:NL-ZE
- dpv_loc_owl:NL-ZE
is_a: NL
class_uri: loc:NL-ZE

```
</details></div>