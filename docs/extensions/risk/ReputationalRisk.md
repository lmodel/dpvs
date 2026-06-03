---
search:
  boost: 10.0
---

# Class: ReputationalRisk 


_Risks and issues that affect the reputation of the organisation_



<div data-search-exclude markdown="1">



URI: [risk:ReputationalRisk](https://w3id.org/lmodel/dpv/risk/ReputationalRisk)





```mermaid
 classDiagram
    class ReputationalRisk
    click ReputationalRisk href "../ReputationalRisk/"
      PotentialConsequence <|-- ReputationalRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ReputationalRisk
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ReputationalRisk
        click PotentialRisk href "../PotentialRisk/"
      OrganisationalRiskConcept <|-- ReputationalRisk
        click OrganisationalRiskConcept href "../OrganisationalRiskConcept/"
      

      ReputationalRisk <|-- CredibilityLoss
        click CredibilityLoss href "../CredibilityLoss/"
      ReputationalRisk <|-- CustomerConfidenceLoss
        click CustomerConfidenceLoss href "../CustomerConfidenceLoss/"
      ReputationalRisk <|-- GoodwillLoss
        click GoodwillLoss href "../GoodwillLoss/"
      ReputationalRisk <|-- NegotiatingCapacityLoss
        click NegotiatingCapacityLoss href "../NegotiatingCapacityLoss/"
      ReputationalRisk <|-- OpportunityLoss
        click OpportunityLoss href "../OpportunityLoss/"
      ReputationalRisk <|-- ReputationalLoss
        click ReputationalLoss href "../ReputationalLoss/"
      ReputationalRisk <|-- TrustLoss
        click TrustLoss href "../TrustLoss/"
      

      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * **ReputationalRisk** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [CredibilityLoss](CredibilityLoss.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [CustomerConfidenceLoss](CustomerConfidenceLoss.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [GoodwillLoss](GoodwillLoss.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [NegotiatingCapacityLoss](NegotiatingCapacityLoss.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [OpportunityLoss](OpportunityLoss.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [ReputationalLoss](ReputationalLoss.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [TrustLoss](TrustLoss.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ReputationalRisk](https://w3id.org/lmodel/dpv/risk/ReputationalRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Reputational Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ReputationalRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ReputationalRisk |
| native | risk:ReputationalRisk |
| exact | dpv_risk:ReputationalRisk, dpv_risk_owl:ReputationalRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReputationalRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReputationalRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risks and issues that affect the reputation of the organisation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reputational Risk
exact_mappings:
- dpv_risk:ReputationalRisk
- dpv_risk_owl:ReputationalRisk
is_a: OrganisationalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ReputationalRisk

```
</details>

### Induced

<details>
```yaml
name: ReputationalRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ReputationalRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risks and issues that affect the reputation of the organisation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Reputational Risk
exact_mappings:
- dpv_risk:ReputationalRisk
- dpv_risk_owl:ReputationalRisk
is_a: OrganisationalRiskConcept
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ReputationalRisk

```
</details></div>