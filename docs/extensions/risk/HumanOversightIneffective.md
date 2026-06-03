---
search:
  boost: 10.0
---

# Class: HumanOversightIneffective 


_Concept representing cases where human oversight is ineffective for the_

_intended effect, such as for when human can observe a problem but cannot_

_do anything about it_



<div data-search-exclude markdown="1">



URI: [risk:HumanOversightIneffective](https://w3id.org/lmodel/dpv/risk/HumanOversightIneffective)





```mermaid
 classDiagram
    class HumanOversightIneffective
    click HumanOversightIneffective href "../HumanOversightIneffective/"
      PotentialConsequence <|-- HumanOversightIneffective
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- HumanOversightIneffective
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- HumanOversightIneffective
        click PotentialRiskSource href "../PotentialRiskSource/"
      OrganisationalManagementRisk <|-- HumanOversightIneffective
        click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OrganisationalManagementRisk](OrganisationalManagementRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **HumanOversightIneffective** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:HumanOversightIneffective](https://w3id.org/lmodel/dpv/risk/HumanOversightIneffective) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Human Oversight Ineffective




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#HumanOversightIneffective |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:HumanOversightIneffective |
| native | risk:HumanOversightIneffective |
| exact | dpv_risk:HumanOversightIneffective, dpv_risk_owl:HumanOversightIneffective |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HumanOversightIneffective
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HumanOversightIneffective
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing cases where human oversight is ineffective for
  the

  intended effect, such as for when human can observe a problem but cannot

  do anything about it'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Human Oversight Ineffective
exact_mappings:
- dpv_risk:HumanOversightIneffective
- dpv_risk_owl:HumanOversightIneffective
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:HumanOversightIneffective

```
</details>

### Induced

<details>
```yaml
name: HumanOversightIneffective
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#HumanOversightIneffective
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing cases where human oversight is ineffective for
  the

  intended effect, such as for when human can observe a problem but cannot

  do anything about it'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Human Oversight Ineffective
exact_mappings:
- dpv_risk:HumanOversightIneffective
- dpv_risk_owl:HumanOversightIneffective
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:HumanOversightIneffective

```
</details></div>