---
search:
  boost: 10.0
---

# Class: SimpsonsParadoxBias 


_Bias that occurs when a trend that is indicated in individual groups of_

_data reverses when the groups of data are combined_



<div data-search-exclude markdown="1">



URI: [risk:SimpsonsParadoxBias](https://w3id.org/lmodel/dpv/risk/SimpsonsParadoxBias)





```mermaid
 classDiagram
    class SimpsonsParadoxBias
    click SimpsonsParadoxBias href "../SimpsonsParadoxBias/"
      PotentialConsequence <|-- SimpsonsParadoxBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SimpsonsParadoxBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SimpsonsParadoxBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataBias <|-- SimpsonsParadoxBias
        click DataBias href "../DataBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * **SimpsonsParadoxBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SimpsonsParadoxBias](https://w3id.org/lmodel/dpv/risk/SimpsonsParadoxBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Simpson'S Paradox Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#SimpsonsParadoxBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SimpsonsParadoxBias |
| native | risk:SimpsonsParadoxBias |
| exact | dpv_risk:SimpsonsParadoxBias, dpv_risk_owl:SimpsonsParadoxBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SimpsonsParadoxBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SimpsonsParadoxBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when a trend that is indicated in individual groups
  of

  data reverses when the groups of data are combined'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Simpson'S Paradox Bias
exact_mappings:
- dpv_risk:SimpsonsParadoxBias
- dpv_risk_owl:SimpsonsParadoxBias
is_a: DataBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SimpsonsParadoxBias

```
</details>

### Induced

<details>
```yaml
name: SimpsonsParadoxBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SimpsonsParadoxBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when a trend that is indicated in individual groups
  of

  data reverses when the groups of data are combined'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Simpson'S Paradox Bias
exact_mappings:
- dpv_risk:SimpsonsParadoxBias
- dpv_risk_owl:SimpsonsParadoxBias
is_a: DataBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SimpsonsParadoxBias

```
</details></div>