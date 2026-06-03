---
search:
  boost: 10.0
---

# Class: TaskExecutionRisk 


_Concept representing risks and issues associated with execution of_

_tasks, operations, activities, and other similar processes_



<div data-search-exclude markdown="1">



URI: [risk:TaskExecutionRisk](https://w3id.org/lmodel/dpv/risk/TaskExecutionRisk)





```mermaid
 classDiagram
    class TaskExecutionRisk
    click TaskExecutionRisk href "../TaskExecutionRisk/"
      IntegrityConcept <|-- TaskExecutionRisk
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- TaskExecutionRisk
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- TaskExecutionRisk
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- TaskExecutionRisk
        click PotentialRiskSource href "../PotentialRiskSource/"
      OperationalSecurityRisk <|-- TaskExecutionRisk
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      

      TaskExecutionRisk <|-- TaskExecutionIncorrect
        click TaskExecutionIncorrect href "../TaskExecutionIncorrect/"
      TaskExecutionRisk <|-- TaskOmitted
        click TaskOmitted href "../TaskOmitted/"
      TaskExecutionRisk <|-- TaskTimingIncorrect
        click TaskTimingIncorrect href "../TaskTimingIncorrect/"
      

      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **TaskExecutionRisk** [ [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [TaskExecutionIncorrect](TaskExecutionIncorrect.md) [ [AvailabilityConcept](AvailabilityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [TaskOmitted](TaskOmitted.md) [ [AvailabilityConcept](AvailabilityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [TaskTimingIncorrect](TaskTimingIncorrect.md) [ [AvailabilityConcept](AvailabilityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:TaskExecutionRisk](https://w3id.org/lmodel/dpv/risk/TaskExecutionRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Task Execution Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#TaskExecutionRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:TaskExecutionRisk |
| native | risk:TaskExecutionRisk |
| exact | dpv_risk:TaskExecutionRisk, dpv_risk_owl:TaskExecutionRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TaskExecutionRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TaskExecutionRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing risks and issues associated with execution of

  tasks, operations, activities, and other similar processes'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Task Execution Risk
exact_mappings:
- dpv_risk:TaskExecutionRisk
- dpv_risk_owl:TaskExecutionRisk
is_a: OperationalSecurityRisk
mixins:
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TaskExecutionRisk

```
</details>

### Induced

<details>
```yaml
name: TaskExecutionRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TaskExecutionRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing risks and issues associated with execution of

  tasks, operations, activities, and other similar processes'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Task Execution Risk
exact_mappings:
- dpv_risk:TaskExecutionRisk
- dpv_risk_owl:TaskExecutionRisk
is_a: OperationalSecurityRisk
mixins:
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TaskExecutionRisk

```
</details></div>