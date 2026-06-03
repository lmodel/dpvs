---
search:
  boost: 10.0
---

# Class: InformativenessBias 


_Bias that occurs when the mapping between inputs present in the data and_

_outputs are more difficult to identify for some group_



<div data-search-exclude markdown="1">



URI: [risk:InformativenessBias](https://w3id.org/lmodel/dpv/risk/InformativenessBias)





```mermaid
 classDiagram
    class InformativenessBias
    click InformativenessBias href "../InformativenessBias/"
      PotentialConsequence <|-- InformativenessBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- InformativenessBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- InformativenessBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      DataBias <|-- InformativenessBias
        click DataBias href "../DataBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * **InformativenessBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InformativenessBias](https://w3id.org/lmodel/dpv/risk/InformativenessBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Informativeness Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#InformativenessBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InformativenessBias |
| native | risk:InformativenessBias |
| exact | dpv_risk:InformativenessBias, dpv_risk_owl:InformativenessBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InformativenessBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InformativenessBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when the mapping between inputs present in the data
  and

  outputs are more difficult to identify for some group'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Informativeness Bias
exact_mappings:
- dpv_risk:InformativenessBias
- dpv_risk_owl:InformativenessBias
is_a: DataBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:InformativenessBias

```
</details>

### Induced

<details>
```yaml
name: InformativenessBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InformativenessBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when the mapping between inputs present in the data
  and

  outputs are more difficult to identify for some group'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Informativeness Bias
exact_mappings:
- dpv_risk:InformativenessBias
- dpv_risk_owl:InformativenessBias
is_a: DataBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:InformativenessBias

```
</details></div>