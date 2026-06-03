---
search:
  boost: 10.0
---

# Class: HumanOversightInsufficient 


_Concept representing cases where human oversight is insufficient for the_

_intended effect, such as not being capable of identifying a problem_



<div data-search-exclude markdown="1">



URI: [risk:HumanOversightInsufficient](https://w3id.org/lmodel/dpv/risk/HumanOversightInsufficient)





```mermaid
 classDiagram
    class HumanOversightInsufficient
    click HumanOversightInsufficient href "../HumanOversightInsufficient/"
      PotentialConsequence <|-- HumanOversightInsufficient
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- HumanOversightInsufficient
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- HumanOversightInsufficient
        click PotentialRiskSource href "../PotentialRiskSource/"
      OrganisationalManagementRisk <|-- HumanOversightInsufficient
        click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OrganisationalManagementRisk](OrganisationalManagementRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **HumanOversightInsufficient** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:HumanOversightInsufficient](https://w3id.org/lmodel/dpv/risk/HumanOversightInsufficient) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Human Oversight Insufficient




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#HumanOversightInsufficient |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:HumanOversightInsufficient |
| native | risk:HumanOversightInsufficient |
| exact | dpv_risk:HumanOversightInsufficient, dpv_risk_owl:HumanOversightInsufficient |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HumanOversightInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HumanOversightInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing cases where human oversight is insufficient for
  the

  intended effect, such as not being capable of identifying a problem'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Human Oversight Insufficient
exact_mappings:
- dpv_risk:HumanOversightInsufficient
- dpv_risk_owl:HumanOversightInsufficient
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:HumanOversightInsufficient

```
</details>

### Induced

<details>
```yaml
name: HumanOversightInsufficient
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HumanOversightInsufficient
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing cases where human oversight is insufficient for
  the

  intended effect, such as not being capable of identifying a problem'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Human Oversight Insufficient
exact_mappings:
- dpv_risk:HumanOversightInsufficient
- dpv_risk_owl:HumanOversightInsufficient
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:HumanOversightInsufficient

```
</details></div>