---
search:
  boost: 10.0
---

# Class: TaskOmitted 


_Concept representing omission of task(s)_



<div data-search-exclude markdown="1">



URI: [risk:TaskOmitted](https://w3id.org/lmodel/dpv/risk/TaskOmitted)





```mermaid
 classDiagram
    class TaskOmitted
    click TaskOmitted href "../TaskOmitted/"
      AvailabilityConcept <|-- TaskOmitted
        click AvailabilityConcept href "../AvailabilityConcept/"
      IntegrityConcept <|-- TaskOmitted
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- TaskOmitted
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- TaskOmitted
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- TaskOmitted
        click PotentialRiskSource href "../PotentialRiskSource/"
      TaskExecutionRisk <|-- TaskOmitted
        click TaskExecutionRisk href "../TaskExecutionRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [TaskExecutionRisk](TaskExecutionRisk.md) [ [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **TaskOmitted** [ [AvailabilityConcept](AvailabilityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:TaskOmitted](https://w3id.org/lmodel/dpv/risk/TaskOmitted) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Task Omitted




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#TaskOmitted |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:TaskOmitted |
| native | risk:TaskOmitted |
| exact | dpv_risk:TaskOmitted, dpv_risk_owl:TaskOmitted |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TaskOmitted
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TaskOmitted
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing omission of task(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Task Omitted
exact_mappings:
- dpv_risk:TaskOmitted
- dpv_risk_owl:TaskOmitted
is_a: TaskExecutionRisk
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TaskOmitted

```
</details>

### Induced

<details>
```yaml
name: TaskOmitted
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TaskOmitted
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing omission of task(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Task Omitted
exact_mappings:
- dpv_risk:TaskOmitted
- dpv_risk_owl:TaskOmitted
is_a: TaskExecutionRisk
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TaskOmitted

```
</details></div>