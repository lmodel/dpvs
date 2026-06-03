---
search:
  boost: 10.0
---

# Class: CompromiseAccount 


_Concept representing a compromised account that is then used by the_

_compromiser_



<div data-search-exclude markdown="1">



URI: [risk:CompromiseAccount](https://w3id.org/lmodel/dpv/risk/CompromiseAccount)





```mermaid
 classDiagram
    class CompromiseAccount
    click CompromiseAccount href "../CompromiseAccount/"
      AvailabilityConcept <|-- CompromiseAccount
        click AvailabilityConcept href "../AvailabilityConcept/"
      ConfidentialityConcept <|-- CompromiseAccount
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- CompromiseAccount
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- CompromiseAccount
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- CompromiseAccount
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- CompromiseAccount
        click PotentialRiskSource href "../PotentialRiskSource/"
      ExternalSecurityThreat <|-- CompromiseAccount
        click ExternalSecurityThreat href "../ExternalSecurityThreat/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **CompromiseAccount** [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:CompromiseAccount](https://w3id.org/lmodel/dpv/risk/CompromiseAccount) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Compromise Account




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#CompromiseAccount |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:CompromiseAccount |
| native | risk:CompromiseAccount |
| exact | dpv_risk:CompromiseAccount, dpv_risk_owl:CompromiseAccount |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CompromiseAccount
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CompromiseAccount
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing a compromised account that is then used by the

  compromiser'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Compromise Account
exact_mappings:
- dpv_risk:CompromiseAccount
- dpv_risk_owl:CompromiseAccount
is_a: ExternalSecurityThreat
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:CompromiseAccount

```
</details>

### Induced

<details>
```yaml
name: CompromiseAccount
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CompromiseAccount
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing a compromised account that is then used by the

  compromiser'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Compromise Account
exact_mappings:
- dpv_risk:CompromiseAccount
- dpv_risk_owl:CompromiseAccount
is_a: ExternalSecurityThreat
mixins:
- AvailabilityConcept
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:CompromiseAccount

```
</details></div>