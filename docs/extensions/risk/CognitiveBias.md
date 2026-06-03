---
search:
  boost: 10.0
---

# Class: CognitiveBias 


_Bias that occurs when humans are processing and interpreting information_



<div data-search-exclude markdown="1">



URI: [risk:CognitiveBias](https://w3id.org/lmodel/dpv/risk/CognitiveBias)





```mermaid
 classDiagram
    class CognitiveBias
    click CognitiveBias href "../CognitiveBias/"
      PotentialConsequence <|-- CognitiveBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- CognitiveBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- CognitiveBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      Bias <|-- CognitiveBias
        click Bias href "../Bias/"
      

      CognitiveBias <|-- ConfirmationBias
        click ConfirmationBias href "../ConfirmationBias/"
      CognitiveBias <|-- GroupAttributionBias
        click GroupAttributionBias href "../GroupAttributionBias/"
      CognitiveBias <|-- ImplicitBias
        click ImplicitBias href "../ImplicitBias/"
      CognitiveBias <|-- InGroupBias
        click InGroupBias href "../InGroupBias/"
      CognitiveBias <|-- OutGroupHomogeneityBias
        click OutGroupHomogeneityBias href "../OutGroupHomogeneityBias/"
      CognitiveBias <|-- RequirementsBias
        click RequirementsBias href "../RequirementsBias/"
      CognitiveBias <|-- RuleBasedSystemDesign
        click RuleBasedSystemDesign href "../RuleBasedSystemDesign/"
      CognitiveBias <|-- SocietalBias
        click SocietalBias href "../SocietalBias/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **CognitiveBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [ConfirmationBias](ConfirmationBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [GroupAttributionBias](GroupAttributionBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [ImplicitBias](ImplicitBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [InGroupBias](InGroupBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [OutGroupHomogeneityBias](OutGroupHomogeneityBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [RequirementsBias](RequirementsBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [RuleBasedSystemDesign](RuleBasedSystemDesign.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [SocietalBias](SocietalBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:CognitiveBias](https://w3id.org/lmodel/dpv/risk/CognitiveBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Cognitive Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#CognitiveBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:CognitiveBias |
| native | risk:CognitiveBias |
| exact | dpv_risk:CognitiveBias, dpv_risk_owl:CognitiveBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CognitiveBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CognitiveBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Bias that occurs when humans are processing and interpreting information
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Cognitive Bias
exact_mappings:
- dpv_risk:CognitiveBias
- dpv_risk_owl:CognitiveBias
is_a: Bias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:CognitiveBias

```
</details>

### Induced

<details>
```yaml
name: CognitiveBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CognitiveBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Bias that occurs when humans are processing and interpreting information
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Cognitive Bias
exact_mappings:
- dpv_risk:CognitiveBias
- dpv_risk_owl:CognitiveBias
is_a: Bias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:CognitiveBias

```
</details></div>