---
search:
  boost: 10.0
---

# Class: TaskExecutionIncorrect 


_Concept representing incorrect execution of task(s)_



<div data-search-exclude markdown="1">



URI: [risk:TaskExecutionIncorrect](https://w3id.org/lmodel/dpv/risk/TaskExecutionIncorrect)





```mermaid
 classDiagram
    class TaskExecutionIncorrect
    click TaskExecutionIncorrect href "../TaskExecutionIncorrect/"
      AvailabilityConcept <|-- TaskExecutionIncorrect
        click AvailabilityConcept href "../AvailabilityConcept/"
      IntegrityConcept <|-- TaskExecutionIncorrect
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- TaskExecutionIncorrect
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- TaskExecutionIncorrect
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- TaskExecutionIncorrect
        click PotentialRiskSource href "../PotentialRiskSource/"
      TaskExecutionRisk <|-- TaskExecutionIncorrect
        click TaskExecutionRisk href "../TaskExecutionRisk/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OperationalSecurityRisk](OperationalSecurityRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [TaskExecutionRisk](TaskExecutionRisk.md) [ [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **TaskExecutionIncorrect** [ [AvailabilityConcept](AvailabilityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:TaskExecutionIncorrect](https://w3id.org/lmodel/dpv/risk/TaskExecutionIncorrect) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Task Execution Incorrect




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#TaskExecutionIncorrect |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:TaskExecutionIncorrect |
| native | risk:TaskExecutionIncorrect |
| exact | dpv_risk:TaskExecutionIncorrect, dpv_risk_owl:TaskExecutionIncorrect |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TaskExecutionIncorrect
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TaskExecutionIncorrect
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing incorrect execution of task(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Task Execution Incorrect
exact_mappings:
- dpv_risk:TaskExecutionIncorrect
- dpv_risk_owl:TaskExecutionIncorrect
is_a: TaskExecutionRisk
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TaskExecutionIncorrect

```
</details>

### Induced

<details>
```yaml
name: TaskExecutionIncorrect
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#TaskExecutionIncorrect
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing incorrect execution of task(s)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Task Execution Incorrect
exact_mappings:
- dpv_risk:TaskExecutionIncorrect
- dpv_risk_owl:TaskExecutionIncorrect
is_a: TaskExecutionRisk
mixins:
- AvailabilityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:TaskExecutionIncorrect

```
</details></div>