---
search:
  boost: 10.0
---

# Class: TechnicalRiskConcept 


_Risk concepts, including any potential risk sources, consequences, or_

_impacts, that are technical in nature or relate to a technical or_

_technological process_



<div data-search-exclude markdown="1">



URI: [risk:TechnicalRiskConcept](https://w3id.org/lmodel/dpv/risk/TechnicalRiskConcept)





```mermaid
 classDiagram
    class TechnicalRiskConcept
    click TechnicalRiskConcept href "../TechnicalRiskConcept/"
      PotentialConsequence <|-- TechnicalRiskConcept
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- TechnicalRiskConcept
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- TechnicalRiskConcept
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- TechnicalRiskConcept
        click PotentialRiskSource href "../PotentialRiskSource/"
      

      TechnicalRiskConcept <|-- Bias
        click Bias href "../Bias/"
      TechnicalRiskConcept <|-- DataRisk
        click DataRisk href "../DataRisk/"
      TechnicalRiskConcept <|-- ExternalSecurityThreat
        click ExternalSecurityThreat href "../ExternalSecurityThreat/"
      TechnicalRiskConcept <|-- OperationalSecurityRisk
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      

      
```





## Inheritance
* **TechnicalRiskConcept** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [DataRisk](DataRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:TechnicalRiskConcept](https://w3id.org/lmodel/dpv/risk/TechnicalRiskConcept) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Technical Risk Concept




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#TechnicalRiskConcept |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:TechnicalRiskConcept |
| native | risk:TechnicalRiskConcept |
| exact | dpv_risk:TechnicalRiskConcept, dpv_risk_owl:TechnicalRiskConcept |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TechnicalRiskConcept
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TechnicalRiskConcept
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risk concepts, including any potential risk sources, consequences, or

  impacts, that are technical in nature or relate to a technical or

  technological process'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Technical Risk Concept
exact_mappings:
- dpv_risk:TechnicalRiskConcept
- dpv_risk_owl:TechnicalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TechnicalRiskConcept

```
</details>

### Induced

<details>
```yaml
name: TechnicalRiskConcept
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TechnicalRiskConcept
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risk concepts, including any potential risk sources, consequences, or

  impacts, that are technical in nature or relate to a technical or

  technological process'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Technical Risk Concept
exact_mappings:
- dpv_risk:TechnicalRiskConcept
- dpv_risk_owl:TechnicalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TechnicalRiskConcept

```
</details></div>