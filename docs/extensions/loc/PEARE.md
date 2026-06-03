---
search:
  boost: 10.0
---

# Class: PEARE 


_Concept representing region Arequipa Region in country Peru_



<div data-search-exclude markdown="1">



URI: [loc:PE-ARE](https://w3id.org/lmodel/dpv/loc/PE-ARE)





```mermaid
 classDiagram
    class PEARE
    click PEARE href "../PEARE/"
      PE <|-- PEARE
        click PE href "../PE/"
      
      
```





## Inheritance
* [PE](PE.md)
    * **PEARE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PE-ARE](https://w3id.org/lmodel/dpv/loc/PE-ARE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* PE-ARE
* Arequipa Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PE-ARE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PE-ARE |
| native | loc:PEARE |
| exact | dpv_loc:PE-ARE, dpv_loc_owl:PE-ARE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PEARE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PE-ARE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Arequipa Region in country Peru
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PE-ARE
- Arequipa Region
exact_mappings:
- dpv_loc:PE-ARE
- dpv_loc_owl:PE-ARE
is_a: PE
class_uri: loc:PE-ARE

```
</details>

### Induced

<details>
```yaml
name: PEARE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PE-ARE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Arequipa Region in country Peru
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PE-ARE
- Arequipa Region
exact_mappings:
- dpv_loc:PE-ARE
- dpv_loc_owl:PE-ARE
is_a: PE
class_uri: loc:PE-ARE

```
</details></div>