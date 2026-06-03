---
search:
  boost: 10.0
---

# Class: IdentityTheft 


_Concept representing Identity Theft_



<div data-search-exclude markdown="1">



URI: [risk:IdentityTheft](https://w3id.org/lmodel/dpv/risk/IdentityTheft)





```mermaid
 classDiagram
    class IdentityTheft
    click IdentityTheft href "../IdentityTheft/"
      ConfidentialityConcept <|-- IdentityTheft
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- IdentityTheft
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- IdentityTheft
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- IdentityTheft
        click PotentialRiskSource href "../PotentialRiskSource/"
      MaliciousActivity <|-- IdentityTheft
        click MaliciousActivity href "../MaliciousActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **IdentityTheft** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IdentityTheft](https://w3id.org/lmodel/dpv/risk/IdentityTheft) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Identity Theft




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IdentityTheft |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IdentityTheft |
| native | risk:IdentityTheft |
| exact | dpv_risk:IdentityTheft, dpv_risk_owl:IdentityTheft |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IdentityTheft
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IdentityTheft
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Identity Theft
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Identity Theft
exact_mappings:
- dpv_risk:IdentityTheft
- dpv_risk_owl:IdentityTheft
is_a: MaliciousActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:IdentityTheft

```
</details>

### Induced

<details>
```yaml
name: IdentityTheft
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IdentityTheft
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Identity Theft
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Identity Theft
exact_mappings:
- dpv_risk:IdentityTheft
- dpv_risk_owl:IdentityTheft
is_a: MaliciousActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:IdentityTheft

```
</details></div>