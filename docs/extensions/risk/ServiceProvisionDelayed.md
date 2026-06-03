---
search:
  boost: 10.0
---

# Class: ServiceProvisionDelayed 


_Concept representing service provision delayed_



<div data-search-exclude markdown="1">



URI: [risk:ServiceProvisionDelayed](https://w3id.org/lmodel/dpv/risk/ServiceProvisionDelayed)





```mermaid
 classDiagram
    class ServiceProvisionDelayed
    click ServiceProvisionDelayed href "../ServiceProvisionDelayed/"
      PotentialConsequence <|-- ServiceProvisionDelayed
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ServiceProvisionDelayed
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ServiceProvisionDelayed
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- ServiceProvisionDelayed
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ServiceProvisionDelayed** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ServiceProvisionDelayed](https://w3id.org/lmodel/dpv/risk/ServiceProvisionDelayed) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Service Provision Delayed




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ServiceProvisionDelayed |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ServiceProvisionDelayed |
| native | risk:ServiceProvisionDelayed |
| exact | dpv_risk:ServiceProvisionDelayed, dpv_risk_owl:ServiceProvisionDelayed |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ServiceProvisionDelayed
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceProvisionDelayed
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service provision delayed
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Provision Delayed
exact_mappings:
- dpv_risk:ServiceProvisionDelayed
- dpv_risk_owl:ServiceProvisionDelayed
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceProvisionDelayed

```
</details>

### Induced

<details>
```yaml
name: ServiceProvisionDelayed
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ServiceProvisionDelayed
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing service provision delayed
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Service Provision Delayed
exact_mappings:
- dpv_risk:ServiceProvisionDelayed
- dpv_risk_owl:ServiceProvisionDelayed
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ServiceProvisionDelayed

```
</details></div>