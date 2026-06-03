---
search:
  boost: 10.0
---

# Class: ModelInteractionBias 


_Bias that occurs from the structure of a model to create biased_

_predictions_



<div data-search-exclude markdown="1">



URI: [ai:ModelInteractionBias](https://w3id.org/lmodel/dpv/ai/ModelInteractionBias)





```mermaid
 classDiagram
    class ModelInteractionBias
    click ModelInteractionBias href "../ModelInteractionBias/"
      RiskConcept <|-- ModelInteractionBias
        click RiskConcept href "../RiskConcept/"
      EngineeringDecisionBias <|-- ModelInteractionBias
        click EngineeringDecisionBias href "../EngineeringDecisionBias/"
      

      ModelInteractionBias <|-- ModelExpressivenessBias
        click ModelExpressivenessBias href "../ModelExpressivenessBias/"
      

      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [AIBias](AIBias.md)
        * [EngineeringDecisionBias](EngineeringDecisionBias.md) [ [RiskConcept](RiskConcept.md)]
            * **ModelInteractionBias** [ [RiskConcept](RiskConcept.md)]
                * [ModelExpressivenessBias](ModelExpressivenessBias.md) [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ModelInteractionBias](https://w3id.org/lmodel/dpv/ai/ModelInteractionBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Model Interaction Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/ai/owl#ModelInteractionBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ModelInteractionBias |
| native | ai:ModelInteractionBias |
| exact | dpv_ai:ModelInteractionBias, dpv_ai_owl:ModelInteractionBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModelInteractionBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ModelInteractionBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs from the structure of a model to create biased

  predictions'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Model Interaction Bias
exact_mappings:
- dpv_ai:ModelInteractionBias
- dpv_ai_owl:ModelInteractionBias
is_a: EngineeringDecisionBias
mixins:
- RiskConcept
class_uri: ai:ModelInteractionBias

```
</details>

### Induced

<details>
```yaml
name: ModelInteractionBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ModelInteractionBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs from the structure of a model to create biased

  predictions'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Model Interaction Bias
exact_mappings:
- dpv_ai:ModelInteractionBias
- dpv_ai_owl:ModelInteractionBias
is_a: EngineeringDecisionBias
mixins:
- RiskConcept
class_uri: ai:ModelInteractionBias

```
</details></div>