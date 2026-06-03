---
search:
  boost: 10.0
---

# Class: AISystemRisk 


_Risks associated with AI Systems_



<div data-search-exclude markdown="1">



URI: [ai:AISystemRisk](https://w3id.org/lmodel/dpv/ai/AISystemRisk)





```mermaid
 classDiagram
    class AISystemRisk
    click AISystemRisk href "../AISystemRisk/"
      RiskConcept <|-- AISystemRisk
        click RiskConcept href "../RiskConcept/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * **AISystemRisk**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:AISystemRisk](https://w3id.org/lmodel/dpv/ai/AISystemRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* AI System Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#AISystemRisk |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:AISystemRisk |
| native | ai:AISystemRisk |
| exact | dpv_ai:AISystemRisk, dpv_ai_owl:AISystemRisk, iso42001:AIRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AISystemRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AISystemRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Risks associated with AI Systems
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- AI System Risk
exact_mappings:
- dpv_ai:AISystemRisk
- dpv_ai_owl:AISystemRisk
- iso42001:AIRisk
is_a: RiskConcept
class_uri: ai:AISystemRisk

```
</details>

### Induced

<details>
```yaml
name: AISystemRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AISystemRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Risks associated with AI Systems
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- AI System Risk
exact_mappings:
- dpv_ai:AISystemRisk
- dpv_ai_owl:AISystemRisk
- iso42001:AIRisk
is_a: RiskConcept
class_uri: ai:AISystemRisk

```
</details></div>