---
search:
  boost: 10.0
---

# Class: Bias 


_Bias is defined as the systematic difference in treatment of certain_

_objects, people, or groups in comparison to others_



<div data-search-exclude markdown="1">



URI: [risk:Bias](https://w3id.org/lmodel/dpv/risk/Bias)





```mermaid
 classDiagram
    class Bias
    click Bias href "../Bias/"
      PotentialConsequence <|-- Bias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- Bias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Bias
        click PotentialRiskSource href "../PotentialRiskSource/"
      TechnicalRiskConcept <|-- Bias
        click TechnicalRiskConcept href "../TechnicalRiskConcept/"
      

      Bias <|-- CognitiveBias
        click CognitiveBias href "../CognitiveBias/"
      Bias <|-- DataBias
        click DataBias href "../DataBias/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **Bias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [CognitiveBias](CognitiveBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Bias](https://w3id.org/lmodel/dpv/risk/Bias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#Bias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Bias |
| native | risk:Bias |
| exact | dpv_risk:Bias, dpv_risk_owl:Bias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Bias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Bias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias is defined as the systematic difference in treatment of certain

  objects, people, or groups in comparison to others'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Bias
exact_mappings:
- dpv_risk:Bias
- dpv_risk_owl:Bias
is_a: TechnicalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Bias

```
</details>

### Induced

<details>
```yaml
name: Bias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Bias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias is defined as the systematic difference in treatment of certain

  objects, people, or groups in comparison to others'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Bias
exact_mappings:
- dpv_risk:Bias
- dpv_risk_owl:Bias
is_a: TechnicalRiskConcept
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Bias

```
</details></div>