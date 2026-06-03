---
search:
  boost: 10.0
---

# Class: ITAV 


_Concept representing region Province of Avellino in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-AV](https://w3id.org/lmodel/dpv/loc/IT-AV)





```mermaid
 classDiagram
    class ITAV
    click ITAV href "../ITAV/"
      IT <|-- ITAV
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITAV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-AV](https://w3id.org/lmodel/dpv/loc/IT-AV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-AV
* Province of Avellino




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-AV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-AV |
| native | loc:ITAV |
| exact | dpv_loc:IT-AV, dpv_loc_owl:IT-AV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITAV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Avellino in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AV
- Province of Avellino
exact_mappings:
- dpv_loc:IT-AV
- dpv_loc_owl:IT-AV
is_a: IT
class_uri: loc:IT-AV

```
</details>

### Induced

<details>
```yaml
name: ITAV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-AV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Province of Avellino in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-AV
- Province of Avellino
exact_mappings:
- dpv_loc:IT-AV
- dpv_loc_owl:IT-AV
is_a: IT
class_uri: loc:IT-AV

```
</details></div>