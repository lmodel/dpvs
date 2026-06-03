---
search:
  boost: 10.0
---

# Class: MDSN 


_Concept representing region Transnistria in country Republic of Moldova_



<div data-search-exclude markdown="1">



URI: [loc:MD-SN](https://w3id.org/lmodel/dpv/loc/MD-SN)





```mermaid
 classDiagram
    class MDSN
    click MDSN href "../MDSN/"
      MD <|-- MDSN
        click MD href "../MD/"
      
      
```





## Inheritance
* [MD](MD.md)
    * **MDSN**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MD-SN](https://w3id.org/lmodel/dpv/loc/MD-SN) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* MD-SN
* Transnistria




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MD-SN |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MD-SN |
| native | loc:MDSN |
| exact | dpv_loc:MD-SN, dpv_loc_owl:MD-SN |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MDSN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MD-SN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Transnistria in country Republic of Moldova
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MD-SN
- Transnistria
exact_mappings:
- dpv_loc:MD-SN
- dpv_loc_owl:MD-SN
is_a: MD
class_uri: loc:MD-SN

```
</details>

### Induced

<details>
```yaml
name: MDSN
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MD-SN
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Transnistria in country Republic of Moldova
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- MD-SN
- Transnistria
exact_mappings:
- dpv_loc:MD-SN
- dpv_loc_owl:MD-SN
is_a: MD
class_uri: loc:MD-SN

```
</details></div>