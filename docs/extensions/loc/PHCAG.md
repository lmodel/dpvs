---
search:
  boost: 10.0
---

# Class: PHCAG 


_Concept representing region Cagayan (province) in country Philippines_



<div data-search-exclude markdown="1">



URI: [loc:PH-CAG](https://w3id.org/lmodel/dpv/loc/PH-CAG)





```mermaid
 classDiagram
    class PHCAG
    click PHCAG href "../PHCAG/"
      PH <|-- PHCAG
        click PH href "../PH/"
      
      
```





## Inheritance
* [PH](PH.md)
    * **PHCAG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PH-CAG](https://w3id.org/lmodel/dpv/loc/PH-CAG) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* PH-CAG
* Cagayan (province)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PH-CAG |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PH-CAG |
| native | loc:PHCAG |
| exact | dpv_loc:PH-CAG, dpv_loc_owl:PH-CAG |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PHCAG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PH-CAG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Cagayan (province) in country Philippines
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PH-CAG
- Cagayan (province)
exact_mappings:
- dpv_loc:PH-CAG
- dpv_loc_owl:PH-CAG
is_a: PH
class_uri: loc:PH-CAG

```
</details>

### Induced

<details>
```yaml
name: PHCAG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PH-CAG
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Cagayan (province) in country Philippines
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PH-CAG
- Cagayan (province)
exact_mappings:
- dpv_loc:PH-CAG
- dpv_loc_owl:PH-CAG
is_a: PH
class_uri: loc:PH-CAG

```
</details></div>