---
search:
  boost: 10.0
---

# Class: DistributedDenialServiceAttack 


_Concept representing Distributed Denial of Service Attack (DDoS)_



<div data-search-exclude markdown="1">



URI: [risk:DistributedDenialServiceAttack](https://w3id.org/lmodel/dpv/risk/DistributedDenialServiceAttack)





```mermaid
 classDiagram
    class DistributedDenialServiceAttack
    click DistributedDenialServiceAttack href "../DistributedDenialServiceAttack/"
      AvailabilityConcept <|-- DistributedDenialServiceAttack
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialRisk <|-- DistributedDenialServiceAttack
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DistributedDenialServiceAttack
        click PotentialRiskSource href "../PotentialRiskSource/"
      DenialServiceAttack <|-- DistributedDenialServiceAttack
        click DenialServiceAttack href "../DenialServiceAttack/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [SecurityAttack](SecurityAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [DenialServiceAttack](DenialServiceAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * **DistributedDenialServiceAttack** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DistributedDenialServiceAttack](https://w3id.org/lmodel/dpv/risk/DistributedDenialServiceAttack) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Distributed Denial of Service Attack (DDoS)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DistributedDenialServiceAttack |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DistributedDenialServiceAttack |
| native | risk:DistributedDenialServiceAttack |
| exact | dpv_risk:DistributedDenialServiceAttack, dpv_risk_owl:DistributedDenialServiceAttack |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DistributedDenialServiceAttack
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DistributedDenialServiceAttack
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Distributed Denial of Service Attack (DDoS)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Distributed Denial of Service Attack (DDoS)
exact_mappings:
- dpv_risk:DistributedDenialServiceAttack
- dpv_risk_owl:DistributedDenialServiceAttack
is_a: DenialServiceAttack
mixins:
- AvailabilityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DistributedDenialServiceAttack

```
</details>

### Induced

<details>
```yaml
name: DistributedDenialServiceAttack
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DistributedDenialServiceAttack
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Distributed Denial of Service Attack (DDoS)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Distributed Denial of Service Attack (DDoS)
exact_mappings:
- dpv_risk:DistributedDenialServiceAttack
- dpv_risk_owl:DistributedDenialServiceAttack
is_a: DenialServiceAttack
mixins:
- AvailabilityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DistributedDenialServiceAttack

```
</details></div>