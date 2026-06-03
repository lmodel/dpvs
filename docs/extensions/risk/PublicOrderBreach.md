---
search:
  boost: 10.0
---

# Class: PublicOrderBreach 


_Concept representing Public Order Breach_



<div data-search-exclude markdown="1">



URI: [risk:PublicOrderBreach](https://w3id.org/lmodel/dpv/risk/PublicOrderBreach)





```mermaid
 classDiagram
    class PublicOrderBreach
    click PublicOrderBreach href "../PublicOrderBreach/"
      PotentialConsequence <|-- PublicOrderBreach
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- PublicOrderBreach
        click PotentialRisk href "../PotentialRisk/"
      LegalComplianceRisk <|-- PublicOrderBreach
        click LegalComplianceRisk href "../LegalComplianceRisk/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegalComplianceRisk](LegalComplianceRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **PublicOrderBreach** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PublicOrderBreach](https://w3id.org/lmodel/dpv/risk/PublicOrderBreach) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Public Order Breach




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PublicOrderBreach |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PublicOrderBreach |
| native | risk:PublicOrderBreach |
| exact | dpv_risk:PublicOrderBreach, dpv_risk_owl:PublicOrderBreach |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PublicOrderBreach
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PublicOrderBreach
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Public Order Breach
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Public Order Breach
exact_mappings:
- dpv_risk:PublicOrderBreach
- dpv_risk_owl:PublicOrderBreach
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:PublicOrderBreach

```
</details>

### Induced

<details>
```yaml
name: PublicOrderBreach
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PublicOrderBreach
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Public Order Breach
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Public Order Breach
exact_mappings:
- dpv_risk:PublicOrderBreach
- dpv_risk_owl:PublicOrderBreach
is_a: LegalComplianceRisk
mixins:
- PotentialConsequence
- PotentialRisk
class_uri: risk:PublicOrderBreach

```
</details></div>