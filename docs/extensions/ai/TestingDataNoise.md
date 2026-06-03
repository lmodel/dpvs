---
search:
  boost: 10.0
---

# Class: TestingDataNoise 


_Concept representing testing data being noisy_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataNoise](https://w3id.org/lmodel/dpv/ai/TestingDataNoise)





```mermaid
 classDiagram
    class TestingDataNoise
    click TestingDataNoise href "../TestingDataNoise/"
      RiskConcept <|-- TestingDataNoise
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataNoise
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataNoise** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataNoise](https://w3id.org/lmodel/dpv/ai/TestingDataNoise) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Noise




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataNoise |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataNoise |
| native | ai:TestingDataNoise |
| exact | dpv_ai:TestingDataNoise, dpv_ai_owl:TestingDataNoise |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataNoise
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataNoise
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being noisy
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Noise
exact_mappings:
- dpv_ai:TestingDataNoise
- dpv_ai_owl:TestingDataNoise
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataNoise

```
</details>

### Induced

<details>
```yaml
name: TestingDataNoise
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataNoise
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being noisy
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Noise
exact_mappings:
- dpv_ai:TestingDataNoise
- dpv_ai_owl:TestingDataNoise
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataNoise

```
</details></div>