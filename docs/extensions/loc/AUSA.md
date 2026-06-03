---
search:
  boost: 10.0
---

# Class: AUSA 


_Concept representing region South Australia in country Australia_



<div data-search-exclude markdown="1">



URI: [loc:AU-SA](https://w3id.org/lmodel/dpv/loc/AU-SA)





```mermaid
 classDiagram
    class AUSA
    click AUSA href "../AUSA/"
      AU <|-- AUSA
        click AU href "../AU/"
      
      
```





## Inheritance
* [AU](AU.md)
    * **AUSA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AU-SA](https://w3id.org/lmodel/dpv/loc/AU-SA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* AU-SA
* South Australia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AU-SA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AU-SA |
| native | loc:AUSA |
| exact | dpv_loc:AU-SA, dpv_loc_owl:AU-SA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AUSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AU-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region South Australia in country Australia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AU-SA
- South Australia
exact_mappings:
- dpv_loc:AU-SA
- dpv_loc_owl:AU-SA
is_a: AU
class_uri: loc:AU-SA

```
</details>

### Induced

<details>
```yaml
name: AUSA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AU-SA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region South Australia in country Australia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AU-SA
- South Australia
exact_mappings:
- dpv_loc:AU-SA
- dpv_loc_owl:AU-SA
is_a: AU
class_uri: loc:AU-SA

```
</details></div>