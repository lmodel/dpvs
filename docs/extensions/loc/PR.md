---
search:
  boost: 10.0
---

# Class: PR 


_Concept representing Country of Puerto Rico_



<div data-search-exclude markdown="1">



URI: [loc:PR](https://w3id.org/lmodel/dpv/loc/PR)





```mermaid
 classDiagram
    class PR
    click PR href "../PR/"
      US <|-- PR
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **PR**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:PR](https://w3id.org/lmodel/dpv/loc/PR) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Puerto Rico




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#PR |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:PR |
| native | loc:PR |
| exact | dpv_loc:PR, dpv_loc_owl:PR |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Puerto Rico
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Puerto Rico
exact_mappings:
- dpv_loc:PR
- dpv_loc_owl:PR
is_a: US
class_uri: loc:PR

```
</details>

### Induced

<details>
```yaml
name: PR
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#PR
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Puerto Rico
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Puerto Rico
exact_mappings:
- dpv_loc:PR
- dpv_loc_owl:PR
is_a: US
class_uri: loc:PR

```
</details></div>