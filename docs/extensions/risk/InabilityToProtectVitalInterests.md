---
search:
  boost: 10.0
---

# Class: InabilityToProtectVitalInterests 


_Concept representing inability to protect vital interests_



<div data-search-exclude markdown="1">



URI: [risk:InabilityToProtectVitalInterests](https://w3id.org/lmodel/dpv/risk/InabilityToProtectVitalInterests)





```mermaid
 classDiagram
    class InabilityToProtectVitalInterests
    click InabilityToProtectVitalInterests href "../InabilityToProtectVitalInterests/"
      PotentialConsequence <|-- InabilityToProtectVitalInterests
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- InabilityToProtectVitalInterests
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- InabilityToProtectVitalInterests
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- InabilityToProtectVitalInterests
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **InabilityToProtectVitalInterests** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InabilityToProtectVitalInterests](https://w3id.org/lmodel/dpv/risk/InabilityToProtectVitalInterests) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Inability to Protect Vital Interests




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#InabilityToProtectVitalInterests |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InabilityToProtectVitalInterests |
| native | risk:InabilityToProtectVitalInterests |
| exact | dpv_risk:InabilityToProtectVitalInterests, dpv_risk_owl:InabilityToProtectVitalInterests |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InabilityToProtectVitalInterests
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToProtectVitalInterests
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to protect vital interests
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Protect Vital Interests
exact_mappings:
- dpv_risk:InabilityToProtectVitalInterests
- dpv_risk_owl:InabilityToProtectVitalInterests
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToProtectVitalInterests

```
</details>

### Induced

<details>
```yaml
name: InabilityToProtectVitalInterests
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToProtectVitalInterests
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to protect vital interests
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Protect Vital Interests
exact_mappings:
- dpv_risk:InabilityToProtectVitalInterests
- dpv_risk_owl:InabilityToProtectVitalInterests
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToProtectVitalInterests

```
</details></div>