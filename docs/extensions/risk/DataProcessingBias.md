---
search:
  boost: 10.0
---

# Class: DataProcessingBias 


_Bias that occurs due to pre-processing (or post-processing) of data,_

_even though the original data would not have led to any bias_



<div data-search-exclude markdown="1">



URI: [risk:DataProcessingBias](https://w3id.org/lmodel/dpv/risk/DataProcessingBias)





```mermaid
 classDiagram
    class DataProcessingBias
    click DataProcessingBias href "../DataProcessingBias/"
      PotentialConsequence <|-- DataProcessingBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DataProcessingBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DataProcessingBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataBias <|-- DataProcessingBias
        click DataBias href "../DataBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * **DataProcessingBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DataProcessingBias](https://w3id.org/lmodel/dpv/risk/DataProcessingBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Data Processing Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#DataProcessingBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DataProcessingBias |
| native | risk:DataProcessingBias |
| exact | dpv_risk:DataProcessingBias, dpv_risk_owl:DataProcessingBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataProcessingBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataProcessingBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs due to pre-processing (or post-processing) of data,

  even though the original data would not have led to any bias'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Processing Bias
exact_mappings:
- dpv_risk:DataProcessingBias
- dpv_risk_owl:DataProcessingBias
is_a: DataBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataProcessingBias

```
</details>

### Induced

<details>
```yaml
name: DataProcessingBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DataProcessingBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs due to pre-processing (or post-processing) of data,

  even though the original data would not have led to any bias'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Data Processing Bias
exact_mappings:
- dpv_risk:DataProcessingBias
- dpv_risk_owl:DataProcessingBias
is_a: DataBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DataProcessingBias

```
</details></div>