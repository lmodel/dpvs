---
search:
  boost: 10.0
---

# Class: PoliticalOpinion 


_Information about opinions regarding politics and political topics_



<div data-search-exclude markdown="1">



URI: [pd:PoliticalOpinion](https://w3id.org/lmodel/dpv/pd/PoliticalOpinion)





```mermaid
 classDiagram
    class PoliticalOpinion
    click PoliticalOpinion href "../PoliticalOpinion/"
      PublicLife <|-- PoliticalOpinion
        click PublicLife href "../PublicLife/"
      
      
```





## Inheritance
* **PoliticalOpinion** [ [PublicLife](PublicLife.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PoliticalOpinion](https://w3id.org/lmodel/dpv/pd/PoliticalOpinion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Political Opinion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PoliticalOpinion |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PoliticalOpinion |
| native | pd:PoliticalOpinion |
| exact | dpv_pd:PoliticalOpinion, dpv_pd_owl:PoliticalOpinion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PoliticalOpinion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PoliticalOpinion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about opinions regarding politics and political topics
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Political Opinion
exact_mappings:
- dpv_pd:PoliticalOpinion
- dpv_pd_owl:PoliticalOpinion
mixins:
- PublicLife
class_uri: pd:PoliticalOpinion

```
</details>

### Induced

<details>
```yaml
name: PoliticalOpinion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PoliticalOpinion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about opinions regarding politics and political topics
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Political Opinion
exact_mappings:
- dpv_pd:PoliticalOpinion
- dpv_pd_owl:PoliticalOpinion
mixins:
- PublicLife
class_uri: pd:PoliticalOpinion

```
</details></div>