---
search:
  boost: 10.0
---

# Class: ValidationDataNoise 


_Concept representing validation data being noisy_



<div data-search-exclude markdown="1">



URI: [ai:ValidationDataNoise](https://w3id.org/lmodel/dpv/ai/ValidationDataNoise)





```mermaid
 classDiagram
    class ValidationDataNoise
    click ValidationDataNoise href "../ValidationDataNoise/"
      RiskConcept <|-- ValidationDataNoise
        click RiskConcept href "../RiskConcept/"
      ValidationDataRisk <|-- ValidationDataNoise
        click ValidationDataRisk href "../ValidationDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [ValidationDataRisk](ValidationDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **ValidationDataNoise** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:ValidationDataNoise](https://w3id.org/lmodel/dpv/ai/ValidationDataNoise) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Validation Data Noise




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#ValidationDataNoise |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:ValidationDataNoise |
| native | ai:ValidationDataNoise |
| exact | dpv_ai:ValidationDataNoise, dpv_ai_owl:ValidationDataNoise |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ValidationDataNoise
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataNoise
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being noisy
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Noise
exact_mappings:
- dpv_ai:ValidationDataNoise
- dpv_ai_owl:ValidationDataNoise
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataNoise

```
</details>

### Induced

<details>
```yaml
name: ValidationDataNoise
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#ValidationDataNoise
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing validation data being noisy
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Validation Data Noise
exact_mappings:
- dpv_ai:ValidationDataNoise
- dpv_ai_owl:ValidationDataNoise
is_a: ValidationDataRisk
mixins:
- RiskConcept
class_uri: ai:ValidationDataNoise

```
</details></div>