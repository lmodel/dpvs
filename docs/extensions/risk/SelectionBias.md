---
search:
  boost: 10.0
---

# Class: SelectionBias 


_Bias that occurs when a dataset's samples are chosen in a way that is_

_not reflective of their real-world distribution_



<div data-search-exclude markdown="1">



URI: [risk:SelectionBias](https://w3id.org/lmodel/dpv/risk/SelectionBias)





```mermaid
 classDiagram
    class SelectionBias
    click SelectionBias href "../SelectionBias/"
      PotentialConsequence <|-- SelectionBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SelectionBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SelectionBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      StatisticalBias <|-- SelectionBias
        click StatisticalBias href "../StatisticalBias/"
      

      SelectionBias <|-- CoverageBias
        click CoverageBias href "../CoverageBias/"
      SelectionBias <|-- NonResponseBias
        click NonResponseBias href "../NonResponseBias/"
      SelectionBias <|-- SamplingBias
        click SamplingBias href "../SamplingBias/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * [StatisticalBias](StatisticalBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **SelectionBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                    * [CoverageBias](CoverageBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                    * [NonResponseBias](NonResponseBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                    * [SamplingBias](SamplingBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SelectionBias](https://w3id.org/lmodel/dpv/risk/SelectionBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Selection Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#SelectionBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SelectionBias |
| native | risk:SelectionBias |
| exact | dpv_risk:SelectionBias, dpv_risk_owl:SelectionBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SelectionBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SelectionBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when a dataset''s samples are chosen in a way that
  is

  not reflective of their real-world distribution'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Selection Bias
exact_mappings:
- dpv_risk:SelectionBias
- dpv_risk_owl:SelectionBias
is_a: StatisticalBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SelectionBias

```
</details>

### Induced

<details>
```yaml
name: SelectionBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SelectionBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when a dataset''s samples are chosen in a way that
  is

  not reflective of their real-world distribution'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Selection Bias
exact_mappings:
- dpv_risk:SelectionBias
- dpv_risk_owl:SelectionBias
is_a: StatisticalBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SelectionBias

```
</details></div>