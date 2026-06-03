---
search:
  boost: 10.0
---

# Class: ITTO 


_Concept representing region Metropolitan city of Turin in country Italy_



<div data-search-exclude markdown="1">



URI: [loc:IT-TO](https://w3id.org/lmodel/dpv/loc/IT-TO)





```mermaid
 classDiagram
    class ITTO
    click ITTO href "../ITTO/"
      IT <|-- ITTO
        click IT href "../IT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IT](IT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **ITTO**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IT-TO](https://w3id.org/lmodel/dpv/loc/IT-TO) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IT-TO
* Metropolitan city of Turin




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IT-TO |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IT-TO |
| native | loc:ITTO |
| exact | dpv_loc:IT-TO, dpv_loc_owl:IT-TO |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ITTO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Metropolitan city of Turin in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TO
- Metropolitan city of Turin
exact_mappings:
- dpv_loc:IT-TO
- dpv_loc_owl:IT-TO
is_a: IT
class_uri: loc:IT-TO

```
</details>

### Induced

<details>
```yaml
name: ITTO
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IT-TO
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Metropolitan city of Turin in country Italy
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IT-TO
- Metropolitan city of Turin
exact_mappings:
- dpv_loc:IT-TO
- dpv_loc_owl:IT-TO
is_a: IT
class_uri: loc:IT-TO

```
</details></div>