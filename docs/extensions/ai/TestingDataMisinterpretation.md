---
search:
  boost: 10.0
---

# Class: TestingDataMisinterpretation 


_Concept representing testing data being misinterpreted_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataMisinterpretation](https://w3id.org/lmodel/dpv/ai/TestingDataMisinterpretation)





```mermaid
 classDiagram
    class TestingDataMisinterpretation
    click TestingDataMisinterpretation href "../TestingDataMisinterpretation/"
      RiskConcept <|-- TestingDataMisinterpretation
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataMisinterpretation
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataMisinterpretation** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataMisinterpretation](https://w3id.org/lmodel/dpv/ai/TestingDataMisinterpretation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Misinterpretation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataMisinterpretation |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataMisinterpretation |
| native | ai:TestingDataMisinterpretation |
| exact | dpv_ai:TestingDataMisinterpretation, dpv_ai_owl:TestingDataMisinterpretation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataMisinterpretation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataMisinterpretation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being misinterpreted
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Misinterpretation
exact_mappings:
- dpv_ai:TestingDataMisinterpretation
- dpv_ai_owl:TestingDataMisinterpretation
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataMisinterpretation

```
</details>

### Induced

<details>
```yaml
name: TestingDataMisinterpretation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataMisinterpretation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing testing data being misinterpreted
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Misinterpretation
exact_mappings:
- dpv_ai:TestingDataMisinterpretation
- dpv_ai_owl:TestingDataMisinterpretation
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataMisinterpretation

```
</details></div>