---
search:
  boost: 10.0
---

# Class: StatisticalBias 


_Bias that occurs as the type of consistent numerical offset in an_

_estimate relative to the true underlying value, inherent to most_

_estimates_



<div data-search-exclude markdown="1">



URI: [risk:StatisticalBias](https://w3id.org/lmodel/dpv/risk/StatisticalBias)





```mermaid
 classDiagram
    class StatisticalBias
    click StatisticalBias href "../StatisticalBias/"
      PotentialConsequence <|-- StatisticalBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- StatisticalBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- StatisticalBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataBias <|-- StatisticalBias
        click DataBias href "../DataBias/"
      

      StatisticalBias <|-- ConfoundingVariablesBias
        click ConfoundingVariablesBias href "../ConfoundingVariablesBias/"
      StatisticalBias <|-- NonNormalityBias
        click NonNormalityBias href "../NonNormalityBias/"
      StatisticalBias <|-- SelectionBias
        click SelectionBias href "../SelectionBias/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * **StatisticalBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [ConfoundingVariablesBias](ConfoundingVariablesBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [NonNormalityBias](NonNormalityBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [SelectionBias](SelectionBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:StatisticalBias](https://w3id.org/lmodel/dpv/risk/StatisticalBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Statistical Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO 20501:2019 |
| upstream_iri | https://w3id.org/dpv/risk/owl#StatisticalBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:StatisticalBias |
| native | risk:StatisticalBias |
| exact | dpv_risk:StatisticalBias, dpv_risk_owl:StatisticalBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StatisticalBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO 20501:2019
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#StatisticalBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs as the type of consistent numerical offset in an

  estimate relative to the true underlying value, inherent to most

  estimates'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Statistical Bias
exact_mappings:
- dpv_risk:StatisticalBias
- dpv_risk_owl:StatisticalBias
is_a: DataBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:StatisticalBias

```
</details>

### Induced

<details>
```yaml
name: StatisticalBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO 20501:2019
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#StatisticalBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs as the type of consistent numerical offset in an

  estimate relative to the true underlying value, inherent to most

  estimates'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Statistical Bias
exact_mappings:
- dpv_risk:StatisticalBias
- dpv_risk_owl:StatisticalBias
is_a: DataBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:StatisticalBias

```
</details></div>