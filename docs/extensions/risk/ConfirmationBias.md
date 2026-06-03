---
search:
  boost: 10.0
---

# Class: ConfirmationBias 


_Bias that occurs when hypotheses, regardless of their veracity, are more_

_likely to be confirmed by the intentional or unintentional_

_interpretation of information_



<div data-search-exclude markdown="1">



URI: [risk:ConfirmationBias](https://w3id.org/lmodel/dpv/risk/ConfirmationBias)





```mermaid
 classDiagram
    class ConfirmationBias
    click ConfirmationBias href "../ConfirmationBias/"
      PotentialConsequence <|-- ConfirmationBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ConfirmationBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ConfirmationBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      CognitiveBias <|-- ConfirmationBias
        click CognitiveBias href "../CognitiveBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [CognitiveBias](CognitiveBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **ConfirmationBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ConfirmationBias](https://w3id.org/lmodel/dpv/risk/ConfirmationBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Confirmation Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#ConfirmationBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ConfirmationBias |
| native | risk:ConfirmationBias |
| exact | dpv_risk:ConfirmationBias, dpv_risk_owl:ConfirmationBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConfirmationBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ConfirmationBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when hypotheses, regardless of their veracity, are
  more

  likely to be confirmed by the intentional or unintentional

  interpretation of information'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Confirmation Bias
exact_mappings:
- dpv_risk:ConfirmationBias
- dpv_risk_owl:ConfirmationBias
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ConfirmationBias

```
</details>

### Induced

<details>
```yaml
name: ConfirmationBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ConfirmationBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when hypotheses, regardless of their veracity, are
  more

  likely to be confirmed by the intentional or unintentional

  interpretation of information'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Confirmation Bias
exact_mappings:
- dpv_risk:ConfirmationBias
- dpv_risk_owl:ConfirmationBias
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ConfirmationBias

```
</details></div>