---
search:
  boost: 10.0
---

# Class: IncidentMonitoringStage 


_The stage in the lifecycle where an AI system is actively being_

_monitored for incidents_



<div data-search-exclude markdown="1">



URI: [ai:IncidentMonitoringStage](https://w3id.org/lmodel/dpv/ai/IncidentMonitoringStage)





```mermaid
 classDiagram
    class IncidentMonitoringStage
    click IncidentMonitoringStage href "../IncidentMonitoringStage/"
      LifecycleStage <|-- IncidentMonitoringStage
        click LifecycleStage href "../LifecycleStage/"
      OperationStage <|-- IncidentMonitoringStage
        click OperationStage href "../OperationStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * [OperationStage](OperationStage.md)
        * **IncidentMonitoringStage** [ [LifecycleStage](LifecycleStage.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:IncidentMonitoringStage](https://w3id.org/lmodel/dpv/ai/IncidentMonitoringStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Incident Monitoring Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#IncidentMonitoringStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:IncidentMonitoringStage |
| native | ai:IncidentMonitoringStage |
| exact | dpv_ai:IncidentMonitoringStage, dpv_ai_owl:IncidentMonitoringStage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncidentMonitoringStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#IncidentMonitoringStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where an AI system is actively being

  monitored for incidents'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Incident Monitoring Stage
exact_mappings:
- dpv_ai:IncidentMonitoringStage
- dpv_ai_owl:IncidentMonitoringStage
is_a: OperationStage
mixins:
- LifecycleStage
class_uri: ai:IncidentMonitoringStage

```
</details>

### Induced

<details>
```yaml
name: IncidentMonitoringStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#IncidentMonitoringStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where an AI system is actively being

  monitored for incidents'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Incident Monitoring Stage
exact_mappings:
- dpv_ai:IncidentMonitoringStage
- dpv_ai_owl:IncidentMonitoringStage
is_a: OperationStage
mixins:
- LifecycleStage
class_uri: ai:IncidentMonitoringStage

```
</details></div>