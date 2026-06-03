---
search:
  boost: 10.0
---

# Class: PoliticalAffiliation 


_Information about political affiliation and history_



<div data-search-exclude markdown="1">



URI: [pd:PoliticalAffiliation](https://w3id.org/lmodel/dpv/pd/PoliticalAffiliation)





```mermaid
 classDiagram
    class PoliticalAffiliation
    click PoliticalAffiliation href "../PoliticalAffiliation/"
      PublicLife <|-- PoliticalAffiliation
        click PublicLife href "../PublicLife/"
      
      
```





## Inheritance
* **PoliticalAffiliation** [ [PublicLife](PublicLife.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PoliticalAffiliation](https://w3id.org/lmodel/dpv/pd/PoliticalAffiliation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Political Affiliation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PoliticalAffiliation |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PoliticalAffiliation |
| native | pd:PoliticalAffiliation |
| exact | dpv_pd:PoliticalAffiliation, dpv_pd_owl:PoliticalAffiliation |
| related | svd:Political |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PoliticalAffiliation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PoliticalAffiliation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about political affiliation and history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Political Affiliation
exact_mappings:
- dpv_pd:PoliticalAffiliation
- dpv_pd_owl:PoliticalAffiliation
related_mappings:
- svd:Political
mixins:
- PublicLife
class_uri: pd:PoliticalAffiliation

```
</details>

### Induced

<details>
```yaml
name: PoliticalAffiliation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PoliticalAffiliation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about political affiliation and history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Political Affiliation
exact_mappings:
- dpv_pd:PoliticalAffiliation
- dpv_pd_owl:PoliticalAffiliation
related_mappings:
- svd:Political
mixins:
- PublicLife
class_uri: pd:PoliticalAffiliation

```
</details></div>