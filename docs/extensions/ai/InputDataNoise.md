---
search:
  boost: 10.0
---

# Class: InputDataNoise 


_Concept representing input data being noisy_



<div data-search-exclude markdown="1">



URI: [ai:InputDataNoise](https://w3id.org/lmodel/dpv/ai/InputDataNoise)





```mermaid
 classDiagram
    class InputDataNoise
    click InputDataNoise href "../InputDataNoise/"
      RiskConcept <|-- InputDataNoise
        click RiskConcept href "../RiskConcept/"
      InputDataRisk <|-- InputDataNoise
        click InputDataRisk href "../InputDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [InputDataRisk](InputDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **InputDataNoise** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:InputDataNoise](https://w3id.org/lmodel/dpv/ai/InputDataNoise) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Input Data Noise




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#InputDataNoise |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:InputDataNoise |
| native | ai:InputDataNoise |
| exact | dpv_ai:InputDataNoise, dpv_ai_owl:InputDataNoise |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InputDataNoise
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataNoise
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being noisy
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Noise
exact_mappings:
- dpv_ai:InputDataNoise
- dpv_ai_owl:InputDataNoise
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataNoise

```
</details>

### Induced

<details>
```yaml
name: InputDataNoise
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#InputDataNoise
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing input data being noisy
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Input Data Noise
exact_mappings:
- dpv_ai:InputDataNoise
- dpv_ai_owl:InputDataNoise
is_a: InputDataRisk
mixins:
- RiskConcept
class_uri: ai:InputDataNoise

```
</details></div>