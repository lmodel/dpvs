---
search:
  boost: 10.0
---

# Class: DocumentationIssues 


_Concept representing issues with the development and use of_

_documentation_



<div data-search-exclude markdown="1">



URI: [risk:DocumentationIssues](https://w3id.org/lmodel/dpv/risk/DocumentationIssues)





```mermaid
 classDiagram
    class DocumentationIssues
    click DocumentationIssues href "../DocumentationIssues/"
      PotentialConsequence <|-- DocumentationIssues
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- DocumentationIssues
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DocumentationIssues
        click PotentialRiskSource href "../PotentialRiskSource/"
      OrganisationalManagementRisk <|-- DocumentationIssues
        click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      

      DocumentationIssues <|-- InstructionsInaccessible
        click InstructionsInaccessible href "../InstructionsInaccessible/"
      DocumentationIssues <|-- InstructionsIncorrect
        click InstructionsIncorrect href "../InstructionsIncorrect/"
      DocumentationIssues <|-- InstructionsInsufficient
        click InstructionsInsufficient href "../InstructionsInsufficient/"
      DocumentationIssues <|-- InstructionsUnsuitable
        click InstructionsUnsuitable href "../InstructionsUnsuitable/"
      

      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OrganisationalManagementRisk](OrganisationalManagementRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **DocumentationIssues** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [InstructionsInaccessible](InstructionsInaccessible.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [InstructionsIncorrect](InstructionsIncorrect.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [InstructionsInsufficient](InstructionsInsufficient.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [InstructionsUnsuitable](InstructionsUnsuitable.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DocumentationIssues](https://w3id.org/lmodel/dpv/risk/DocumentationIssues) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Documentation Issues




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DocumentationIssues |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DocumentationIssues |
| native | risk:DocumentationIssues |
| exact | dpv_risk:DocumentationIssues, dpv_risk_owl:DocumentationIssues |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DocumentationIssues
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DocumentationIssues
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing issues with the development and use of

  documentation'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Documentation Issues
exact_mappings:
- dpv_risk:DocumentationIssues
- dpv_risk_owl:DocumentationIssues
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DocumentationIssues

```
</details>

### Induced

<details>
```yaml
name: DocumentationIssues
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DocumentationIssues
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing issues with the development and use of

  documentation'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Documentation Issues
exact_mappings:
- dpv_risk:DocumentationIssues
- dpv_risk_owl:DocumentationIssues
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DocumentationIssues

```
</details></div>