---
search:
  boost: 10.0
---

# Class: ConfoundingVariablesBias 


_Bias that occurs as a confounding variable that influences both the_

_dependent variable and independent variable causing a spurious_

_association_



<div data-search-exclude markdown="1">



URI: [risk:ConfoundingVariablesBias](https://w3id.org/lmodel/dpv/risk/ConfoundingVariablesBias)





```mermaid
 classDiagram
    class ConfoundingVariablesBias
    click ConfoundingVariablesBias href "../ConfoundingVariablesBias/"
      PotentialConsequence <|-- ConfoundingVariablesBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ConfoundingVariablesBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ConfoundingVariablesBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      StatisticalBias <|-- ConfoundingVariablesBias
        click StatisticalBias href "../StatisticalBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DataBias](DataBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md) [DataRisk](DataRisk.md)]
            * [StatisticalBias](StatisticalBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **ConfoundingVariablesBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ConfoundingVariablesBias](https://w3id.org/lmodel/dpv/risk/ConfoundingVariablesBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Confounding Variables Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#ConfoundingVariablesBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ConfoundingVariablesBias |
| native | risk:ConfoundingVariablesBias |
| exact | dpv_risk:ConfoundingVariablesBias, dpv_risk_owl:ConfoundingVariablesBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConfoundingVariablesBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ConfoundingVariablesBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs as a confounding variable that influences both the

  dependent variable and independent variable causing a spurious

  association'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Confounding Variables Bias
exact_mappings:
- dpv_risk:ConfoundingVariablesBias
- dpv_risk_owl:ConfoundingVariablesBias
is_a: StatisticalBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ConfoundingVariablesBias

```
</details>

### Induced

<details>
```yaml
name: ConfoundingVariablesBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ConfoundingVariablesBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs as a confounding variable that influences both the

  dependent variable and independent variable causing a spurious

  association'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Confounding Variables Bias
exact_mappings:
- dpv_risk:ConfoundingVariablesBias
- dpv_risk_owl:ConfoundingVariablesBias
is_a: StatisticalBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ConfoundingVariablesBias

```
</details></div>