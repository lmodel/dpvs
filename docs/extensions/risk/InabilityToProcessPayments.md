---
search:
  boost: 10.0
---

# Class: InabilityToProcessPayments 


_Concept representing inability to process payments_



<div data-search-exclude markdown="1">



URI: [risk:InabilityToProcessPayments](https://w3id.org/lmodel/dpv/risk/InabilityToProcessPayments)





```mermaid
 classDiagram
    class InabilityToProcessPayments
    click InabilityToProcessPayments href "../InabilityToProcessPayments/"
      PotentialConsequence <|-- InabilityToProcessPayments
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- InabilityToProcessPayments
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- InabilityToProcessPayments
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- InabilityToProcessPayments
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **InabilityToProcessPayments** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InabilityToProcessPayments](https://w3id.org/lmodel/dpv/risk/InabilityToProcessPayments) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Inability to Process Payments




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#InabilityToProcessPayments |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InabilityToProcessPayments |
| native | risk:InabilityToProcessPayments |
| exact | dpv_risk:InabilityToProcessPayments, dpv_risk_owl:InabilityToProcessPayments |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InabilityToProcessPayments
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToProcessPayments
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to process payments
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Process Payments
exact_mappings:
- dpv_risk:InabilityToProcessPayments
- dpv_risk_owl:InabilityToProcessPayments
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToProcessPayments

```
</details>

### Induced

<details>
```yaml
name: InabilityToProcessPayments
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToProcessPayments
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to process payments
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Process Payments
exact_mappings:
- dpv_risk:InabilityToProcessPayments
- dpv_risk_owl:InabilityToProcessPayments
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToProcessPayments

```
</details></div>