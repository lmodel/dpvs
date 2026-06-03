---
search:
  boost: 10.0
---

# Class: TestingDataSelectionError 


_Concept representing an error in testing data selection_



<div data-search-exclude markdown="1">



URI: [ai:TestingDataSelectionError](https://w3id.org/lmodel/dpv/ai/TestingDataSelectionError)





```mermaid
 classDiagram
    class TestingDataSelectionError
    click TestingDataSelectionError href "../TestingDataSelectionError/"
      RiskConcept <|-- TestingDataSelectionError
        click RiskConcept href "../RiskConcept/"
      TestingDataRisk <|-- TestingDataSelectionError
        click TestingDataRisk href "../TestingDataRisk/"
      
      
```





## Inheritance
* [RiskConcept](RiskConcept.md)
    * [DataRisk](DataRisk.md)
        * [TestingDataRisk](TestingDataRisk.md) [ [RiskConcept](RiskConcept.md)]
            * **TestingDataSelectionError** [ [RiskConcept](RiskConcept.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ai:TestingDataSelectionError](https://w3id.org/lmodel/dpv/ai/TestingDataSelectionError) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [AiSubset](AiSubset.md)



## Aliases


* Testing Data Selection Error




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/ai/owl#TestingDataSelectionError |
| dpv_extension_slug | ai |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/ai




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ai:TestingDataSelectionError |
| native | ai:TestingDataSelectionError |
| exact | dpv_ai:TestingDataSelectionError, dpv_ai_owl:TestingDataSelectionError |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TestingDataSelectionError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataSelectionError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing an error in testing data selection
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Selection Error
exact_mappings:
- dpv_ai:TestingDataSelectionError
- dpv_ai_owl:TestingDataSelectionError
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataSelectionError

```
</details>

### Induced

<details>
```yaml
name: TestingDataSelectionError
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/ai/owl#TestingDataSelectionError
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: ai
description: Concept representing an error in testing data selection
in_subset:
- ai_subset
from_schema: https://w3id.org/lmodel/dpv/ai
aliases:
- Testing Data Selection Error
exact_mappings:
- dpv_ai:TestingDataSelectionError
- dpv_ai_owl:TestingDataSelectionError
is_a: TestingDataRisk
mixins:
- RiskConcept
class_uri: ai:TestingDataSelectionError

```
</details></div>