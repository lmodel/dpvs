---
search:
  boost: 10.0
---

# Class: PEAMA 


_Concept representing region Amazonas Region in country Peru_



<div data-search-exclude markdown="1">



URI: [loc:PE-AMA](https://w3id.org/lmodel/dpv/loc/PE-AMA)





```mermaid
 classDiagram
    class PEAMA
    click PEAMA href "../PEAMA/"
      PE <|-- PEAMA
        click PE href "../PE/"
      
      
```





## Inheritance
* [PE](PE.md)
    * **PEAMA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PE-AMA](https://w3id.org/lmodel/dpv/loc/PE-AMA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* PE-AMA
* Amazonas Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PE-AMA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PE-AMA |
| native | loc:PEAMA |
| exact | dpv_loc:PE-AMA, dpv_loc_owl:PE-AMA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PEAMA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PE-AMA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Amazonas Region in country Peru
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PE-AMA
- Amazonas Region
exact_mappings:
- dpv_loc:PE-AMA
- dpv_loc_owl:PE-AMA
is_a: PE
class_uri: loc:PE-AMA

```
</details>

### Induced

<details>
```yaml
name: PEAMA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PE-AMA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Amazonas Region in country Peru
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PE-AMA
- Amazonas Region
exact_mappings:
- dpv_loc:PE-AMA
- dpv_loc_owl:PE-AMA
is_a: PE
class_uri: loc:PE-AMA

```
</details></div>