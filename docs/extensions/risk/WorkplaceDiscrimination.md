---
search:
  boost: 10.0
---

# Class: WorkplaceDiscrimination 


_Discrimination occurring at workplace or in the context of work_

_environments_



<div data-search-exclude markdown="1">



URI: [risk:WorkplaceDiscrimination](https://w3id.org/lmodel/dpv/risk/WorkplaceDiscrimination)





```mermaid
 classDiagram
    class WorkplaceDiscrimination
    click WorkplaceDiscrimination href "../WorkplaceDiscrimination/"
      PotentialConsequence <|-- WorkplaceDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- WorkplaceDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- WorkplaceDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- WorkplaceDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **WorkplaceDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:WorkplaceDiscrimination](https://w3id.org/lmodel/dpv/risk/WorkplaceDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Workplace Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#WorkplaceDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:WorkplaceDiscrimination |
| native | risk:WorkplaceDiscrimination |
| exact | dpv_risk:WorkplaceDiscrimination, dpv_risk_owl:WorkplaceDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WorkplaceDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#WorkplaceDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination occurring at workplace or in the context of work

  environments'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Workplace Discrimination
exact_mappings:
- dpv_risk:WorkplaceDiscrimination
- dpv_risk_owl:WorkplaceDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:WorkplaceDiscrimination

```
</details>

### Induced

<details>
```yaml
name: WorkplaceDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#WorkplaceDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination occurring at workplace or in the context of work

  environments'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Workplace Discrimination
exact_mappings:
- dpv_risk:WorkplaceDiscrimination
- dpv_risk_owl:WorkplaceDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:WorkplaceDiscrimination

```
</details></div>