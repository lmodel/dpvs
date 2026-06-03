---
search:
  boost: 10.0
---

# Class: BehaviourDistortion 


_Concept representing distortion of behaviour of individual(s)_



<div data-search-exclude markdown="1">



URI: [risk:BehaviourDistortion](https://w3id.org/lmodel/dpv/risk/BehaviourDistortion)





```mermaid
 classDiagram
    class BehaviourDistortion
    click BehaviourDistortion href "../BehaviourDistortion/"
      PotentialConsequence <|-- BehaviourDistortion
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- BehaviourDistortion
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- BehaviourDistortion
        click PotentialRisk href "../PotentialRisk/"
      IndividualRisk <|-- BehaviourDistortion
        click IndividualRisk href "../IndividualRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **BehaviourDistortion** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:BehaviourDistortion](https://w3id.org/lmodel/dpv/risk/BehaviourDistortion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Behaviour Distortion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#BehaviourDistortion |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:BehaviourDistortion |
| native | risk:BehaviourDistortion |
| exact | dpv_risk:BehaviourDistortion, dpv_risk_owl:BehaviourDistortion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BehaviourDistortion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#BehaviourDistortion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing distortion of behaviour of individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Behaviour Distortion
exact_mappings:
- dpv_risk:BehaviourDistortion
- dpv_risk_owl:BehaviourDistortion
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:BehaviourDistortion

```
</details>

### Induced

<details>
```yaml
name: BehaviourDistortion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#BehaviourDistortion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing distortion of behaviour of individual(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Behaviour Distortion
exact_mappings:
- dpv_risk:BehaviourDistortion
- dpv_risk_owl:BehaviourDistortion
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:BehaviourDistortion

```
</details></div>