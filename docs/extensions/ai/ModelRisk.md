---
search:
  boost: 10.0
---

# Class: ModelRisk 


_Risks associated with AI Models_



<div data-search-exclude markdown="1">



URI: [ai:ModelRisk](https://w3id.org/lmodel/dpv/ai/ModelRisk)





```mermaid
 classDiagram
    class ModelRisk
    click ModelRisk href "../ModelRisk/"
      RiskConcept <|-- ModelRisk
        click RiskConcept href "../RiskConcept/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * **ModelRisk**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ModelRisk](https://w3id.org/lmodel/dpv/ai/ModelRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Model Risk




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ModelRisk |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ModelRisk |
| native | ai:ModelRisk |
| exact | dpv_ai:ModelRisk, dpv_ai_owl:ModelRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModelRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ModelRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Risks associated with AI Models
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Model Risk
exact_mappings:
- dpv_ai:ModelRisk
- dpv_ai_owl:ModelRisk
is_a: RiskConcept
class_uri: ai:ModelRisk

```
</details>

### Induced

<details>
```yaml
name: ModelRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ModelRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Risks associated with AI Models
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Model Risk
exact_mappings:
- dpv_ai:ModelRisk
- dpv_ai_owl:ModelRisk
is_a: RiskConcept
class_uri: ai:ModelRisk

```
</details></div>