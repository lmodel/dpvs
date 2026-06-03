---
search:
  boost: 10.0
---

# Class: LoyaltyProgramExclusion 


_Concept representing exclusion from loyalty program_



<div data-search-exclude markdown="1">



URI: [risk:LoyaltyProgramExclusion](https://w3id.org/lmodel/dpv/risk/LoyaltyProgramExclusion)





```mermaid
 classDiagram
    class LoyaltyProgramExclusion
    click LoyaltyProgramExclusion href "../LoyaltyProgramExclusion/"
      PotentialConsequence <|-- LoyaltyProgramExclusion
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- LoyaltyProgramExclusion
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- LoyaltyProgramExclusion
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- LoyaltyProgramExclusion
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **LoyaltyProgramExclusion** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:LoyaltyProgramExclusion](https://w3id.org/lmodel/dpv/risk/LoyaltyProgramExclusion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Loyalty Program Exclusion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#LoyaltyProgramExclusion |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:LoyaltyProgramExclusion |
| native | risk:LoyaltyProgramExclusion |
| exact | dpv_risk:LoyaltyProgramExclusion, dpv_risk_owl:LoyaltyProgramExclusion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LoyaltyProgramExclusion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LoyaltyProgramExclusion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing exclusion from loyalty program
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Loyalty Program Exclusion
exact_mappings:
- dpv_risk:LoyaltyProgramExclusion
- dpv_risk_owl:LoyaltyProgramExclusion
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:LoyaltyProgramExclusion

```
</details>

### Induced

<details>
```yaml
name: LoyaltyProgramExclusion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LoyaltyProgramExclusion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing exclusion from loyalty program
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Loyalty Program Exclusion
exact_mappings:
- dpv_risk:LoyaltyProgramExclusion
- dpv_risk_owl:LoyaltyProgramExclusion
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:LoyaltyProgramExclusion

```
</details></div>