---
search:
  boost: 10.0
---

# Class: SocialStatus 


_Information about social status_



<div data-search-exclude markdown="1">



URI: [pd:SocialStatus](https://w3id.org/lmodel/dpv/pd/SocialStatus)





```mermaid
 classDiagram
    class SocialStatus
    click SocialStatus href "../SocialStatus/"
      PublicLife <|-- SocialStatus
        click PublicLife href "../PublicLife/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [PublicLife](PublicLife.md)
        * **SocialStatus**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:SocialStatus](https://w3id.org/lmodel/dpv/pd/SocialStatus) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Social Status




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#SocialStatus |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:SocialStatus |
| native | pd:SocialStatus |
| exact | dpv_pd:SocialStatus, dpv_pd_owl:SocialStatus |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SocialStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SocialStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about social status
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social Status
exact_mappings:
- dpv_pd:SocialStatus
- dpv_pd_owl:SocialStatus
is_a: PublicLife
class_uri: pd:SocialStatus

```
</details>

### Induced

<details>
```yaml
name: SocialStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SocialStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about social status
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social Status
exact_mappings:
- dpv_pd:SocialStatus
- dpv_pd_owl:SocialStatus
is_a: PublicLife
class_uri: pd:SocialStatus

```
</details></div>