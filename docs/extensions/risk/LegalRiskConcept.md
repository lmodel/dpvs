---
search:
  boost: 10.0
---

# Class: LegalRiskConcept 


_Risk concepts, including any potential risk sources, consequences, or_

_impacts, that are legal in nature or relate to a legal system or process_



<div data-search-exclude markdown="1">



URI: [risk:LegalRiskConcept](https://w3id.org/lmodel/dpv/risk/LegalRiskConcept)





```mermaid
 classDiagram
    class LegalRiskConcept
    click LegalRiskConcept href "../LegalRiskConcept/"
      PotentialConsequence <|-- LegalRiskConcept
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- LegalRiskConcept
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- LegalRiskConcept
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- LegalRiskConcept
        click PotentialRiskSource href "../PotentialRiskSource/"
      

      LegalRiskConcept <|-- LegalComplianceRisk
        click LegalComplianceRisk href "../LegalComplianceRisk/"
      LegalRiskConcept <|-- LegallyRelevantConsequence
        click LegallyRelevantConsequence href "../LegallyRelevantConsequence/"
      LegalRiskConcept <|-- PolicyRisk
        click PolicyRisk href "../PolicyRisk/"
      

      
```





## Inheritance
* **LegalRiskConcept** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegalComplianceRisk](LegalComplianceRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegallyRelevantConsequence](LegallyRelevantConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
    * [PolicyRisk](PolicyRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:LegalRiskConcept](https://w3id.org/lmodel/dpv/risk/LegalRiskConcept) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Legal Risk Concept


## Comments

* Legal in this context refers exclusively to the law applied within a
jurisdiction and does not include internal policies or rules within an
organisation



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#LegalRiskConcept |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:LegalRiskConcept |
| native | risk:LegalRiskConcept |
| exact | dpv_risk:LegalRiskConcept, dpv_risk_owl:LegalRiskConcept |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegalRiskConcept
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LegalRiskConcept
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risk concepts, including any potential risk sources, consequences, or

  impacts, that are legal in nature or relate to a legal system or process'
comments:
- 'Legal in this context refers exclusively to the law applied within a

  jurisdiction and does not include internal policies or rules within an

  organisation'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Legal Risk Concept
exact_mappings:
- dpv_risk:LegalRiskConcept
- dpv_risk_owl:LegalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PotentialRiskSource
class_uri: risk:LegalRiskConcept

```
</details>

### Induced

<details>
```yaml
name: LegalRiskConcept
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LegalRiskConcept
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Risk concepts, including any potential risk sources, consequences, or

  impacts, that are legal in nature or relate to a legal system or process'
comments:
- 'Legal in this context refers exclusively to the law applied within a

  jurisdiction and does not include internal policies or rules within an

  organisation'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Legal Risk Concept
exact_mappings:
- dpv_risk:LegalRiskConcept
- dpv_risk_owl:LegalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
- PotentialRiskSource
class_uri: risk:LegalRiskConcept

```
</details></div>