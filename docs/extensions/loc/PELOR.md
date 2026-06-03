---
search:
  boost: 10.0
---

# Class: PELOR 


_Concept representing region Loreto Region in country Peru_



<div data-search-exclude markdown="1">



URI: [loc:PE-LOR](https://w3id.org/lmodel/dpv/loc/PE-LOR)





```mermaid
 classDiagram
    class PELOR
    click PELOR href "../PELOR/"
      PE <|-- PELOR
        click PE href "../PE/"
      
      
```





## Inheritance
* [PE](PE.md)
    * **PELOR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PE-LOR](https://w3id.org/lmodel/dpv/loc/PE-LOR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* PE-LOR
* Loreto Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PE-LOR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PE-LOR |
| native | loc:PELOR |
| exact | dpv_loc:PE-LOR, dpv_loc_owl:PE-LOR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PELOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PE-LOR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Loreto Region in country Peru
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PE-LOR
- Loreto Region
exact_mappings:
- dpv_loc:PE-LOR
- dpv_loc_owl:PE-LOR
is_a: PE
class_uri: loc:PE-LOR

```
</details>

### Induced

<details>
```yaml
name: PELOR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PE-LOR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Loreto Region in country Peru
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- PE-LOR
- Loreto Region
exact_mappings:
- dpv_loc:PE-LOR
- dpv_loc_owl:PE-LOR
is_a: PE
class_uri: loc:PE-LOR

```
</details></div>