---
search:
  boost: 10.0
---

# Class: InabilityToEstablishLegalClaims 


_Concept representing inability to establish legal claims_



<div data-search-exclude markdown="1">



URI: [risk:InabilityToEstablishLegalClaims](https://w3id.org/lmodel/dpv/risk/InabilityToEstablishLegalClaims)





```mermaid
 classDiagram
    class InabilityToEstablishLegalClaims
    click InabilityToEstablishLegalClaims href "../InabilityToEstablishLegalClaims/"
      PotentialConsequence <|-- InabilityToEstablishLegalClaims
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- InabilityToEstablishLegalClaims
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- InabilityToEstablishLegalClaims
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- InabilityToEstablishLegalClaims
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **InabilityToEstablishLegalClaims** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InabilityToEstablishLegalClaims](https://w3id.org/lmodel/dpv/risk/InabilityToEstablishLegalClaims) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Inability to Establish Legal Claims




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#InabilityToEstablishLegalClaims |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InabilityToEstablishLegalClaims |
| native | risk:InabilityToEstablishLegalClaims |
| exact | dpv_risk:InabilityToEstablishLegalClaims, dpv_risk_owl:InabilityToEstablishLegalClaims |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InabilityToEstablishLegalClaims
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToEstablishLegalClaims
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to establish legal claims
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Establish Legal Claims
exact_mappings:
- dpv_risk:InabilityToEstablishLegalClaims
- dpv_risk_owl:InabilityToEstablishLegalClaims
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToEstablishLegalClaims

```
</details>

### Induced

<details>
```yaml
name: InabilityToEstablishLegalClaims
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToEstablishLegalClaims
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to establish legal claims
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Establish Legal Claims
exact_mappings:
- dpv_risk:InabilityToEstablishLegalClaims
- dpv_risk_owl:InabilityToEstablishLegalClaims
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToEstablishLegalClaims

```
</details></div>