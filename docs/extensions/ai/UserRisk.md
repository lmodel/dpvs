---
search:
  boost: 10.0
---

# Class: UserRisk 


_Risks associated with Users of AI Systems_



<div data-search-exclude markdown="1">



URI: [ai:UserRisk](https://w3id.org/lmodel/dpv/ai/UserRisk)





```mermaid
 classDiagram
    class UserRisk
    click UserRisk href "../UserRisk/"
      RiskConcept <|-- UserRisk
        click RiskConcept href "../RiskConcept/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * **UserRisk**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:UserRisk](https://w3id.org/lmodel/dpv/ai/UserRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* User Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#UserRisk |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:UserRisk |
| native | ai:UserRisk |
| exact | dpv_ai:UserRisk, dpv_ai_owl:UserRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UserRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#UserRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Risks associated with Users of AI Systems
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- User Risk
exact_mappings:
- dpv_ai:UserRisk
- dpv_ai_owl:UserRisk
is_a: RiskConcept
class_uri: ai:UserRisk

```
</details>

### Induced

<details>
```yaml
name: UserRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#UserRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Risks associated with Users of AI Systems
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- User Risk
exact_mappings:
- dpv_ai:UserRisk
- dpv_ai_owl:UserRisk
is_a: RiskConcept
class_uri: ai:UserRisk

```
</details></div>