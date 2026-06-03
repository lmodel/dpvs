---
search:
  boost: 10.0
---

# Class: EngineeringDecisionBias 


_Bias that occurs due to machine learning model architectures -_

_encompassing all model specifications, parameters and manually designed_

_features_



<div data-search-exclude markdown="1">



URI: [ai:EngineeringDecisionBias](https://w3id.org/lmodel/dpv/ai/EngineeringDecisionBias)





```mermaid
 classDiagram
    class EngineeringDecisionBias
    click EngineeringDecisionBias href "../EngineeringDecisionBias/"
      RiskConcept <|-- EngineeringDecisionBias
        click RiskConcept href "../RiskConcept/"
      AIBias <|-- EngineeringDecisionBias
        click AIBias href "../AIBias/"
      

      EngineeringDecisionBias <|-- AlgorithmSelectionBias
        click AlgorithmSelectionBias href "../AlgorithmSelectionBias/"
      EngineeringDecisionBias <|-- FeatureEngineeringBias
        click FeatureEngineeringBias href "../FeatureEngineeringBias/"
      EngineeringDecisionBias <|-- HyperparameterTuningBias
        click HyperparameterTuningBias href "../HyperparameterTuningBias/"
      EngineeringDecisionBias <|-- InformativenessBias
        click InformativenessBias href "../InformativenessBias/"
      EngineeringDecisionBias <|-- ModelBias
        click ModelBias href "../ModelBias/"
      EngineeringDecisionBias <|-- ModelInteractionBias
        click ModelInteractionBias href "../ModelInteractionBias/"
      

      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [AIBias](AIBias.md)
        * **EngineeringDecisionBias** [ [RiskConcept](RiskConcept.md)]
            * [AlgorithmSelectionBias](AlgorithmSelectionBias.md) [ [RiskConcept](RiskConcept.md)]
            * [FeatureEngineeringBias](FeatureEngineeringBias.md) [ [RiskConcept](RiskConcept.md)]
            * [HyperparameterTuningBias](HyperparameterTuningBias.md) [ [RiskConcept](RiskConcept.md)]
            * [InformativenessBias](InformativenessBias.md) [ [RiskConcept](RiskConcept.md)]
            * [ModelBias](ModelBias.md) [ [RiskConcept](RiskConcept.md)]
            * [ModelInteractionBias](ModelInteractionBias.md) [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:EngineeringDecisionBias](https://w3id.org/lmodel/dpv/ai/EngineeringDecisionBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Engineering Decision Bias


## Comments

* Data bias and human cognitive bias can contribute to such bias



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/ai/owl#EngineeringDecisionBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:EngineeringDecisionBias |
| native | ai:EngineeringDecisionBias |
| exact | dpv_ai:EngineeringDecisionBias, dpv_ai_owl:EngineeringDecisionBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EngineeringDecisionBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#EngineeringDecisionBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs due to machine learning model architectures -

  encompassing all model specifications, parameters and manually designed

  features'
comments:
- Data bias and human cognitive bias can contribute to such bias
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Engineering Decision Bias
exact_mappings:
- dpv_ai:EngineeringDecisionBias
- dpv_ai_owl:EngineeringDecisionBias
is_a: AIBias
mixins:
- RiskConcept
class_uri: ai:EngineeringDecisionBias

```
</details>

### Induced

<details>
```yaml
name: EngineeringDecisionBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#EngineeringDecisionBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Bias that occurs due to machine learning model architectures -

  encompassing all model specifications, parameters and manually designed

  features'
comments:
- Data bias and human cognitive bias can contribute to such bias
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Engineering Decision Bias
exact_mappings:
- dpv_ai:EngineeringDecisionBias
- dpv_ai_owl:EngineeringDecisionBias
is_a: AIBias
mixins:
- RiskConcept
class_uri: ai:EngineeringDecisionBias

```
</details></div>