---
search:
  boost: 10.0
---

# Class: IERN 


_Concept representing region County Roscommon in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-RN](https://w3id.org/lmodel/dpv/loc/IE-RN)





```mermaid
 classDiagram
    class IERN
    click IERN href "../IERN/"
      IE <|-- IERN
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IERN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-RN](https://w3id.org/lmodel/dpv/loc/IE-RN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-RN
* County Roscommon




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-RN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-RN |
| native | loc:IERN |
| exact | dpv_loc:IE-RN, dpv_loc_owl:IE-RN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IERN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-RN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Roscommon in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-RN
- County Roscommon
exact_mappings:
- dpv_loc:IE-RN
- dpv_loc_owl:IE-RN
is_a: IE
class_uri: loc:IE-RN

```
</details>

### Induced

<details>
```yaml
name: IERN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-RN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Roscommon in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-RN
- County Roscommon
exact_mappings:
- dpv_loc:IE-RN
- dpv_loc_owl:IE-RN
is_a: IE
class_uri: loc:IE-RN

```
</details></div>