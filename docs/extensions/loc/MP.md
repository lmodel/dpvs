---
search:
  boost: 10.0
---

# Class: MP 


_Concept representing Country of Northern Mariana Islands_



<div data-search-exclude markdown="1">



URI: [loc:MP](https://w3id.org/lmodel/dpv/loc/MP)





```mermaid
 classDiagram
    class MP
    click MP href "../MP/"
      US <|-- MP
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **MP**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:MP](https://w3id.org/lmodel/dpv/loc/MP) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Northern Mariana Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#MP |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:MP |
| native | loc:MP |
| exact | dpv_loc:MP, dpv_loc_owl:MP |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Northern Mariana Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Northern Mariana Islands
exact_mappings:
- dpv_loc:MP
- dpv_loc_owl:MP
is_a: US
class_uri: loc:MP

```
</details>

### Induced

<details>
```yaml
name: MP
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#MP
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Northern Mariana Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Northern Mariana Islands
exact_mappings:
- dpv_loc:MP
- dpv_loc_owl:MP
is_a: US
class_uri: loc:MP

```
</details></div>