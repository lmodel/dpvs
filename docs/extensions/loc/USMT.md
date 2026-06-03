---
search:
  boost: 10.0
---

# Class: USMT 


_Concept representing region Montana in country United States of America_



<div data-search-exclude markdown="1">



URI: [loc:US-MT](https://w3id.org/lmodel/dpv/loc/US-MT)





```mermaid
 classDiagram
    class USMT
    click USMT href "../USMT/"
      US <|-- USMT
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **USMT**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:US-MT](https://w3id.org/lmodel/dpv/loc/US-MT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* US-MT
* Montana




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#US-MT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:US-MT |
| native | loc:USMT |
| exact | dpv_loc:US-MT, dpv_loc_owl:US-MT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: USMT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Montana in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MT
- Montana
exact_mappings:
- dpv_loc:US-MT
- dpv_loc_owl:US-MT
is_a: US
class_uri: loc:US-MT

```
</details>

### Induced

<details>
```yaml
name: USMT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#US-MT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Montana in country United States of America
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- US-MT
- Montana
exact_mappings:
- dpv_loc:US-MT
- dpv_loc_owl:US-MT
is_a: US
class_uri: loc:US-MT

```
</details></div>