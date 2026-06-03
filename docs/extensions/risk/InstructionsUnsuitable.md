---
search:
  boost: 10.0
---

# Class: InstructionsUnsuitable 


_Concept representing cases wher instructions are unsuitable for the_

_specific task or for the specific audience, including due to_

_incomprehensibility, lack of knowledge, or not being fit for purpose_



<div data-search-exclude markdown="1">



URI: [risk:InstructionsUnsuitable](https://w3id.org/lmodel/dpv/risk/InstructionsUnsuitable)





```mermaid
 classDiagram
    class InstructionsUnsuitable
    click InstructionsUnsuitable href "../InstructionsUnsuitable/"
      PotentialConsequence <|-- InstructionsUnsuitable
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- InstructionsUnsuitable
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- InstructionsUnsuitable
        click PotentialRiskSource href "../PotentialRiskSource/"
      DocumentationIssues <|-- InstructionsUnsuitable
        click DocumentationIssues href "../DocumentationIssues/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OrganisationalManagementRisk](OrganisationalManagementRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DocumentationIssues](DocumentationIssues.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **InstructionsUnsuitable** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InstructionsUnsuitable](https://w3id.org/lmodel/dpv/risk/InstructionsUnsuitable) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Instructions Unsuitable




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#InstructionsUnsuitable |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InstructionsUnsuitable |
| native | risk:InstructionsUnsuitable |
| exact | dpv_risk:InstructionsUnsuitable, dpv_risk_owl:InstructionsUnsuitable |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InstructionsUnsuitable
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InstructionsUnsuitable
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing cases wher instructions are unsuitable for the

  specific task or for the specific audience, including due to

  incomprehensibility, lack of knowledge, or not being fit for purpose'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Instructions Unsuitable
exact_mappings:
- dpv_risk:InstructionsUnsuitable
- dpv_risk_owl:InstructionsUnsuitable
is_a: DocumentationIssues
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:InstructionsUnsuitable

```
</details>

### Induced

<details>
```yaml
name: InstructionsUnsuitable
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InstructionsUnsuitable
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing cases wher instructions are unsuitable for the

  specific task or for the specific audience, including due to

  incomprehensibility, lack of knowledge, or not being fit for purpose'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Instructions Unsuitable
exact_mappings:
- dpv_risk:InstructionsUnsuitable
- dpv_risk_owl:InstructionsUnsuitable
is_a: DocumentationIssues
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:InstructionsUnsuitable

```
</details></div>