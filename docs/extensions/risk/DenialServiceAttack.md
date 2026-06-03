---
search:
  boost: 10.0
---

# Class: DenialServiceAttack 


_Concept representing Denial of Service Attack (DoS)_



<div data-search-exclude markdown="1">



URI: [risk:DenialServiceAttack](https://w3id.org/lmodel/dpv/risk/DenialServiceAttack)





```mermaid
 classDiagram
    class DenialServiceAttack
    click DenialServiceAttack href "../DenialServiceAttack/"
      AvailabilityConcept <|-- DenialServiceAttack
        click AvailabilityConcept href "../AvailabilityConcept/"
      PotentialRisk <|-- DenialServiceAttack
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- DenialServiceAttack
        click PotentialRiskSource href "../PotentialRiskSource/"
      SecurityAttack <|-- DenialServiceAttack
        click SecurityAttack href "../SecurityAttack/"
      

      DenialServiceAttack <|-- DistributedDenialServiceAttack
        click DistributedDenialServiceAttack href "../DistributedDenialServiceAttack/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [SecurityAttack](SecurityAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **DenialServiceAttack** [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
                * [DistributedDenialServiceAttack](DistributedDenialServiceAttack.md) [ [AvailabilityConcept](AvailabilityConcept.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DenialServiceAttack](https://w3id.org/lmodel/dpv/risk/DenialServiceAttack) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Denial of Service Attack (DoS)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DenialServiceAttack |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DenialServiceAttack |
| native | risk:DenialServiceAttack |
| exact | dpv_risk:DenialServiceAttack, dpv_risk_owl:DenialServiceAttack |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DenialServiceAttack
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DenialServiceAttack
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Denial of Service Attack (DoS)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Denial of Service Attack (DoS)
exact_mappings:
- dpv_risk:DenialServiceAttack
- dpv_risk_owl:DenialServiceAttack
is_a: SecurityAttack
mixins:
- AvailabilityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DenialServiceAttack

```
</details>

### Induced

<details>
```yaml
name: DenialServiceAttack
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DenialServiceAttack
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Denial of Service Attack (DoS)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Denial of Service Attack (DoS)
exact_mappings:
- dpv_risk:DenialServiceAttack
- dpv_risk_owl:DenialServiceAttack
is_a: SecurityAttack
mixins:
- AvailabilityConcept
- PotentialRisk
- PotentialRiskSource
class_uri: risk:DenialServiceAttack

```
</details></div>