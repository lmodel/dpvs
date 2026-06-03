---
search:
  boost: 10.0
---

# Class: UID 


_Information about unique identifiers_



<div data-search-exclude markdown="1">



URI: [pd:UID](https://w3id.org/lmodel/dpv/pd/UID)





```mermaid
 classDiagram
    class UID
    click UID href "../UID/"
      Identifying <|-- UID
        click Identifying href "../Identifying/"
      
      
```





## Inheritance
* [External](External.md)
    * [Identifying](Identifying.md)
        * **UID**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:UID](https://w3id.org/lmodel/dpv/pd/UID) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* UID




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#UID |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:UID |
| native | pd:UID |
| exact | dpv_pd:UID, dpv_pd_owl:UID |
| related | svd:UniqueId |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UID
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#UID
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about unique identifiers
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- UID
exact_mappings:
- dpv_pd:UID
- dpv_pd_owl:UID
related_mappings:
- svd:UniqueId
is_a: Identifying
class_uri: pd:UID

```
</details>

### Induced

<details>
```yaml
name: UID
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#UID
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about unique identifiers
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- UID
exact_mappings:
- dpv_pd:UID
- dpv_pd_owl:UID
related_mappings:
- svd:UniqueId
is_a: Identifying
class_uri: pd:UID

```
</details></div>