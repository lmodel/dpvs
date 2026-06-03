---
search:
  boost: 10.0
---

# Class: NonResponseBias 


_Bias that occurs when people from certain groups opt-out of surveys at_

_different rates than users from other groups. This is also called as_

_Participation bias_



<div data-search-exclude markdown="1">



URI: [risk:NonResponseBias](https://w3id.org/lmodel/dpv/risk/NonResponseBias)





```mermaid
 classDiagram
    class NonResponseBias
    click NonResponseBias href "../NonResponseBias/"
      PotentialConsequence <|-- NonResponseBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- NonResponseBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- NonResponseBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      SelectionBias <|-- NonResponseBias
        click SelectionBias href "../SelectionBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * [StatisticalBias](StatisticalBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [SelectionBias](SelectionBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                    * **NonResponseBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:NonResponseBias](https://w3id.org/lmodel/dpv/risk/NonResponseBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Non-Response Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#NonResponseBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:NonResponseBias |
| native | risk:NonResponseBias |
| exact | dpv_risk:NonResponseBias, dpv_risk_owl:NonResponseBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NonResponseBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#NonResponseBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when people from certain groups opt-out of surveys
  at

  different rates than users from other groups. This is also called as

  Participation bias'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Non-Response Bias
exact_mappings:
- dpv_risk:NonResponseBias
- dpv_risk_owl:NonResponseBias
is_a: SelectionBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:NonResponseBias

```
</details>

### Induced

<details>
```yaml
name: NonResponseBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#NonResponseBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when people from certain groups opt-out of surveys
  at

  different rates than users from other groups. This is also called as

  Participation bias'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Non-Response Bias
exact_mappings:
- dpv_risk:NonResponseBias
- dpv_risk_owl:NonResponseBias
is_a: SelectionBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:NonResponseBias

```
</details></div>