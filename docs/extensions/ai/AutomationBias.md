---
search:
  boost: 10.0
---

# Class: AutomationBias 


_Bias that occurs due to propensity for humans to favour suggestions from_

_automated decision-making systems and to ignore contradictory_

_information made without automation, even if it is correct_



<div data-search-exclude markdown="1">



URI: [ai:AutomationBias](https://w3id.org/lmodel/dpv/ai/AutomationBias)





```mermaid
 classDiagram
    class AutomationBias
    click AutomationBias href "../AutomationBias/"
      RiskConcept <|-- AutomationBias
        click RiskConcept href "../RiskConcept/"
      AIBias <|-- AutomationBias
        click AIBias href "../AIBias/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [AIBias](AIBias.md)
        * **AutomationBias** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:AutomationBias](https://w3id.org/lmodel/dpv/ai/AutomationBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Automation Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/ai/owl#AutomationBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:AutomationBias |
| native | ai:AutomationBias |
| exact | dpv_ai:AutomationBias, dpv_ai_owl:AutomationBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AutomationBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AutomationBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs due to propensity for humans to favour suggestions
  from

  automated decision-making systems and to ignore contradictory

  information made without automation, even if it is correct'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Automation Bias
exact_mappings:
- dpv_ai:AutomationBias
- dpv_ai_owl:AutomationBias
is_a: AIBias
mixins:
- RiskConcept
class_uri: ai:AutomationBias

```
</details>

### Induced

<details>
```yaml
name: AutomationBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#AutomationBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs due to propensity for humans to favour suggestions
  from

  automated decision-making systems and to ignore contradictory

  information made without automation, even if it is correct'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Automation Bias
exact_mappings:
- dpv_ai:AutomationBias
- dpv_ai_owl:AutomationBias
is_a: AIBias
mixins:
- RiskConcept
class_uri: ai:AutomationBias

```
</details></div>