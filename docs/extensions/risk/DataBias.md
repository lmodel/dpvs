---
search:
  boost: 10.0
---

# Class: DataBias 


_Bias that occurs when data properties that if unaddressed lead to_

_systems that perform better or worse for different groups_



<div data-search-exclude markdown="1">



URI: [risk:DataBias](https://w3id.org/lmodel/dpv/risk/DataBias)





```mermaid
 classDiagram
    class DataBias
    click DataBias href "../DataBias/"
      PotentialConsequence <|-- DataBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataRisk <|-- DataBias
        click DataRisk href "../DataRisk/"
      Bias <|-- DataBias
        click Bias href "../Bias/"
      

      DataBias <|-- DataAggregationBias
        click DataAggregationBias href "../DataAggregationBias/"
      DataBias <|-- DataProcessingBias
        click DataProcessingBias href "../DataProcessingBias/"
      DataBias <|-- InformativenessBias
        click InformativenessBias href "../InformativenessBias/"
      DataBias <|-- SimpsonsParadoxBias
        click SimpsonsParadoxBias href "../SimpsonsParadoxBias/"
      DataBias <|-- StatisticalBias
        click StatisticalBias href "../StatisticalBias/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DataBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * [DataAggregationBias](DataAggregationBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DataProcessingBias](DataProcessingBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [InformativenessBias](InformativenessBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [SimpsonsParadoxBias](SimpsonsParadoxBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [StatisticalBias](StatisticalBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataBias](https://w3id.org/lmodel/dpv/risk/DataBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataBias |
| native | risk:DataBias |
| exact | dpv_risk:DataBias, dpv_risk_owl:DataBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when data properties that if unaddressed lead to

  systems that perform better or worse for different groups'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Bias
exact_mappings:
- dpv_risk:DataBias
- dpv_risk_owl:DataBias
is_a: Bias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- DataRisk
class_uri: risk:DataBias

```
</details>

### Induced

<details>
```yaml
name: DataBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when data properties that if unaddressed lead to

  systems that perform better or worse for different groups'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Bias
exact_mappings:
- dpv_risk:DataBias
- dpv_risk_owl:DataBias
is_a: Bias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
- DataRisk
class_uri: risk:DataBias

```
</details></div>