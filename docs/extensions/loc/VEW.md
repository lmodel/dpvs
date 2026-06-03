---
search:
  boost: 10.0
---

# Class: VEW 


_Concept representing region Federal dependencies of Venezuela in country_

_Venezuela (Bolivarian Republic of)_



<div data-search-exclude markdown="1">



URI: [loc:VE-W](https://w3id.org/lmodel/dpv/loc/VE-W)





```mermaid
 classDiagram
    class VEW
    click VEW href "../VEW/"
      VE <|-- VEW
        click VE href "../VE/"
      
      
```





## Inheritance
* [VE](VE.md)
    * **VEW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:VE-W](https://w3id.org/lmodel/dpv/loc/VE-W) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* VE-W
* Federal dependencies of Venezuela




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#VE-W |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:VE-W |
| native | loc:VEW |
| exact | dpv_loc:VE-W, dpv_loc_owl:VE-W |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VEW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VE-W
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Federal dependencies of Venezuela in country

  Venezuela (Bolivarian Republic of)'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- VE-W
- Federal dependencies of Venezuela
exact_mappings:
- dpv_loc:VE-W
- dpv_loc_owl:VE-W
is_a: VE
class_uri: loc:VE-W

```
</details>

### Induced

<details>
```yaml
name: VEW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VE-W
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region Federal dependencies of Venezuela in country

  Venezuela (Bolivarian Republic of)'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- VE-W
- Federal dependencies of Venezuela
exact_mappings:
- dpv_loc:VE-W
- dpv_loc_owl:VE-W
is_a: VE
class_uri: loc:VE-W

```
</details></div>