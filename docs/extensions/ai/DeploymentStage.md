---
search:
  boost: 10.0
---

# Class: DeploymentStage 


_The stage in the lifecycle where the AI system is installed, released or_

_configured for deployment and operation in a target environment_



<div data-search-exclude markdown="1">



URI: [ai:DeploymentStage](https://w3id.org/lmodel/dpv/ai/DeploymentStage)





```mermaid
 classDiagram
    class DeploymentStage
    click DeploymentStage href "../DeploymentStage/"
      LifecycleStage <|-- DeploymentStage
        click LifecycleStage href "../LifecycleStage/"
      
      
```





## Inheritance
* [LifecycleStage](LifecycleStage.md)
    * **DeploymentStage**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:DeploymentStage](https://w3id.org/lmodel/dpv/ai/DeploymentStage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Deployment Stage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/ai/owl#DeploymentStage |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:DeploymentStage |
| native | ai:DeploymentStage |
| exact | dpv_ai:DeploymentStage, dpv_ai_owl:DeploymentStage |
| close | iso42001:AIReferenceControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DeploymentStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DeploymentStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is installed, released
  or

  configured for deployment and operation in a target environment'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Deployment Stage
exact_mappings:
- dpv_ai:DeploymentStage
- dpv_ai_owl:DeploymentStage
close_mappings:
- iso42001:AIReferenceControl
is_a: LifecycleStage
class_uri: ai:DeploymentStage

```
</details>

### Induced

<details>
```yaml
name: DeploymentStage
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#DeploymentStage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'The stage in the lifecycle where the AI system is installed, released
  or

  configured for deployment and operation in a target environment'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Deployment Stage
exact_mappings:
- dpv_ai:DeploymentStage
- dpv_ai_owl:DeploymentStage
close_mappings:
- iso42001:AIReferenceControl
is_a: LifecycleStage
class_uri: ai:DeploymentStage

```
</details></div>