---
search:
  boost: 10.0
---

# Class: TestingDataBias 


_Concept representing testing data containing or potentially containing_

_bias_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataBias](https://w3id.org/lmodel/dpv/ai/TestingDataBias)





```mermaid
 classDiagram
    class TestingDataBias
    click TestingDataBias href "../TestingDataBias/"
      RiskConcept <|-- TestingDataBias
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataBias
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataBias** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataBias](https://w3id.org/lmodel/dpv/ai/TestingDataBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataBias |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataBias |
| native | ai:TestingDataBias |
| exact | dpv_ai:TestingDataBias, dpv_ai_owl:TestingDataBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataBias
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Concept representing testing data containing or potentially containing

  bias'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Bias
exact_mappings:
- dpv_ai:TestingDataBias
- dpv_ai_owl:TestingDataBias
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataBias

```
</details>

### Induced

<details>
```yaml
name: TestingDataBias
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: 'Concept representing testing data containing or potentially containing

  bias'
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Bias
exact_mappings:
- dpv_ai:TestingDataBias
- dpv_ai_owl:TestingDataBias
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataBias

```
</details></div>