---
search:
  boost: 10.0
---

# Class: InstructionsInaccessible 


_Concept representing cases wher instructions are inaccessible_



<div data-search-exclude markdown="1">



URI: [risk:InstructionsInaccessible](https://w3id.org/lmodel/dpv/risk/InstructionsInaccessible)





```mermaid
 classDiagram
    class InstructionsInaccessible
    click InstructionsInaccessible href "../InstructionsInaccessible/"
      PotentialConsequence <|-- InstructionsInaccessible
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- InstructionsInaccessible
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- InstructionsInaccessible
        click PotentialRiskSource href "../PotentialRiskSource/"
      DocumentationIssues <|-- InstructionsInaccessible
        click DocumentationIssues href "../DocumentationIssues/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OrganisationalManagementRisk](OrganisationalManagementRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [DocumentationIssues](DocumentationIssues.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **InstructionsInaccessible** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InstructionsInaccessible](https://w3id.org/lmodel/dpv/risk/InstructionsInaccessible) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Instructions Inaccessible




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#InstructionsInaccessible |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InstructionsInaccessible |
| native | risk:InstructionsInaccessible |
| exact | dpv_risk:InstructionsInaccessible, dpv_risk_owl:InstructionsInaccessible |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InstructionsInaccessible
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InstructionsInaccessible
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing cases wher instructions are inaccessible
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Instructions Inaccessible
exact_mappings:
- dpv_risk:InstructionsInaccessible
- dpv_risk_owl:InstructionsInaccessible
is_a: DocumentationIssues
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:InstructionsInaccessible

```
</details>

### Induced

<details>
```yaml
name: InstructionsInaccessible
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InstructionsInaccessible
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing cases wher instructions are inaccessible
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Instructions Inaccessible
exact_mappings:
- dpv_risk:InstructionsInaccessible
- dpv_risk_owl:InstructionsInaccessible
is_a: DocumentationIssues
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:InstructionsInaccessible

```
</details></div>