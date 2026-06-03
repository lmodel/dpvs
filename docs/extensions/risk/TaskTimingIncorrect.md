---
search:
  boost: 10.0
---

# Class: TaskTimingIncorrect 


_Concept representing incorrect timing for task(s) i.e. the task_

_execution does not occur at the correct time_



<div data-search-exclude markdown="1">



URI: [risk:TaskTimingIncorrect](https://w3id.org/lmodel/dpv/risk/TaskTimingIncorrect)





```mermaid
 classDiagram
    class TaskTimingIncorrect
    click TaskTimingIncorrect href "../TaskTimingIncorrect/"
      AvailabilityConcept <|-- TaskTimingIncorrect
        click AvailabilityConcept href "../AvailabilityConcept/"
      IntegrityConcept <|-- TaskTimingIncorrect
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- TaskTimingIncorrect
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- TaskTimingIncorrect
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- TaskTimingIncorrect
        click PotentialRiskSource href "../PotentialRiskSource/"
      TaskExecutionRisk <|-- TaskTimingIncorrect
        click TaskExecutionRisk href "../TaskExecutionRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [TaskExecutionRisk](TaskExecutionRisk.md) [ [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **TaskTimingIncorrect** [ [AvailabilityConcept](AvailabilityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:TaskTimingIncorrect](https://w3id.org/lmodel/dpv/risk/TaskTimingIncorrect) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Task Timing Incorrect




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#TaskTimingIncorrect |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:TaskTimingIncorrect |
| native | risk:TaskTimingIncorrect |
| exact | dpv_risk:TaskTimingIncorrect, dpv_risk_owl:TaskTimingIncorrect |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TaskTimingIncorrect
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TaskTimingIncorrect
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing incorrect timing for task(s) i.e. the task

  execution does not occur at the correct time'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Task Timing Incorrect
exact_mappings:
- dpv_risk:TaskTimingIncorrect
- dpv_risk_owl:TaskTimingIncorrect
is_a: TaskExecutionRisk
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TaskTimingIncorrect

```
</details>

### Induced

<details>
```yaml
name: TaskTimingIncorrect
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TaskTimingIncorrect
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing incorrect timing for task(s) i.e. the task

  execution does not occur at the correct time'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Task Timing Incorrect
exact_mappings:
- dpv_risk:TaskTimingIncorrect
- dpv_risk_owl:TaskTimingIncorrect
is_a: TaskExecutionRisk
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TaskTimingIncorrect

```
</details></div>