---
search:
  boost: 10.0
---

# Class: DataAggregationBias 


_Bias that occurs when aggregating data covering different groups of_

_objects has different statistical distributions that introduce bias into_

_the data_



<div data-search-exclude markdown="1">



URI: [risk:DataAggregationBias](https://w3id.org/lmodel/dpv/risk/DataAggregationBias)





```mermaid
 classDiagram
    class DataAggregationBias
    click DataAggregationBias href "../DataAggregationBias/"
      PotentialConsequence <|-- DataAggregationBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataAggregationBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataAggregationBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataBias <|-- DataAggregationBias
        click DataBias href "../DataBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * **DataAggregationBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataAggregationBias](https://w3id.org/lmodel/dpv/risk/DataAggregationBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Aggregation Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataAggregationBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataAggregationBias |
| native | risk:DataAggregationBias |
| exact | dpv_risk:DataAggregationBias, dpv_risk_owl:DataAggregationBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataAggregationBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataAggregationBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when aggregating data covering different groups of

  objects has different statistical distributions that introduce bias into

  the data'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Aggregation Bias
exact_mappings:
- dpv_risk:DataAggregationBias
- dpv_risk_owl:DataAggregationBias
is_a: DataBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataAggregationBias

```
</details>

### Induced

<details>
```yaml
name: DataAggregationBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataAggregationBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when aggregating data covering different groups of

  objects has different statistical distributions that introduce bias into

  the data'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Aggregation Bias
exact_mappings:
- dpv_risk:DataAggregationBias
- dpv_risk_owl:DataAggregationBias
is_a: DataBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataAggregationBias

```
</details></div>