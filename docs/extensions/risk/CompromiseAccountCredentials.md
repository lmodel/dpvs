---
search:
  boost: 10.0
---

# Class: CompromiseAccountCredentials 


_Concept representing Account Credentials to be compromised_



<div data-search-exclude markdown="1">



URI: [risk:CompromiseAccountCredentials](https://w3id.org/lmodel/dpv/risk/CompromiseAccountCredentials)





```mermaid
 classDiagram
    class CompromiseAccountCredentials
    click CompromiseAccountCredentials href "../CompromiseAccountCredentials/"
      ConfidentialityConcept <|-- CompromiseAccountCredentials
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- CompromiseAccountCredentials
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- CompromiseAccountCredentials
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- CompromiseAccountCredentials
        click PotentialRiskSource href "../PotentialRiskSource/"
      ExternalSecurityThreat <|-- CompromiseAccountCredentials
        click ExternalSecurityThreat href "../ExternalSecurityThreat/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **CompromiseAccountCredentials** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:CompromiseAccountCredentials](https://w3id.org/lmodel/dpv/risk/CompromiseAccountCredentials) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Compromise Account Credentials




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#CompromiseAccountCredentials |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:CompromiseAccountCredentials |
| native | risk:CompromiseAccountCredentials |
| exact | dpv_risk:CompromiseAccountCredentials, dpv_risk_owl:CompromiseAccountCredentials |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CompromiseAccountCredentials
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CompromiseAccountCredentials
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Account Credentials to be compromised
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Compromise Account Credentials
exact_mappings:
- dpv_risk:CompromiseAccountCredentials
- dpv_risk_owl:CompromiseAccountCredentials
is_a: ExternalSecurityThreat
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:CompromiseAccountCredentials

```
</details>

### Induced

<details>
```yaml
name: CompromiseAccountCredentials
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CompromiseAccountCredentials
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Account Credentials to be compromised
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Compromise Account Credentials
exact_mappings:
- dpv_risk:CompromiseAccountCredentials
- dpv_risk_owl:CompromiseAccountCredentials
is_a: ExternalSecurityThreat
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:CompromiseAccountCredentials

```
</details></div>