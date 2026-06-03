---
search:
  boost: 10.0
---

# Class: TestingDataIncomplete 


_Concept representing testing data being incomplete_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataIncomplete](https://w3id.org/lmodel/dpv/ai/TestingDataIncomplete)





```mermaid
 classDiagram
    class TestingDataIncomplete
    click TestingDataIncomplete href "../TestingDataIncomplete/"
      RiskConcept <|-- TestingDataIncomplete
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataIncomplete
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataIncomplete** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataIncomplete](https://w3id.org/lmodel/dpv/ai/TestingDataIncomplete) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Incomplete




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataIncomplete |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataIncomplete |
| native | ai:TestingDataIncomplete |
| exact | dpv_ai:TestingDataIncomplete, dpv_ai_owl:TestingDataIncomplete |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataIncomplete
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataIncomplete
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being incomplete
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Incomplete
exact_mappings:
- dpv_ai:TestingDataIncomplete
- dpv_ai_owl:TestingDataIncomplete
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataIncomplete

```
</details>

### Induced

<details>
```yaml
name: TestingDataIncomplete
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataIncomplete
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being incomplete
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Incomplete
exact_mappings:
- dpv_ai:TestingDataIncomplete
- dpv_ai_owl:TestingDataIncomplete
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataIncomplete

```
</details></div>