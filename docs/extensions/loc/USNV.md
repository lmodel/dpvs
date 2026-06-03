---
search:
  boost: 10.0
---

# Class: USNV 


_Concept representing region Nevada in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-NV](https://w3id.org/lmodel/dpv/loc/US-NV)





```mermaid
 classDiagram
    class USNV
    click USNV href "../USNV/"
      US <|-- USNV
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USNV**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-NV](https://w3id.org/lmodel/dpv/loc/US-NV) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-NV
* Nevada




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-NV |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-NV |
| native | loc:USNV |
| exact | dpv_loc:US-NV, dpv_loc_owl:US-NV |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USNV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nevada in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NV
- Nevada
exact_mappings:
- dpv_loc:US-NV
- dpv_loc_owl:US-NV
is_a: US
class_uri: loc:US-NV

```
</details>

### Induced

<details>
```yaml
name: USNV
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-NV
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Nevada in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-NV
- Nevada
exact_mappings:
- dpv_loc:US-NV
- dpv_loc_owl:US-NV
is_a: US
class_uri: loc:US-NV

```
</details></div>