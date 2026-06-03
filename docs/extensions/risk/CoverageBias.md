---
search:
  boost: 10.0
---

# Class: CoverageBias 


_Bias that occurs when a population represented in a dataset does not_

_match the actual or real population that are being used_



<div data-search-exclude markdown="1">



URI: [risk:CoverageBias](https://w3id.org/lmodel/dpv/risk/CoverageBias)





```mermaid
 classDiagram
    class CoverageBias
    click CoverageBias href "../CoverageBias/"
      PotentialConsequence <|-- CoverageBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- CoverageBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- CoverageBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      SelectionBias <|-- CoverageBias
        click SelectionBias href "../SelectionBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * [StatisticalBias](StatisticalBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [SelectionBias](SelectionBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                    * **CoverageBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:CoverageBias](https://w3id.org/lmodel/dpv/risk/CoverageBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Coverage Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#CoverageBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:CoverageBias |
| native | risk:CoverageBias |
| exact | dpv_risk:CoverageBias, dpv_risk_owl:CoverageBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CoverageBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CoverageBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when a population represented in a dataset does not

  match the actual or real population that are being used'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Coverage Bias
exact_mappings:
- dpv_risk:CoverageBias
- dpv_risk_owl:CoverageBias
is_a: SelectionBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:CoverageBias

```
</details>

### Induced

<details>
```yaml
name: CoverageBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CoverageBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when a population represented in a dataset does not

  match the actual or real population that are being used'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Coverage Bias
exact_mappings:
- dpv_risk:CoverageBias
- dpv_risk_owl:CoverageBias
is_a: SelectionBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:CoverageBias

```
</details></div>