---
search:
  boost: 10.0
---

# Class: MaritalStatus 


_Information about marital status and history_



<div data-search-exclude markdown="1">



URI: [pd:MaritalStatus](https://w3id.org/lmodel/dpv/pd/MaritalStatus)





```mermaid
 classDiagram
    class MaritalStatus
    click MaritalStatus href "../MaritalStatus/"
      PublicLife <|-- MaritalStatus
        click PublicLife href "../PublicLife/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [PublicLife](PublicLife.md)
        * **MaritalStatus**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:MaritalStatus](https://w3id.org/lmodel/dpv/pd/MaritalStatus) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Marital Status




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#MaritalStatus |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:MaritalStatus |
| native | pd:MaritalStatus |
| exact | dpv_pd:MaritalStatus, dpv_pd_owl:MaritalStatus |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MaritalStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#MaritalStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about marital status and history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Marital Status
exact_mappings:
- dpv_pd:MaritalStatus
- dpv_pd_owl:MaritalStatus
is_a: PublicLife
class_uri: pd:MaritalStatus

```
</details>

### Induced

<details>
```yaml
name: MaritalStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#MaritalStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about marital status and history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Marital Status
exact_mappings:
- dpv_pd:MaritalStatus
- dpv_pd_owl:MaritalStatus
is_a: PublicLife
class_uri: pd:MaritalStatus

```
</details></div>