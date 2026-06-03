---
search:
  boost: 10.0
---

# Class: ITSV 


_Concept representing region Province of Savona in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-SV](https://w3id.org/lmodel/dpv/loc/IT-SV)





```mermaid
 classDiagram
    class ITSV
    click ITSV href "../ITSV/"
      IT <|-- ITSV
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITSV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-SV](https://w3id.org/lmodel/dpv/loc/IT-SV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-SV
* Province of Savona




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-SV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-SV |
| native | loc:ITSV |
| exact | dpv_loc:IT-SV, dpv_loc_owl:IT-SV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITSV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Savona in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SV
- Province of Savona
exact_mappings:
- dpv_loc:IT-SV
- dpv_loc_owl:IT-SV
is_a: IT
class_uri: loc:IT-SV

```
</details>

### Induced

<details>
```yaml
name: ITSV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-SV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Savona in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-SV
- Province of Savona
exact_mappings:
- dpv_loc:IT-SV
- dpv_loc_owl:IT-SV
is_a: IT
class_uri: loc:IT-SV

```
</details></div>