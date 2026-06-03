---
search:
  boost: 10.0
---

# Class: AIBias 


_Bias associated with development, use, or other activities involving an_

_AI technology or system_



<div data-search-exclude markdown="1">



URI: [ai:AIBias](https://w3id.org/lmodel/dpv/ai/AIBias)





```mermaid
 classDiagram
    class AIBias
    click AIBias href "../AIBias/"
      RiskConcept <|-- AIBias
        click RiskConcept href "../RiskConcept/"
      

      AIBias <|-- AutomationBias
        click AutomationBias href "../AutomationBias/"
      AIBias <|-- DataBias
        click DataBias href "../DataBias/"
      AIBias <|-- EngineeringDecisionBias
        click EngineeringDecisionBias href "../EngineeringDecisionBias/"
      

      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * **AIBias**
        * [AutomationBias](AutomationBias.md) [ [RiskConcept](RiskConcept.md)]
        * [DataBias](DataBias.md) [ [RiskConcept](RiskConcept.md)]
        * [EngineeringDecisionBias](EngineeringDecisionBias.md) [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:AIBias](https://w3id.org/lmodel/dpv/ai/AIBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* AI Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#AIBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:AIBias |
| native | ai:AIBias |
| exact | dpv_ai:AIBias, dpv_ai_owl:AIBias |
| close | iso42001:AIRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AIBias
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AIBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias associated with development, use, or other activities involving
  an

  AI technology or system'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- AI Bias
exact_mappings:
- dpv_ai:AIBias
- dpv_ai_owl:AIBias
close_mappings:
- iso42001:AIRisk
is_a: RiskConcept
class_uri: ai:AIBias

```
</details>

### Induced

<details>
```yaml
name: AIBias
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AIBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias associated with development, use, or other activities involving
  an

  AI technology or system'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- AI Bias
exact_mappings:
- dpv_ai:AIBias
- dpv_ai_owl:AIBias
close_mappings:
- iso42001:AIRisk
is_a: RiskConcept
class_uri: ai:AIBias

```
</details></div>