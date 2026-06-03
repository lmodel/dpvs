---
search:
  boost: 10.0
---

# Class: InabilityToProvideHealthCare 


_Concept representing inability to provide health care_



<div data-search-exclude markdown="1">



URI: [risk:InabilityToProvideHealthCare](https://w3id.org/lmodel/dpv/risk/InabilityToProvideHealthCare)





```mermaid
 classDiagram
    class InabilityToProvideHealthCare
    click InabilityToProvideHealthCare href "../InabilityToProvideHealthCare/"
      PotentialConsequence <|-- InabilityToProvideHealthCare
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- InabilityToProvideHealthCare
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- InabilityToProvideHealthCare
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- InabilityToProvideHealthCare
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **InabilityToProvideHealthCare** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InabilityToProvideHealthCare](https://w3id.org/lmodel/dpv/risk/InabilityToProvideHealthCare) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Inability to Provide Health Care




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#InabilityToProvideHealthCare |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InabilityToProvideHealthCare |
| native | risk:InabilityToProvideHealthCare |
| exact | dpv_risk:InabilityToProvideHealthCare, dpv_risk_owl:InabilityToProvideHealthCare |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InabilityToProvideHealthCare
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToProvideHealthCare
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to provide health care
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Provide Health Care
exact_mappings:
- dpv_risk:InabilityToProvideHealthCare
- dpv_risk_owl:InabilityToProvideHealthCare
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToProvideHealthCare

```
</details>

### Induced

<details>
```yaml
name: InabilityToProvideHealthCare
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToProvideHealthCare
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to provide health care
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Provide Health Care
exact_mappings:
- dpv_risk:InabilityToProvideHealthCare
- dpv_risk_owl:InabilityToProvideHealthCare
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToProvideHealthCare

```
</details></div>