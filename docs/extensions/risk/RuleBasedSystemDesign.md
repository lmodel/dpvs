---
search:
  boost: 10.0
---

# Class: RuleBasedSystemDesign 


_Bias that occurs due to developer experience and expert advice having a_

_significant influence on rule-based system design_



<div data-search-exclude markdown="1">



URI: [risk:RuleBasedSystemDesign](https://w3id.org/lmodel/dpv/risk/RuleBasedSystemDesign)





```mermaid
 classDiagram
    class RuleBasedSystemDesign
    click RuleBasedSystemDesign href "../RuleBasedSystemDesign/"
      PotentialConsequence <|-- RuleBasedSystemDesign
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- RuleBasedSystemDesign
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- RuleBasedSystemDesign
        click PotentialRiskSource href "../PotentialRiskSource/"
      CognitiveBias <|-- RuleBasedSystemDesign
        click CognitiveBias href "../CognitiveBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [CognitiveBias](CognitiveBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **RuleBasedSystemDesign** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RuleBasedSystemDesign](https://w3id.org/lmodel/dpv/risk/RuleBasedSystemDesign) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Rule-Based System Design


## Comments

* Rule based system design also potentially introduces various forms of
human cognitive bias



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#RuleBasedSystemDesign |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RuleBasedSystemDesign |
| native | risk:RuleBasedSystemDesign |
| exact | dpv_risk:RuleBasedSystemDesign, dpv_risk_owl:RuleBasedSystemDesign |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RuleBasedSystemDesign
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RuleBasedSystemDesign
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs due to developer experience and expert advice having
  a

  significant influence on rule-based system design'
comments:
- 'Rule based system design also potentially introduces various forms of

  human cognitive bias'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Rule-Based System Design
exact_mappings:
- dpv_risk:RuleBasedSystemDesign
- dpv_risk_owl:RuleBasedSystemDesign
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:RuleBasedSystemDesign

```
</details>

### Induced

<details>
```yaml
name: RuleBasedSystemDesign
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RuleBasedSystemDesign
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs due to developer experience and expert advice having
  a

  significant influence on rule-based system design'
comments:
- 'Rule based system design also potentially introduces various forms of

  human cognitive bias'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Rule-Based System Design
exact_mappings:
- dpv_risk:RuleBasedSystemDesign
- dpv_risk_owl:RuleBasedSystemDesign
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:RuleBasedSystemDesign

```
</details></div>