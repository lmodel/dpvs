---
search:
  boost: 10.0
---

# Class: NonNormalityBias 


_Bias that occurs when the dataset is subject to a different (i.e._

_non-normal) distribution (e.g., Chi-Square, Beta, Lorentz, Cauchy,_

_Weibull or Pareto) where the results can be biased and misleading_



<div data-search-exclude markdown="1">



URI: [risk:NonNormalityBias](https://w3id.org/lmodel/dpv/risk/NonNormalityBias)





```mermaid
 classDiagram
    class NonNormalityBias
    click NonNormalityBias href "../NonNormalityBias/"
      PotentialConsequence <|-- NonNormalityBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- NonNormalityBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- NonNormalityBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      StatisticalBias <|-- NonNormalityBias
        click StatisticalBias href "../StatisticalBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * [StatisticalBias](StatisticalBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **NonNormalityBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:NonNormalityBias](https://w3id.org/lmodel/dpv/risk/NonNormalityBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Non-Normality Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#NonNormalityBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:NonNormalityBias |
| native | risk:NonNormalityBias |
| exact | dpv_risk:NonNormalityBias, dpv_risk_owl:NonNormalityBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NonNormalityBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#NonNormalityBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when the dataset is subject to a different (i.e.

  non-normal) distribution (e.g., Chi-Square, Beta, Lorentz, Cauchy,

  Weibull or Pareto) where the results can be biased and misleading'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Non-Normality Bias
exact_mappings:
- dpv_risk:NonNormalityBias
- dpv_risk_owl:NonNormalityBias
is_a: StatisticalBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:NonNormalityBias

```
</details>

### Induced

<details>
```yaml
name: NonNormalityBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#NonNormalityBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when the dataset is subject to a different (i.e.

  non-normal) distribution (e.g., Chi-Square, Beta, Lorentz, Cauchy,

  Weibull or Pareto) where the results can be biased and misleading'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Non-Normality Bias
exact_mappings:
- dpv_risk:NonNormalityBias
- dpv_risk_owl:NonNormalityBias
is_a: StatisticalBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:NonNormalityBias

```
</details></div>