---
search:
  boost: 10.0
---

# Class: InabilityToFulfilLegalObligations 


_Concept representing inability to fulfil legal obligations_



<div data-search-exclude markdown="1">



URI: [risk:InabilityToFulfilLegalObligations](https://w3id.org/lmodel/dpv/risk/InabilityToFulfilLegalObligations)





```mermaid
 classDiagram
    class InabilityToFulfilLegalObligations
    click InabilityToFulfilLegalObligations href "../InabilityToFulfilLegalObligations/"
      PotentialConsequence <|-- InabilityToFulfilLegalObligations
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- InabilityToFulfilLegalObligations
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- InabilityToFulfilLegalObligations
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- InabilityToFulfilLegalObligations
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **InabilityToFulfilLegalObligations** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InabilityToFulfilLegalObligations](https://w3id.org/lmodel/dpv/risk/InabilityToFulfilLegalObligations) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Inability to Fulfil Legal Obligations




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#InabilityToFulfilLegalObligations |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InabilityToFulfilLegalObligations |
| native | risk:InabilityToFulfilLegalObligations |
| exact | dpv_risk:InabilityToFulfilLegalObligations, dpv_risk_owl:InabilityToFulfilLegalObligations |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InabilityToFulfilLegalObligations
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToFulfilLegalObligations
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to fulfil legal obligations
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Fulfil Legal Obligations
exact_mappings:
- dpv_risk:InabilityToFulfilLegalObligations
- dpv_risk_owl:InabilityToFulfilLegalObligations
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToFulfilLegalObligations

```
</details>

### Induced

<details>
```yaml
name: InabilityToFulfilLegalObligations
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToFulfilLegalObligations
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to fulfil legal obligations
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Fulfil Legal Obligations
exact_mappings:
- dpv_risk:InabilityToFulfilLegalObligations
- dpv_risk_owl:InabilityToFulfilLegalObligations
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToFulfilLegalObligations

```
</details></div>