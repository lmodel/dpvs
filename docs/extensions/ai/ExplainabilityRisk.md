---
search:
  boost: 10.0
---

# Class: ExplainabilityRisk 


_Risk that an AI's decisions or behaviors cannot be adequately_

_understood, interpreted, or justified by relevant stakeholders._



<div data-search-exclude markdown="1">



URI: [ai:ExplainabilityRisk](https://w3id.org/lmodel/dpv/ai/ExplainabilityRisk)





```mermaid
 classDiagram
    class ExplainabilityRisk
    click ExplainabilityRisk href "../ExplainabilityRisk/"
      RiskConcept <|-- ExplainabilityRisk
        click RiskConcept href "../RiskConcept/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * **ExplainabilityRisk**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ExplainabilityRisk](https://w3id.org/lmodel/dpv/ai/ExplainabilityRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Explainability Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ExplainabilityRisk |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ExplainabilityRisk |
| native | ai:ExplainabilityRisk |
| exact | dpv_ai:ExplainabilityRisk, dpv_ai_owl:ExplainabilityRisk |
| close | iso42001:AIRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExplainabilityRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ExplainabilityRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Risk that an AI''s decisions or behaviors cannot be adequately

  understood, interpreted, or justified by relevant stakeholders.'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Explainability Risk
exact_mappings:
- dpv_ai:ExplainabilityRisk
- dpv_ai_owl:ExplainabilityRisk
close_mappings:
- iso42001:AIRisk
is_a: RiskConcept
class_uri: ai:ExplainabilityRisk

```
</details>

### Induced

<details>
```yaml
name: ExplainabilityRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ExplainabilityRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Risk that an AI''s decisions or behaviors cannot be adequately

  understood, interpreted, or justified by relevant stakeholders.'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Explainability Risk
exact_mappings:
- dpv_ai:ExplainabilityRisk
- dpv_ai_owl:ExplainabilityRisk
close_mappings:
- iso42001:AIRisk
is_a: RiskConcept
class_uri: ai:ExplainabilityRisk

```
</details></div>